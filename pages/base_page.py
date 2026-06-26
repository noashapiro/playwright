class BasePage:
    BASE_URL = "https://demowebshop.tricentis.com"

    def __init__(self, page):
        self.page = page

    def navigate(self, path=""):
        self.page.goto(f"{self.BASE_URL}{path}")
