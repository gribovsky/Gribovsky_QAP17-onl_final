from task2.locators.main_page_locator import BN_CATALOG
from task2.pages.base_page import BasePage


class MainPage(BasePage):
    def click_bn_catalog(self):
        self.click(BN_CATALOG)
