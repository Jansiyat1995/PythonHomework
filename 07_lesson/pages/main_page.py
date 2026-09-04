from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )
    BOLT_T_SHIRT = (
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    ONESIE = (
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    )
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK)
        ).click()

    def add_bolt_t_shirt(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT)
        ).click()

    def add_onesie(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ONESIE)
        ).click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()
