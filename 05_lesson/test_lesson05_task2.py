from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    start_url = "https://httpbin.qa-territory.online/forms/post"

    driver.get(start_url)

    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Джансият")

    submit_button = driver.find_element(By.XPATH,
                                        "//button[text()='Submit order']"
                                        )

    submit_button.click()
    assert driver.current_url != start_url

    driver.quit()
