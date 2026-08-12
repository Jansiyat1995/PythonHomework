from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    BACKPACK = (
        By.ID,
        "item_4_title_link"
    )
    BOLT_T_SHIRT = (
        By.ID,
        "item_1_title_link"
    )
    ONESIE = (
        By.ID,
        "item_2_title_link"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_products(self):
        backpack = self.wait.until(
            EC.visibility_of_element_located(self.BACKPACK)
        )
        bolt_t_shirt = self.wait.until(
            EC.visibility_of_element_located(self.BOLT_T_SHIRT)
        )
        onesie = self.wait.until(
            EC.visibility_of_element_located(self.ONESIE)
        )

        return (
            backpack.text,
            bolt_t_shirt.text,
            onesie.text
        )

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
