from selenium.webdriver import ActionChains

from task2.locators.product_page_locator import SEL_BRAND, BOX_NIKA, LINK_FIRST, BN_ADD_TO_CART, BN_GO_TO_CART
from task2.pages.base_page import BasePage


class ProductPage(BasePage):

    @property
    def select_first(self):
        return self.wait_for_element_to_be_clickable(LINK_FIRST)

    def click_brand_select(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.click(SEL_BRAND)

    def click_nika(self):
        self.click(BOX_NIKA)

    def check_nika_clicked(self):
        self.wait_for(BOX_NIKA).is_selected()

    def click_first(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.select_first).perform()
        action.click().perform()

    def check_select_first_clicked(self):
        self.wait_for(LINK_FIRST).is_selected()


    def add_to_cart(self):
        self.click(BN_ADD_TO_CART)

    def go_to_cart(self):
        self.click(BN_GO_TO_CART)

