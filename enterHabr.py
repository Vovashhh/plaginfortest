import os
import re
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_driver_utils import create_chrome_driver_with_extension, login_and_wait
import var


def test_add_unpacked_extension():
    options = webdriver.ChromeOptions()

    # Добавление плагина
    driver = create_chrome_driver_with_extension(var.pathToPlagin)
    driver.get(var.urlHabr)

    login_and_wait(driver)  # Вход под менеджером

    driver.quit()
