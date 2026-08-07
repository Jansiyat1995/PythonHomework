from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()

    equal_button = driver.find_element(By.XPATH, "//span[text()='=']")
    driver.execute_script("arguments[0].click();", equal_button)

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"),
            "15"
        )
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

    driver.quit()
