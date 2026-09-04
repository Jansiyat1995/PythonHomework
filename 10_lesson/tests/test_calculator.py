import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка сложения чисел 7 и 8 "
    "с предварительной установкой задержки 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """Проверяет сложение чисел 7 и 8 в калькуляторе."""

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        calculator_page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Нажать кнопку 7"):
            calculator_page.click_7()

        with allure.step("Нажать кнопку +"):
            calculator_page.click_plus()

        with allure.step("Нажать кнопку 8"):
            calculator_page.click_8()

        with allure.step("Нажать кнопку ="):
            calculator_page.click_equal()

        with allure.step("Проверить, что результат равен 15"):
            result = calculator_page.get_result()
            assert result == "15"

    finally:
        driver.quit()
