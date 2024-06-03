import os
import re
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_add_unpacked_extension():
    options = webdriver.ChromeOptions()

    # Укажите путь к директории вашего разархивированного расширения
    extension_dir_path = os.path.abspath("/Users/max/Downloads/USP_Plugin")

    options.add_argument(f"--load-extension={extension_dir_path}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://kwork.ru/")

    # Перезагрузить страницу
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


    # Добавить время ожидания, чтобы увидеть результат
    time.sleep(15)  # Ждем 10 секунд

    #Закрыть браузер
    driver.quit()

if __name__ == "__main__":
    test_add_unpacked_extension()