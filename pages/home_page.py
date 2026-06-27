from pages.base_page import BasePage


class HomePage(BasePage):
    REGISTER_LINK = ".ico-register"
    DIGITAL_DOWNLOADS_LINK = ".top-menu a[href='/digital-downloads']"
    LOGGED_IN_EMAIL = ".header-links .account"

    def open(self):
        self.navigate()
        return self

    def click_register(self):
        self.page.click(self.REGISTER_LINK)
        return self

    def click_digital_downloads(self):
        self.page.click(self.DIGITAL_DOWNLOADS_LINK)
        return self

    def get_logged_in_email(self):
        return self.page.locator(self.LOGGED_IN_EMAIL).inner_text()
