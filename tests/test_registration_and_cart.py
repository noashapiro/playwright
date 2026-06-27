import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.digital_downloads_page import DigitalDownloadsPage
from pages.cart_page import CartPage
from utils.fake_user import generate_user


@pytest.fixture()
def user():
    return generate_user()


class TestRegistrationAndCart:
    def test_register_and_add_digital_product_to_cart(self, page: Page, user):
        home = HomePage(page)
        home.open()
        home.click_register()

        reg = RegistrationPage(page)
        reg.fill_registration_form(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )
        reg.submit()
        reg.click_continue()

        assert home.get_logged_in_email() == user.email

        home.click_digital_downloads()

        downloads = DigitalDownloadsPage(page)
        product = downloads.add_random_product_to_cart()

        cart = CartPage(page)
        cart.open_via_header()

        assert product in cart.get_product_names()
