import random

from pages.base_page import BasePage


class DigitalDownloadsPage(BasePage):
    PRODUCT_TITLES = ".product-item .product-title a"
    ADD_TO_CART_BUTTON = ".product-item .button-2.product-box-add-to-cart-button"
    NOTIFICATION_BAR = "#bar-notification .content"

    def get_product_names(self):
        self.page.wait_for_selector(self.PRODUCT_TITLES)
        return self.page.locator(self.PRODUCT_TITLES).all_inner_texts()

    def add_random_product_to_cart(self):
        self.page.wait_for_selector(self.PRODUCT_TITLES)
        products = self.page.locator(self.PRODUCT_TITLES)
        buttons = self.page.locator(self.ADD_TO_CART_BUTTON)

        index = random.randint(0, products.count() - 1)
        name = products.nth(index).inner_text()
        buttons.nth(index).click()

        self.page.wait_for_selector(self.NOTIFICATION_BAR)
        return name
