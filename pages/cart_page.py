from pages.base_page import BasePage


class CartPage(BasePage):
    CART_LINK = ".ico-cart"
    CART_PRODUCT_NAMES = ".cart-item-row .product .product-name"

    def open_via_header(self):
        self.page.click(self.CART_LINK)
        return self

    def get_product_names(self):
        self.page.wait_for_selector(self.CART_PRODUCT_NAMES)
        return self.page.locator(self.CART_PRODUCT_NAMES).all_inner_texts()
