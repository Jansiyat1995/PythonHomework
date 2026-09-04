from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница медленного калькулятора."""

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUAL = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу калькулятора.

        Args:
            driver: WebDriver для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """Открывает страницу медленного калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: int) -> None:
        """Устанавливает задержку перед вычислением.

        Args:
            delay: Задержка в секундах.
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        element.clear()
        element.send_keys(delay)

    def click_7(self) -> None:
        """Нажимает кнопку с числом 7."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        ).click()

    def click_plus(self) -> None:
        """Нажимает кнопку сложения."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        ).click()

    def click_8(self) -> None:
        """Нажимает кнопку с числом 8."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        ).click()

    def click_equal(self) -> None:
        """Нажимает кнопку равно."""
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUAL)
        ).click()

    def get_result(self) -> str:
        """Возвращает результат вычисления.

        Returns:
            Результат вычисления в виде строки.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT,
                "15"
            )
        )
        return self.driver.find_element(*self.RESULT).text
