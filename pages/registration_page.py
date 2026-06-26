from pages.base_page import BasePage


class RegistrationPage(BasePage):
    URL = "/register"

    # Locators
    GENDER_MALE = "#gender-male"
    FIRST_NAME = "#FirstName"
    LAST_NAME = "#LastName"
    EMAIL = "#Email"
    PASSWORD = "#Password"
    CONFIRM_PASSWORD = "#ConfirmPassword"
    REGISTER_BUTTON = "#register-button"
    CONTINUE_BUTTON = ".register-continue-button"
    LOGGED_IN_EMAIL = ".header-links .account"

    def open(self):
        self.navigate(self.URL)
        return self

    def fill_registration_form(self, first_name: str, last_name: str, email: str, password: str):
        self.page.click(self.GENDER_MALE)
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.EMAIL, email)
        self.page.fill(self.PASSWORD, password)
        self.page.fill(self.CONFIRM_PASSWORD, password)
        return self

    def submit(self):
        self.page.click(self.REGISTER_BUTTON)
        return self

    def click_continue(self):
        self.page.click(self.CONTINUE_BUTTON)
        return self

    def get_logged_in_email(self) -> str:
        return self.page.locator(self.LOGGED_IN_EMAIL).inner_text()
