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
    driver.get("https://www.weblancer.net/")

    # Перезагрузить страницу
    driver.refresh()




    # Добавить время ожидания, чтобы увидеть результат
    time.sleep(15)  # Ждем 10 секунд

    #Закрыть браузер
    driver.quit()

if __name__ == "__main__":
    test_add_unpacked_extension()