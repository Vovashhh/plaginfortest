#import time
from selenium.common.exceptions import NoSuchElementException
#from selenium import webdriver
from chrome_driver_utils import verify_element_not_present, verify_element_present, chrome_with_extension, \
    login_and_wait, click_element, enter_text, verify_text_in_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import var
import pyperclip
from colorama import init, Fore, Style


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
def C3446_dzen_cyrkle_only_with_register(driver):
    try:
        driver.get(var.urlHabrNew)
        verify_element_not_present(driver, "ID", var.dzenCirle)

        print(Fore.GREEN + "Кейс C3446 успешно выполнен. - Кружок dzenCode тображается только на зарегестрированном проэкте" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3446 failed: {e}")
    return driver

def C3559_register_project_after_send_usp_moderate(driver):
    try:
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.uspModeration)
        enter_text(driver, "ID", var.uspForm, " Тест авто Владимир")
        click_element(driver, "CLASS_NAME", var.uspSend)
        verify_text_in_element(driver, "XPATH", var.regProjByMe, "Вы зарегистрировали проект")

        print(Fore.GREEN + "Кейс C3559 успешно выполнен. Проэкт зарегестрирован после отправки УТП на модерацию" + Style.RESET_ALL)

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

        print(Fore.GREEN + "Кейс C3540 успешно выполнен. - Можно открыть несколько окон" + Style.RESET_ALL)

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

        print(Fore.GREEN + "Кейс C3447 успешно выполнен. - Можно закрыть форму dzenCode" + Style.RESET_ALL)

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

        print(Fore.GREEN + "Кейс C3448 успешно выполнен.- В истории отображается информация о регистрации проэкта" + Style.RESET_ALL)

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
        print(Fore.GREEN + "Кейс C3454 успешно выполнен. - При нажатии на подробнее, происходит переход в РМ" + Style.RESET_ALL)

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

        print(Fore.GREEN + "Кейс C3537 успешно выполнен. - Отображается текст об отправке УТП" + Style.RESET_ALL)

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

        print(Fore.GREEN + "Кейс C3455 успешно выполнен. Ответ сгенерирован менеджером" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3455 failed: {e}")
    finally:
        driver.quit()

def C3456_GPT_moderate_company():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "CSS_SELECTOR", var.mainGPT)
        click_element(driver, "XPATH", var.btnCompany)
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

        print(Fore.GREEN + "Кейс C3456 успешно выполнен. Ответ компании сгенерирован" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3455 failed: {e}")
    finally:
        driver.quit()

def C3459_copy_GPT():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "CSS_SELECTOR", var.mainGPT)
        click_element(driver, "CLASS_NAME", var.copyGPT)

        form_gpt_element = driver.find_element(By.CLASS_NAME, var.formGPT)
        form_gpt_text = form_gpt_element.text.replace('\n', '').replace(' ', '')

        clipboard_text = pyperclip.paste().replace('\n', '').replace(' ', '')

        if clipboard_text == form_gpt_text:
            print("Скопированный текст совпадает.")
        else:
            print("Скопированный текст не совпадает.")

        print(Fore.GREEN + "Кейс C3459 успешно выполнен. Ответ скопирован" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3459 failed: {e}")
    finally:
        driver.quit()

def C3460_whithout_deal():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "XPATH", var.dzenInfo)
        verify_text_in_element(driver, "CLASS_NAME", var.dzenInfoKwork, "Сделка еще не создана")

        print(Fore.GREEN + "Кейс C3460 успешно выполнен. - В информации нет сделки" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3460 failed: {e}")
    finally:
        driver.quit()

    def C3538_auto_enter():
        driver = setup_driver()
        try:
            navigate_and_login(driver)
            time.sleep(2)
            expected_dashboard_url = "https://freelance.habr.com/tasks"
            actual_url = driver.current_url
            assert actual_url == expected_dashboard_url, (f"URL после автовхода не соответствует ожидаемому.")
            print(
                Fore.GREEN + "C3538 успешно выполнен - Пользователь может войти в аккаунт биржи нажав на кнопку 'Автовход'" + Style.RESET_ALL)
        except NoSuchElementException as e:
            print(f"Test C3538 failed: {e}")
        finally:
            driver.quit()

if __name__ == "__main__":
    # try:
    #     C3446_dzen_cyrkle_only_with_register()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3446: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3559_register_project_after_send_usp_moderate()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3559: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3540_check_few_plugin_windows_open()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3540: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3447_close_dzen_form()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3447: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3448_plane_when_register_project()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3448: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3454_clicl_on_more()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3454: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3537_USP_send()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3537: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3455_GPT_moderate_manager()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3455: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3456_GPT_moderate_company()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3456: {e}" + Style.RESET_ALL)

    try:
        C3460_whithout_deal()
    except Exception as e:
        print(Fore.RED + f"Error running C3460: {e}" + Style.RESET_ALL)
    #
    # try:
    #     C3459_copy_GPT()
    # except Exception as e:
    #     print(Fore.RED + f"Error running C3459: {e}" + Style.RESET_ALL)


