import os
import re
import subprocess
import time

from selenium import webdriver


def test_add_unpacked_extension():
    options = webdriver.ChromeOptions()

    # Укажите путь к директории вашего разархивированного расширения
    extension_dir_path = os.path.abspath("C:/Users/crm.28540/Desktop/USP_Plugin")

    options.add_argument(f"--load-extension={extension_dir_path}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://freelance.habr.com/")

    # Добавить время ожидания, чтобы увидеть результат
    time.sleep(10)  # Ждем 10 секунд

    # Закрыть браузер
    driver.quit()


if __name__ == "__main__":
    test_add_unpacked_extension()