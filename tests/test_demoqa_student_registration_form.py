import allure
from allure_commons._allure import step

from allure_commons.types import Severity
from qa_guru_python_07_14.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Anhelina Babareka")
@allure.feature("Student Registration Form")
@allure.story("Student is successfully registered")
@allure.link("https://demoqa.com/", name="Testing")
def test_successful_student_registration_form():
    # Given
    with step("Open registration page"):
        registration_page = RegistrationPage()
        registration_page.open()

    # When
    with step("Fill in the first name"):
        registration_page.fill_first_name("John")

    with step("Fill in the last name"):
        registration_page.fill_last_name("Doe")

    with step("Fill in the email"):
        registration_page.fill_user_email("test_email.demoqa@test.com")

    with step("Fill in the gender"):
        registration_page.fill_gender("Male")

    with step("Fill in the phone number"):
        registration_page.fill_phone_number("8800111111")

    with step("Fill in the birthday date"):
        registration_page.fill_date_of_birth("January", "2000", 1)

    with step("Fill in the subjects"):
        registration_page.fill_subjects("computer")

    with step("Fill in the hobbies"):
        registration_page.fill_hobbies("Sports")

    with step("Fill in the picture"):
        registration_page.upload_picture("student.png")

    with step("Fill in the current address"):
        registration_page.fill_current_address(
            "42 Best street, suite 1, Dallas, TX, 11111"
        )

    with step("Fill in the state"):
        registration_page.fill_state("NCR")

    with step("Fill in the city"):
        registration_page.fill_city("Delhi")

    with step("Submit the form"):
        registration_page.submit_form()

    # Then
    with step("Verify the confirmation modal form pops up"):
        registration_page.modal_form_pops_up()

    with step("Verify the student is registered with the correct data"):
        registration_page.student_should_be_registered(
            "John Doe",
            "test_email.demoqa@test.com",
            "Male",
            "8800111111",
            "01 January,2000",
            "Computer Science",
            "Sports",
            "student.png",
            "42 Best street, suite 1, Dallas, TX, 11111",
            "NCR Delhi",
        )
