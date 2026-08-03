from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    start_url = "https://httpbin.qa-territory.online/"

    driver.get(start_url)
    driver.maximize_window()
    sleep(2)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    assert driver.current_url == start_url + "forms/post"

    driver.back()

    assert driver.current_url == start_url

    driver.quit()
