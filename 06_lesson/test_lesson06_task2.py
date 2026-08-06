from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # 1  пользователь
    driver.add_cookie({
        "name": "SESSION",
        "value": "NjBlYjIzOGUtNzNiMS00NDFkLTlkN2YtMjY4MjIxMGRmYjk5",
        "domain": "gitflic.ru"
    })

    #  Обновите страницу.
    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/jansiyat")

    # Сохраните текущий URL.
    user1_url = driver.current_url

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    # 2 пользователь
    driver.add_cookie({
        "name": "SESSION",
        "value": "MmI3YzI2ZmYtZDU3My00MzhhLWE5NDAtZDFhNmNmYzBhNmY2",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()
    WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/babatova")

    # Сохраните текущий URL.
    user2_url = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert user1_url != user2_url

    driver.quit()
