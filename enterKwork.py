import os
import re
import subprocess
import time
import var

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_driver_utils import create_chrome_driver_with_extension, login_and_wait

expected_text_login = "Мои заказы"  # Ожидаемый текст


def setup_driver():
    options = webdriver.ChromeOptions()
    return create_chrome_driver_with_extension(var.pathToPlagin)


def navigate_and_login(driver):
    driver.get(var.urlKwork)
    driver.refresh()
    login_and_wait(driver)  # Вход под менеджером


def сheck_login():
    with setup_driver() as driver:
        navigate_and_login(driver)

        # Проверка наличия элемента с ожидаемым текстом
        # Проверка наличия элемента с ожидаемым текстом
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[7]/div[3]/div/div[1]/div[2]/div[1]/div"),
                                             expected_text_login)
        )


def check_ball():
    with setup_driver() as driver:
        navigate_and_login(driver)

        notification_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='plugin-notification-button new']"))
        )
        notification_button.click()
        time.sleep(3)
        notification_button.click()

        time.sleep(5)


if __name__ == "__main__":
    сheck_login()
    check_ball()
