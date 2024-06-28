from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_driver_utils import update_variable_in_var_file,  update_num_variable_in_var_file
import var

driver = webdriver.Chrome()

iKwork = var.i + 1
getUrlKwork = f'//div[{iKwork}]/div[1]/div[1]/h1/a'
getUrlHabr = f'//li[{iKwork}]/article/div/header/div[1]/a'
getUrlFreelance = f'//div[{iKwork}]/div[1]/div[1]/div/h2/a'
getUrlFreelancer = f'//*[@id="project-list"]/div[{iKwork}]/div/div[1]/div[1]/a'

try:
    # Откройте нужную страницу
    driver.get("https://kwork.ru/projects")

    # Найдите элемент по xPath и заберите ссылку
    elementKwork = driver.find_element(By.XPATH, getUrlKwork)
    urlKwork = elementKwork.get_attribute('href')
    textKwork = elementKwork.text
    print(f"Текст элемента Kwork: {textKwork}")
    print(f"Значение парсера: {iKwork}")

    # Обновите значение переменной urlKworkNew в файле var.py
    update_variable_in_var_file("urlKworkNew", urlKwork)
    update_variable_in_var_file("nameUrlKwork", textKwork)
    update_num_variable_in_var_file("i", filename="var.py")
#-----------------------------------------------------------------------
    # Откройте нужную страницу
    driver.get("https://freelance.ru/project/search/pro?c=")

    # Найдите элемент по xPath и заберите ссылку
    elementFreelance = driver.find_element(By.XPATH, getUrlFreelance)
    urlFreelance = elementFreelance.get_attribute('href')
    textFreelance = elementFreelance.text
    print(f"Текст элемента freelance: {textFreelance}")
    print(f"Значение парсера freelance: {iKwork}")

    # Обновите значение переменной urlKworkNew в файле var.py
    update_variable_in_var_file("urlFreelanceNew", urlFreelance)
    update_variable_in_var_file("nameUrlFreelance", textFreelance)

#-----------------------------------------------------------------------
    # Откройте нужную страницу
    driver.get(" https://www.freelancer.com/jobs")

    # Найдите элемент по xPath и заберите ссылку
    elementFreelancer = driver.find_element(By.XPATH, getUrlFreelancer)
    urlFreelancer = elementFreelancer.get_attribute('href')
    textFreelancer = elementFreelancer.text
    print(f"Текст элемента freelancer: {textFreelancer}")
    print(f"Значение парсера freelancer: {iKwork}")

    # Обновите значение переменной urlKworkNew в файле var.py
    update_variable_in_var_file("urlFreelancer", urlFreelancer)
    update_variable_in_var_file("textFreelancer", textFreelancer)
#-----------------------------------------------------------------------
    # Откройте нужную страницу
    driver.get("https://freelance.habr.com/tasks")

    # Найдите элемент по xPath и заберите ссылку
    elementhabr = driver.find_element(By.XPATH, getUrlHabr)
    urlHabr = elementhabr.get_attribute('href')
    textHabr = elementhabr.text
    print(f"Текст элемента freelance.habr: {textHabr}")
    print(f"Значение парсера freelance.habr: {iKwork}")

    # Обновите значение переменной freelance.habr в файле var.py
    update_variable_in_var_file("urlHabrNew", urlHabr)
    update_variable_in_var_file("nameUrlHabr", textHabr)



finally:
    driver.quit()
