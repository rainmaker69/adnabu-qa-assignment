from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    ADD_TO_CART = (By.NAME, "add")
    CART_NOTIFICATION = (By.ID, "cart-notification")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )

        button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.CART_NOTIFICATION)
        )