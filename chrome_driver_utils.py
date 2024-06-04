import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def create_chrome_driver_with_extension(extension_dir_path):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--load-extension={os.path.abspath(extension_dir_path)}")
    driver = webdriver.Chrome(options=options)
    return driver


# Вынес команды для добавления плагина в отдельный файл

def login_and_wait(driver):
    # Находим кнопку "Вход" по тексту ссылки
    login_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Вход"))
    )
    login_button.click()

    # Ждем, пока кнопка "auto-enter-fixed" не станет кликабельной
    auto_enter_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "auto-enter-fixed"))
    )

    # Кликаем на кнопку "auto-enter-fixed"
    auto_enter_button.click()

    time.sleep(5)  # Ждем 5  секунд
