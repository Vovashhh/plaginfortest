import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from chrome_driver_utils import chrome_with_extension, login_and_wait, click_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import var

expected_text_login = "Найти задание/вакансию"
expected_unauthorized_text = "Вы не авторизованы, авторизируйтесь"


# Добавление плагина в браузер
def setup_driver():
    return chrome_with_extension(var.pathToPlagin)


# Переход на биржу, обновление и логин
def navigate_and_login(driver):
    driver.get(var.urlFreelance)
    driver.refresh()
    login_and_wait(driver)  # Вход под менеджером


# Проверка логина
def check():
    driver = setup_driver()
    navigate_and_login(driver)
    click_element(driver, "CSS_SELECTOR", var.alertBellBut)
    driver.quit()


if __name__ == "__main__":
    check()
