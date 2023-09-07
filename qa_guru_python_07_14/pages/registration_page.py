from selene import browser, have, command

from qa_guru_python_07_14.resources import resource_path


class RegistrationPage:
    def __init__(self):
        self.google_ad = browser.all('[id^=google_ads][id$=container__]')
        self.drop_down_options = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')

        self.google_ad.with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
        self.google_ad.perform(command.js.remove)
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.8)"'
        )

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def fill_user_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element(
            '..'
        ).click()
        return self

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__month-select').all('option').element_by(
            have.exact_text(month)
        ).click()

        browser.element('.react-datepicker__year-select').all('option').element_by(
            have.exact_text(year)
        ).click()
        browser.element(
            f'.react-datepicker__day--00{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_tab()
        return self

    def fill_hobbies(self, hobby):
        browser.all('[id^=hobbies][type=checkbox]+label').element_by(
            have.exact_text(hobby)
        ).click()
        return self

    def upload_picture(self, picture_path):
        browser.element('#uploadPicture').set_value(resource_path(picture_path))
        return self

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address).press_tab()
        return self

    def fill_state(self, state):
        browser.element('#state').click()

        self.drop_down_options.element_by(have.exact_text(state)).click()
        return self

    def fill_city(self, city):
        browser.element('#city').click()

        self.drop_down_options.element_by(have.exact_text(city)).click()
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def modal_form_pops_up(self):
        browser.element('.modal-header>.modal-title').should(
            have.text('Thanks for submitting the form')
        )

    def student_should_be_registered(
        self,
        name,
        email,
        gender,
        phone_number,
        date_of_birth,
        subject,
        hobby,
        picture,
        address,
        state_and_city,
    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                address,
                state_and_city,
            )
        )
