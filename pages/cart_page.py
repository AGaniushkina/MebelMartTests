import re

from playwright.sync_api import Page, expect

import logging

logger = logging.getLogger(__name__)

class CartPage:
    """Страница корзины"""

    URL = "https://mebelmart-saratov.ru/cart"
    ITEM_NAME = "a.font-weight-bold.mb-2"
    ITEM_PRICE = "div.col-md-2.py-2"

    def __init__(self, page: Page, logger):
        self.logger = logger
        self.page = page
        self.price_column = ".col-md-2"
        self.cart_item = "a.font-weight-bold.mb-2"
        self.URL = "https://mebelmart-saratov.ru/cart"

    def goto(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("load")

    def get_item_price(self, product_name: str) -> str:
        row = self.page.locator("div").filter(has=self.page.get_by_role("link", name=product_name)).first
        raw_price = row.locator(self.price_column).first.inner_text()
        return re.sub(r"\D", "", raw_price)

    def get_total_sum(self) -> str:
        raw_total = self.page.locator("text=/^Итого:/").inner_text()
        return re.sub(r"\D", "", raw_total)



