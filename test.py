import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

global url
urlWeblancer = "https://www.weblancer.net/"

def test_add_unpacked_extension():
    options = webdriver.ChromeOptions()

    # Путь к плагину и его добавление
    extension_dir_path = os.path.abspath("C:/Users/crm.28540/Desktop/USP_Plugin")
    options.add_argument(f"--load-extension={extension_dir_path}")

    driver = webdriver.Chrome(options=options)
    driver.get(urlWeblancer)

    # Поиск и нажатие на "Вход"
    element1 = driver.find_element(By.LINK_TEXT, "Вход")
    element1.click()
    time.sleep(5)

    # Поиск и нажатие на елемент плагина "Автовход"
    button = driver.find_element(By.LINK_TEXT, "Автовход") #По тексту
    #button = driver.find_element(By.ID, "button-auth-extention") # по ID
    button.click()
    time.sleep(5)  # Ждем 10 секунд


    # Закрыть браузер
    driver.quit()


if __name__ == "__main__":
    test_add_unpacked_extension()