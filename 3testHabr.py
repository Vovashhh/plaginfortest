import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from chrome_driver_utils import verify_element_not_present, verify_element_present, chrome_with_extension, \
    login_and_wait, click_element, enter_text, verify_text_in_element
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
    driver.get(var.urlHabr)
    driver.refresh()
    login_and_wait(driver)  # Вход под менеджером


# Проверка логина
def C3559_register_project_after_send_usp_moderate():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.uspModeration)
        enter_text(driver, "ID", var.uspForm, " Тест авто Владимир")
        click_element(driver, "CLASS_NAME", var.uspSend)
        verify_text_in_element(driver, "XPATH", var.regProjByMe, "Вы зарегистрировали проект")
    except NoSuchElementException as e:
        print(f"Test C3559 failed: {e}")
    finally:
        driver.quit()


def C3540_check_few_plugin_windows_open():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        verify_element_present(driver, "CLASS_NAME", var.bellForm)
        verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)
    except NoSuchElementException as e:
        print(f"Test C3540 failed: {e}")
    finally:
        driver.quit()


def C3446_dzen_cyrkle_only_with_register():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        verify_element_not_present(driver, "ID", var.dzenCirle)
    except NoSuchElementException as e:
        print(f"Test C3446 failed: {e}")
    finally:
        driver.quit()


def C3447_close_dzen_form():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)
        click_element(driver, "ID", var.dzenCirle)
        verify_element_not_present(driver, "ID", var.dzenHistoryTab)
    except NoSuchElementException as e:
        print(f"Test C3447 failed: {e}")
    finally:
        driver.quit()


def C3448_plane_when_register_project():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        verify_text_in_element(driver, "CLASS_NAME", var.dzenAction, "Заявка зарегестрирована")
    except NoSuchElementException as e:
        print(f"Test C3448 failed: {e}")
    finally:
        driver.quit()


def C3449_messege_from_client():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        # Дополнить тест
    except NoSuchElementException as e:
        print(f"Test C3449 failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        C3446_dzen_cyrkle_only_with_register()
    except Exception as e:
        print(f"Error running C3446: {e}")

    try:
        C3559_register_project_after_send_usp_moderate()
    except Exception as e:
        print(f"Error running C3559: {e}")

    try:
        C3540_check_few_plugin_windows_open()
    except Exception as e:
        print(f"Error running C3540: {e}")

    try:
        C3447_close_dzen_form()
    except Exception as e:
        print(f"Error running C3447: {e}")

    try:
        C3448_plane_when_register_project()
    except Exception as e:
        print(f"Error running C3448: {e}")

    try:
        C3449_messege_from_client()
    except Exception as e:
        print(f"Error running C3449: {e}")
