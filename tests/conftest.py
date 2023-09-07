import os

import pytest

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="100.0")
    parser.addoption("--browser_url", default='')


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    options = Options()

    options.add_argument("window-size=2800,1400")
    browser.config.base_url = "https://demoqa.com"

    browser_url = request.config.getoption("--browser_url")
    if browser_url:
        browser_version = request.config.getoption("--browser_version")

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{browser_url}",
            options=options,
        )

        browser.config.driver = driver

    browser.config.driver_options = options

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
