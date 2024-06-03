import os
import re
import subprocess
import time
import var


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_driver_utils import create_chrome_driver_with_extension




def test_add_unpacked_extension():
    options = webdriver.ChromeOptions()

    # Добавление плагина
    driver = create_chrome_driver_with_extension(var.pathToPlagin)

    driver.get(var.urlKwork)
    driver.refresh()

    # Находим кнопку "Вход" по тексту ссылки
    login_button = driver.find_element(By.LINK_TEXT, "Вход")
    login_button.click()

    # Ждем, пока кнопка "auto-enter-fixed" не станет кликабельной
    auto_enter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "auto-enter-fixed"))
    )

    # Кликаем на кнопку "auto-enter-fixed"
    auto_enter_button.click()

    time.sleep(15)  # Ждем 15 секунд

    #Закрыть браузер
    driver.quit()

if __name__ == "__main__":
    test_add_unpacked_extension()