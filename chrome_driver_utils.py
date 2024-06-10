import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def chrome_with_extension(extension_dir_path):
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


def login_and_waitF(driver):
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.LinkElement[href='/login']"))
    )
    driver.execute_script("arguments[0].click();", login_button)

    time.sleep(5)
    # Клик по автовход
    auto_enter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "auto-enter-fixed"))
    )

    # Кликаем на кнопку "auto-enter-fixed"
    auto_enter_button.click()

    time.sleep(5)


def click_element(driver, selector_type, selector, wait_time=10):
    if selector_type == "ID":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, selector))
        )
    elif selector_type == "CSS_SELECTOR":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
    elif selector_type == "XPATH":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
    elif selector_type == "NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.NAME, selector))
        )
    elif selector_type == "CLASS_NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CLASS_NAME, selector))
        )
    else:
        raise ValueError("Unsupported selector type: " + selector_type)

    element.click()
    time.sleep(2)  # Ждем 2 секунды после клика


def enter_text(driver, selector_type, selector, text, wait_time=10):
    if selector_type == "ID":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, selector))
        )
    elif selector_type == "CSS_SELECTOR":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
    elif selector_type == "XPATH":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
    elif selector_type == "NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.NAME, selector))
        )
    elif selector_type == "CLASS_NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CLASS_NAME, selector))
        )
    else:
        raise ValueError("Unsupported selector type: " + selector_type)

    element.clear()
    element.send_keys(text)
    time.sleep(2)
