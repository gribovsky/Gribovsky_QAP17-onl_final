from selenium.webdriver.common.by import By

SEL_BRAND = By.XPATH, '(//div[contains(@class, "input-style__real")])[1]'

BOX_NIKA = By.XPATH, '//div[@class="dropdown-style__checkbox-sign"][contains(text(), "Nika")]'

# LINK_FIRST = By.XPATH, '//a[contains(text(), "Санки Nika Тимка 5 универсал (оливковый)")]'
LINK_FIRST = By.XPATH, '(//div[contains(@class, "catalog-form__offers-part catalog-form__offers-part_image")])[1]'

BN_ADD_TO_CART = By.XPATH, '(//a[contains(@class, "product-aside__button_cart")])[1]'

BN_GO_TO_CART = (By.XPATH, '//*[contains(text(), "Перейти в корзину")]')
