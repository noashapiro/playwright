"""
End-to-end test: user registration on DemoWebShop followed by
adding a Digital Downloads product to the cart and verifying it.
"""
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
        # ── Step 1-2: Open site and navigate to Register ──────────────────────
        home = HomePage(page)
        home.open()
        home.click_register()

        # ── Step 3-6: Fill form, submit, and continue ─────────────────────────
        reg = RegistrationPage(page)
        reg.fill_registration_form(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )
        reg.submit()
        reg.click_continue()

        # ── Step 7: Validate email appears in the header ──────────────────────
        displayed_email = home.get_logged_in_email()
        assert displayed_email == user.email, (
            f"Expected '{user.email}' in header, got '{displayed_email}'"
        )

        # ── Step 8: Navigate to Digital Downloads ─────────────────────────────
        home.click_digital_downloads()

        # ── Step 9: Add a random product to cart ──────────────────────────────
        downloads = DigitalDownloadsPage(page)
        selected_product = downloads.add_random_product_to_cart()

        # ── Step 10: Open the Shopping Cart ───────────────────────────────────
        cart = CartPage(page)
        cart.open_via_header()

        # ── Step 11: Verify the product name in the cart ──────────────────────
        cart_products = cart.get_product_names()
        assert selected_product in cart_products, (
            f"Expected '{selected_product}' in cart, but cart contains: {cart_products}"
        )
