from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        element.send_keys(last_name)

    def enter_zip_code(self, zip_code):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ZIP_CODE)
        )
        element.send_keys(zip_code)

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def fill_form(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.continue_checkout()

    def get_total(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return element.text
