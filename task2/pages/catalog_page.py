from selenium.webdriver import ActionChains

from task2.locators.catalog_page_locator import BN_ZIMA, BN_SANKY, BN_ONLINER_PRIME
from task2.pages.base_page import BasePage


class CatalogPage(BasePage):

    @property
    def zima(self):
        return self.wait_for(BN_ZIMA)

    @property
    def sanky(self):
        return self.wait_for(BN_SANKY)

    def click_onliner_prime(self):
        self.click(BN_ONLINER_PRIME)

    def go_to_sanky(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.zima).perform()
        action.move_to_element(self.sanky).perform()
        action.click().perform()