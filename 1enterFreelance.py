import time
from selenium.common.exceptions import NoSuchElementException
import var
from selenium import webdriver
from chrome_driver_utils import create_chrome_driver_with_extension, login_and_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_text_login = "Найти задание/вакансию"
expected_unauthorized_text = "Вы не авторизованы, авторизируйтесь"


# Добавление плагина в браузер
def setup_driver():
    options = webdriver.ChromeOptions()
    return create_chrome_driver_with_extension(var.pathToPlagin)


# Переход на биржу, обновление и логин
def navigate_and_login(driver):
    driver.get(var.urlFreelance)
    driver.refresh()
    login_and_wait(driver)  # Вход под менеджером


# Проверка логина
def check_login():
    try:
        with setup_driver() as driver:
            navigate_and_login(driver)
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "//h2[1]"), expected_text_login)
            )
            print("check_login test passed")
    except NoSuchElementException:
        print("check_login test failed")
    except Exception as e:
        print(f"check_login test failed with error: {e}")


def check_ball():
    try:
        with setup_driver() as driver:
            navigate_and_login(driver)

            notification_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='plugin-notification-button new']"))
            )
            notification_button.click()
            time.sleep(5)
            print("check_ball test passed")
    except NoSuchElementException:
        print("check_ball test failed")
    except Exception as e:
        print(f"check_ball test failed with error: {e}")

def redLine_unautoraize():
    try:
        with setup_driver() as driver:
            options = webdriver.ChromeOptions()
            # Добавление плагина
            driver = create_chrome_driver_with_extension(var.pathToPlagin)
            driver.get("https://freelance.ru/")
            driver.refresh()
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]"), expected_unauthorized_text)
            )
            print("redLine_unauthorize test passed")
    except NoSuchElementException:
        print("redLine_unauthorize test failed")
    except Exception as e:
        print(f"redLine_unauthorize test failed with error: {e}")


if __name__ == "__main__":
    check_login()
    check_ball()
    redLine_unautoraize()
