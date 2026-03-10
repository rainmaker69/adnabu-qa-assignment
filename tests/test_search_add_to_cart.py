from utils.driver_setup import get_driver
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_search_and_add_to_cart():

    driver = get_driver()

    driver.get("https://adnabu-store-assignment1.myshopify.com/")

    home = HomePage(driver)
    product = ProductPage(driver)

    home.open_search()

    home.search_product("shirt")

    home.select_first_product()

    product.add_to_cart()

    assert "products" in driver.current_url.lower()

    driver.quit()