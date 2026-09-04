from selenium import webdriver

from pages.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        calculator_page = CalculatorPage(driver)

        calculator_page.open()
        calculator_page.set_delay("45")
        calculator_page.click_7()
        calculator_page.click_plus()
        calculator_page.click_8()
        calculator_page.click_equal()

        result = calculator_page.get_result()

        assert result == "15"
    finally:
        driver.quit()
