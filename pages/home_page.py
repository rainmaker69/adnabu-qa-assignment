from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    SEARCH_ICON = (By.CSS_SELECTOR, "summary.header__icon--search")
    SEARCH_INPUT = (By.NAME, "q")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[href*='/products/']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_search(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_ICON)
        ).click()

    def search_product(self, product):

        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search.clear()
        search.send_keys(product)
        search.submit()

    def select_first_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )

        product.click()
