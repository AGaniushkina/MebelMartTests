import allure
from playwright.async_api import Page
from playwright.sync_api import expect
import pytest
from pages.likes_page import LikesPage
from pages.sofas_page import SofasPage


@pytest.mark.parametrize(
    "product_name, expected_favorite_name",
    [
        ("Диван Лотос", "Модульный набор для кухни Лотос"),
        ("Диван Мешковина", "Еврокнижка выкатная мешковина Волод"),
        ("Диван замша", "Диван-книжка искусственная замша"),
    ],
)
@allure.title("Добавление '{product_name}' в избранное")
def test_favorites(page: Page, logger, product_name: str, expected_favorite_name: str):

    sofas_page = SofasPage(page, logger)
    favorite_page = LikesPage(page, logger)

    sofas_page.goto()
    sofas_page.add_product_to_favorites_by_name(product_name)
    sofas_page.go_to_favorites()
    favorite_page.confirm_favorites_url()

    expect(sofas_page.page.locator(f"text={expected_favorite_name}")).to_be_visible()
    logger.info(f"'{expected_favorite_name}' найден в избранном")