from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_driver_utils import update_variable_in_var_file

driver = webdriver.Chrome()

bXpathKwork = '//div['
eXpathKwork = ']/div[1]/div[1]/h1/a'
iKwork = 1
current_xpath = bXpathKwork + str(iKwork) + eXpathKwork

try:
    # Откройте нужную страницу
    driver.get("https://kwork.ru/projects")

    # Найдите элемент по xPath и заберите ссылку
    element = driver.find_element(By.XPATH, current_xpath)
    url = element.get_attribute('href')

    # Обновите значение переменной urlKworkNew в файле var.py
    update_variable_in_var_file("urlKworkNew", url)

finally:
    driver.quit()
