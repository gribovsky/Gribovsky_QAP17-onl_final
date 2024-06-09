import time

import pytest

from task2.pages.catalog_page import CatalogPage
from task2.pages.main_page import MainPage
from task2.pages.product_page import ProductPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def product_page(driver):
    yield ProductPage(driver)


class TestCatalog:
    def test_catalog(self, main_page, catalog_page, product_page):
        main_page.click_bn_catalog()
        catalog_page.click_onliner_prime()
        catalog_page.go_to_sanky()
        product_page.click_brand_select()
        product_page.click_nika()
        product_page.check_nika_clicked()
        product_page.click_first()
        product_page.check_select_first_clicked()
        product_page.add_to_cart()
        product_page.go_to_cart()
