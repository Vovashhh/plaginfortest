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


def сheck_login():
    options = webdriver.ChromeOptions()

    # Добавление плагина
    driver = create_chrome_driver_with_extension(var.pathToPlagin)
    driver.get(var.urlFreelancer)
    driver.refresh()

    # Кнопка Log In
    login_button = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.LinkElement[href='/login']"))
    )
    driver.execute_script("arguments[0].click();", login_button)

    time.sleep(5)
    # Клик по автовход
    auto_enter_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "auto-enter-fixed"))
    )

    # Кликаем на кнопку "auto-enter-fixed"
    auto_enter_button.click()

    time.sleep(5)

    driver.quit()


if __name__ == "__main__":
    сheck_login()
