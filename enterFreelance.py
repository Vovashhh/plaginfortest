import time

from selenium.common import NoSuchElementException

import var
from selenium import webdriver
from chrome_driver_utils import create_chrome_driver_with_extension, login_and_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_text_login = "Найти задание/вакансию"
expected_unauthorized_text = "Вы не авторизованы, авторизируйтесь"


# Добавление плагина в браузер
def setup_driver():
    options = webdriver.ChromeOptions()
    return create_chrome_driver_with_extension(var.pathToPlagin)


# Переход на биржу, обновление и логин
def navigate_and_login(driver):
    driver.get(var.urlFreelance)
    driver.refresh()
    login_and_wait(driver)  # Вход под менеджером


# Проверка логина
def сheck_login():
    with setup_driver() as driver:
        navigate_and_login(driver)

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h2[1]"), expected_text_login)
        )


def check_ball():
    with setup_driver() as driver:
        navigate_and_login(driver)

        notification_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='plugin-notification-button new']"))
        )
        notification_button.click()

        time.sleep(5)


if __name__ == "__main__":
    сheck_login()
    check_ball()
