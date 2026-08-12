from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page.add_backpack()
        main_page.add_bolt_t_shirt()
        main_page.add_onesie()
        main_page.open_cart()

        products = cart_page.check_products()

        assert "Sauce Labs Backpack" in products
        assert "Sauce Labs Bolt T-Shirt" in products
        assert "Sauce Labs Onesie" in products

        cart_page.checkout()

        checkout_page.fill_form(
            "Джансият",
            "Бабатова",
            "368600"
        )

        total = checkout_page.get_total()

        assert total == "Total: $58.29"

    finally:
        driver.quit()
