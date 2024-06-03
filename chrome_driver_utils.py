import os
from selenium import webdriver

def create_chrome_driver_with_extension(extension_dir_path):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--load-extension={os.path.abspath(extension_dir_path)}")
    driver = webdriver.Chrome(options=options)
    return driver

# Вынес команды для добавления плагина в отдельный файл