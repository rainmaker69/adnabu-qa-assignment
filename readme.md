AdNabu QA Assignment

Project Overview
This project contains test cases and Selenium automation for the AdNabuTestStore ecommerce application.

Automation Scenario
Search for a product and add it to the cart successfully.

Tech Stack
Python
Selenium WebDriver
Pytest
WebDriver Manager

Project Structure

tests/
    test_search_add_to_cart.py

pages/
    home_page.py
    product_page.py

utils/
    driver_setup.py

requirements.txt


Setup Instructions

1. Clone repository

git clone [<this_repo>](https://github.com/rainmaker69/adnabu-qa-assignment)

2. Install dependencies

pip install -r requirements.txt

3. Run the automated test

pytest tests/test_search_add_to_cart.py
