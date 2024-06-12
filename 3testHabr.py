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

def C3454_clicl_on_more():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        current_tab = driver.current_window_handle
        click_element(driver, "ID", var.dzenCirle)
        verify_text_in_element(driver, "CLASS_NAME", var.dzenAction, "Заявка зарегестрирована")
        click_element(driver, "CLASS_NAME", var.dzenHistMore)
        # Проверка что в новой вкладке открывается pm-dev.
        # Нет проверки что открывается именно заявка, так как нет логина в РМ
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        for tab in driver.window_handles:
            if tab != current_tab:
                driver.switch_to.window(tab)
                break
        assert "https://v2.pm-dev.dzencode.net" in driver.current_url
        print("Переход на новую вкладку pm-dev прошел успешно.")
    except NoSuchElementException as e:
        print(f"Test C3454 failed: {e}")
    finally:
        driver.quit()

def C3537_USP_send():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrRegMeSendUSP)
        verify_text_in_element(driver, "XPATH", var.sentUTP, "Вы отправили УТП")
        # тут добавить проверку в кружке дзена
    except NoSuchElementException as e:
        print(f"Test C3537 failed: {e}")
    finally:
        driver.quit()

def C3455_GPT_moderate_manager():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "CSS_SELECTOR", var.mainGPT)
        click_element(driver, "CLASS_NAME", var.getGPT)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, var.formGPT))
        )

        form_gpt_element = driver.find_element(By.CLASS_NAME, var.formGPT)
        form_gpt_text = form_gpt_element.text.strip()

        if len(form_gpt_text) > 5 and form_gpt_text != "—":
            print("Текст в элементе присутствует и содержит более 5 символов.")
        else:
            raise AssertionError("Текст в элементе отсутствует или содержит менее 5 символов.")

    except NoSuchElementException as e:
        print(f"Test C3455 failed: {e}")
    finally:
        driver.quit()

def C3460_whithout_deal():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "XPATH", var.dzenInfo)
        verify_text_in_element(driver, "XPATH", var.dzenInfoForm, "Сделка еще не создана")

    except NoSuchElementException as e:
        print(f"Test C3460 failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # try:
    #     C3446_dzen_cyrkle_only_with_register()
    # except Exception as e:
    #     print(f"Error running C3446: {e}")
    #
    # try:
    #     C3559_register_project_after_send_usp_moderate()
    # except Exception as e:
    #     print(f"Error running C3559: {e}")
    #
    # try:
    #     C3540_check_few_plugin_windows_open()
    # except Exception as e:
    #     print(f"Error running C3540: {e}")
    #
    # try:
    #     C3447_close_dzen_form()
    # except Exception as e:
    #     print(f"Error running C3447: {e}")
    #
    # try:
    #     C3448_plane_when_register_project()
    # except Exception as e:
    #     print(f"Error running C3448: {e}")
    #
    # try:
    #     C3454_clicl_on_more()
    # except Exception as e:
    #     print(f"Error running C3454: {e}")
    #
    # try:
    #     C3537_USP_send()
    # except Exception as e:
    #     print(f"Error running C3537: {e}")
    #
    # try:
    #     C3455_GPT_moderate_manager()
    # except Exception as e:
    #     print(f"Error running C3455: {e}")

    try:
        C3460_whithout_deal()
    except Exception as e:
        print(f"Error running C3460: {e}")


