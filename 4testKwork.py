import time
from selenium.common.exceptions import NoSuchElementException
from chrome_driver_utils import verify_element_not_present, verify_element_present, chrome_with_extension, \
    login_and_wait, click_element, enter_text, verify_text_in_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import var
import pyperclip
from colorama import Fore, Style


# Добавление плагина в браузер
def setup_driver():
    return chrome_with_extension(var.pathToPlagin)


# Переход на биржу, обновление и логин
def navigate_and_login(driver):
    driver.get(var.urlKwork)
    driver.get(var.urlKwork)
    login_and_wait(driver)  # Вход под менеджером


# Проверка логина
def C3446_dzen_cyrkle_only_with_register(driver):
    try:
        driver.get(var.urlKworkNew)
        verify_element_not_present(driver, "ID", var.dzenCirle)

        print(
            Fore.GREEN + "Кейс C3446 успешно выполнен. - Кружок dzenCode тображается только на зарегестрированном проэкте" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3446 failed: {e}")
    return driver


def C3559_register_project_after_send_usp_moderate(driver):
    try:
        driver.get(var.urlKworkNew)
        click_element(driver, "ID", var.uspModeration)
        enter_text(driver, "ID", var.uspForm, " Тест авто Владимир")
        click_element(driver, "CLASS_NAME", var.uspSend)
        verify_text_in_element(driver, "XPATH", var.regProjByMe, "Вы зарегистрировали проект")

        print(
            Fore.GREEN + "Кейс C3559 успешно выполнен. Проэкт зарегестрирован после отправки УТП на модерацию" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3559 failed: {e}")
    return driver


def C3540_check_few_plugin_windows_open(driver):
    try:
        driver.get(var.urlKworkNew)
        click_element(driver, "ID", var.dzenCirle)
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        verify_element_present(driver, "CLASS_NAME", var.bellForm)
        verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)

        print(Fore.GREEN + "Кейс C3540 успешно выполнен. - Можно открыть несколько окон" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3540 failed: {e}")
    return driver


def C3447_close_dzen_form(driver):
    try:
        driver.get(var.urlKworkNew)
        click_element(driver, "ID", var.dzenCirle)
        verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)
        click_element(driver, "ID", var.dzenCirle)
        verify_element_not_present(driver, "ID", var.dzenHistoryTab)

        print(Fore.GREEN + "Кейс C3447 успешно выполнен. - Можно закрыть форму dzenCode" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3447 failed: {e}")
    return driver


def C3448_plane_when_register_project(driver):
    try:
        driver.get(var.urlKworkNew)
        click_element(driver, "ID", var.dzenCirle)
        verify_text_in_element(driver, "CLASS_NAME", var.dzenAction, "Заявка зарегестрирована")

        print(
            Fore.GREEN + "Кейс C3448 успешно выполнен.- В истории отображается информация о регистрации проэкта" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3448 failed: {e}")
    return driver


def C3454_clicl_on_more(driver):
    try:
        driver.get(var.urlKworkNew)
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
        print(
            Fore.GREEN + "Кейс C3454 успешно выполнен. - При нажатии на подробнее, происходит переход в РМ" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3454 failed: {e}")
    return driver


def C3537_USP_send(driver):
    try:
        driver.get(var.urlKworkRegMeSendUSP)
        verify_text_in_element(driver, "XPATH", var.sentUTP, "Вы отправили УТП")
        # тут добавить проверку в кружке дзена

        print(Fore.GREEN + "Кейс C3537 успешно выполнен. - Отображается текст об отправке УТП" + Style.RESET_ALL)

    except NoSuchElementException as e:
        print(f"Test C3537 failed: {e}")
    return driver


def C3455_GPT_moderate_manager(driver):
    try:
        driver.get(var.urlKworkNew)
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
    return driver


def C3456_GPT_moderate_company(driver):
    try:
        driver.get(var.urlKworkNew)
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
    return driver


def C3459_copy_GPT(driver):
    try:
        driver.get(var.urlKworkNew)
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
    return driver


def C3460_whithout_deal(driver):
    try:
        driver.get(var.urlKworkNew)
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
        expected_dashboard_url = "https://kwork.ru/seller"
        actual_url = driver.current_url
        assert actual_url == expected_dashboard_url, (f"URL после автовхода не соответствует ожидаемому.")
        print(
            Fore.GREEN + "C3538 успешно выполнен - Пользователь может войти в аккаунт биржи нажав на кнопку 'Автовход'" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3538 failed: {e}")
    finally:
        driver.quit()


# Тест - Автовход по сессии
def C3539_auto_enter_session():
    driver = setup_driver()
    try:
        driver.get(var.urlKwork)
        driver.refresh()
        time.sleep(2)
        # Находим кнопку "Вход" по тексту ссылки
        login_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Вход"))
        )
        login_button.click()
        time.sleep(2)
        # Клик по автовходу по сессии
        click_element(driver, "XPATH", var.sessionLogin)
        time.sleep(5)
        expected_dashboard_url = "https://kwork.ru/seller"
        actual_url = driver.current_url
        assert actual_url == expected_dashboard_url, (f"URL после автовхода не соответствует ожидаемому.")
        print(
            Fore.GREEN + "C3539 успешно выполнен - Пользователь может войти в аккаунт биржи нажав на кнопку 'Автовход по сессии'" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3539 failed: {e}")
    finally:
        driver.quit()


# Тест - При нажатии на колокольчик открывается панель уведомлений
def C3482_notification_open(driver):
    try:
        driver.get(var.urlKwork)
        # Открытие колокольчика
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        # Проверка наличия панели уведомлений
        verify_element_present(driver, "CLASS_NAME", var.bellForm)
        # Закрытие колокольчик
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        print(
            Fore.GREEN + "C3482 успешно выполнен - При нажатии на колокольчик открывается панель уведомлений" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3482 failed: {e}")
    return driver


# Тест - Пользователь может посмотреть информацию о клиенте
def C3542_client(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "CLASS_NAME", var.clientIcon, "5")
        print(
            Fore.GREEN + "C3542 успешно выполнен - Пользователь может посмотреть информацию о клиенте" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3542 failed: {e}")
    return driver


# Тест - В информации о клиенте - отображается количество активных переписок
def C3568_client_act_mess(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.reqStestProgress)
        print(
            Fore.GREEN + "C3568 успешно выполнен - В информации о клиенте - отображается количество активных переписок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3568 failed: {e}")
    return driver


# Тест - В информации о клиенте - отображается количество успешных сделок
def C3569_client_comp(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.compByDeal)
        print(
            Fore.GREEN + "C3569 успешно выполнен - В информации о клиенте - отображается количество успешных сделок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3569 failed: {e}")
    return driver


# Тест - В информации о клиенте - отображается количество не успешных сделок
def C3570_client_close(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.closedReason)
        print(
            Fore.GREEN + "C3570 успешно выполнен - В информации о клиенте - отображается количество не успешных сделок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3570 failed: {e}")
    return driver


# Тест - Информация о клиенте скрыта для существующего клиента - если нет комментария
def C3566_info_hidden_without_comment(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "CLASS_NAME", var.clientIcon, "5")
        print(
            Fore.GREEN + "C3566 успешно выполнен - Информация о клиенте скрыта для существующего клиента - если нет комментария" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3573 failed: {e}")
    return driver


# Тест - Менеджер не может заполнить комментарий к заказчику пробелами
def C3586_client_comment_cannot_with_spaces(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "     ")
        # Проверяем что кнопка "Сохранить" задизейблена
        usp_send_button = driver.find_element(By.CLASS_NAME, var.saveClient)
        assert not usp_send_button.is_enabled(), "Кнопка 'Сохранить' должна быть неактивна"
        print(
            Fore.GREEN + "C3586 успешно выполнен - Менеджер не может заполнить комментарий к заказчику пробелами" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3586 failed: {e}")
    return driver


# Тест - Менеджер при нажатии на карандаш может добавить описание
def C3573_client_comment(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "Comment 1")
        click_element(driver, "CLASS_NAME", var.saveClient)
        # Проверяем что введенный текст отображается правильно
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "Comment 1", "Введенный текст не соответствует ожидаемому"
        print(
            Fore.GREEN + "C3573 успешно выполнен - Менеджер при нажатии на карандаш может добавить описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3573 failed: {e}")
    return driver


# Тест - Информация о клиенте раскрытая для существующего клиента - если есть комментарий
def C3567_info_disclosed_with_comment(driver):
    try:
        driver.get(var.urlKworkRegMe)
        verify_element_present(driver, "CLASS_NAME", var.clientIcon)
        print(
            Fore.GREEN + "C3567 успешно выполнен - Информация о клиенте раскрытая для существующего клиента - если есть комментарий" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3567 failed: {e}")
    return driver


# Тест - Менеджер может редактировать описание
def C3574_client_comment_redact(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "Comment Redact")
        click_element(driver, "CLASS_NAME", var.saveClient)
        # Проверяем что введенный текст отображается правильно
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "Comment Redact", "Введенный текст не соответствует ожидаемому"
        print(Fore.GREEN + "C3574 успешно выполнен - Менеджер может редактировать описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3574 failed: {e}")
    return driver


# Тест - Менеджер может удалить описание
def C3575_client_comment_del(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "1")
        enter_text(driver, "ID", var.commentForm, "")
        click_element(driver, "CLASS_NAME", var.saveClient)
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "", "Текст в поле для ввода не был удален"
        print(Fore.GREEN + "C3575 успешно выполнен - Менеджер может удалить описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3575 failed: {e}")
    return driver


# Тест - При нажатии на глазик открывается форма отправки УТП для проверки дежурному
def C3466_usp_Moderation(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.uspModeration)
        # Поиск формы для отправки УТП
        verify_element_present(driver, "ID", var.uspForm)
        enter_text(driver, "ID", var.uspForm, "УТП на проверку")
        click_element(driver, "CLASS_NAME", var.uspSend)
        print(
            Fore.GREEN + "C3466 успешно выполнен - При нажатии на глазик открывается форма отправки УТП для проверки дежурному" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3466 failed: {e}")
    return driver


# Тест - Кнопка "Отправить" задизейбленна пока не введутся символы в форму
def C3467_usp_Moderation_btn(driver):
    try:
        driver.get(var.urlKworkRegMe)
        click_element(driver, "ID", var.uspModeration)
        usp_send_button = driver.find_element(By.CLASS_NAME, var.uspSend)
        assert not usp_send_button.is_enabled(), "Кнопка отправки должна быть неактивна"
        enter_text(driver, "ID", var.uspForm, "Тест УТП на модерацию")
        click_element(driver, "CLASS_NAME", var.uspSend)
        print(
            Fore.GREEN + "C3467 успешно выполнен - Кнопка 'Отправить' задизейбленна пока не введутся символы в форму" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3467 failed: {e}")
    return driver


# Тест - После отправки УТП глазик пропадает, становится недоступным
def C3469_usp_not_available(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)  # Пауза чтобы закрыть уведомление
        verify_element_not_present(driver, "ID", var.uspModeration)
        print(
            Fore.GREEN + "C3469 успешно выполнен - После отправки УТП глазик пропадает, становится недоступным" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3469 failed: {e}")
    return driver


# Тест - Когда кнопка сообщения обведена красным кругом - есть не прочитанное сообщение от клиента
def C3470_mess_btn_red(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)  # Пауза чтобы закрыть уведомление
        button = driver.find_element(By.ID, var.messegeBtn)
        style = button.get_attribute("style")
        assert "border-color: red" in style, "Кнопка не обведена красным кругом"
        print(
            Fore.GREEN + "C3470 успешно выполнен - Когда кнопка сообщения обведена красным кругом - есть не прочитанное сообщение от клиента" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3470 failed: {e}")
    return driver


# Тест - Палец вверх отображается в чате с клиентом, для отметки что сообщение не требует ответа
def C3476_message_thumb_up(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        driver.switch_to.window(driver.window_handles[-1])
        # Находим елемент "Палец вверх"
        verify_element_present(driver, "ID", var.msgThumbUp)
        # Нажимаем на палец вверх
        click_element(driver, "ID", "btn-message-without-answer")
        print(
            Fore.GREEN + "C3476 успешно выполнен - Палец вверх отображается в чате с клиентом, для отметки что сообщение не требует ответа" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3476 failed: {e}")
    return driver


# Тест - Когда кнопка сообщения обведена зеленым - на все сообщения есть ответ , при клике по ней - переход в переписку по проекту
def C3472_mess_btn_green(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)  # Пауза чтобы закрыть уведомление
        button = driver.find_element(By.ID, var.messegeBtn)
        style = button.get_attribute("style")
        assert "border-color: green" in style, "Кнопка не обведена зеленым кругом"
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        assert "inbox" in driver.current_url, "URL не содержит текст 'inbox'"
        print(
            Fore.GREEN + "C3470 успешно выполнен - Когда кнопка сообщения обведена зеленым - на все сообщения есть ответ, при клике по ней - переход в переписку по проекту" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3470 failed: {e}")
    return driver


# Тест - При нажатии на карандаш, открывается форма модерации сообщения
def C3473_message_moderation_form(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        verify_element_present(driver, "ID", var.msgForm)
        print(
            Fore.GREEN + "C3473 успешно выполнен - При нажатии на карандаш, открывается форма модерации сообщения" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3473 failed: {e}")
    return driver


# Тест - Кнопка "Отправить" задизейбленна пока не заполнена форма карандаша для отправки дежурному
def C3474_message_moderation_btn(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        # Проверяем что кнопка "Отправить" задизейблена
        usp_send_button = driver.find_element(By.CLASS_NAME, var.msgSendModerate)
        assert not usp_send_button.is_enabled(), "Кнопка отправки должна быть неактивна"
        enter_text(driver, "ID", var.msgForm, "Текст сообщения для проверки дежурному")
        # Проверяем что кнопка "Отправить" активна
        assert usp_send_button.is_enabled(), "Кнопка отправки должна быть активна"
        print(
            Fore.GREEN + "C3474 успешно выполнен - Кнопка 'Отправить' задизейбленна пока не заполнена форма карандаша для отправки дежурному" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3474 failed: {e}")
    return driver


# Тест - При отправке сообщения на модерацию оно приходит дежурному менеджеру
def C3475_message_moderation_send(driver):
    try:
        driver.get(var.urlKworkRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        enter_text(driver, "ID", var.msgForm, "Текст сообщения для проверки дежурному")
        click_element(driver, "CLASS_NAME", var.msgSendModerate)
        print(
            Fore.GREEN + "C3475 успешно выполнен - При отправке сообщения на модерацию оно приходит дежурному менеджеру" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3475 failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    driver = None
    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3446_dzen_cyrkle_only_with_register(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3446: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3559_register_project_after_send_usp_moderate(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3559: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3540_check_few_plugin_windows_open(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3540: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3447_close_dzen_form(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3447: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3448_plane_when_register_project(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3448: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3454_clicl_on_more(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3454: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3537_USP_send(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3537: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3455_GPT_moderate_manager(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3455: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3456_GPT_moderate_company(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3456: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3459_copy_GPT(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3459: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3460_whithout_deal(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3460: {e}" + Style.RESET_ALL)
    driver = None
    try:
        C3538_auto_enter()
    except Exception as e:
        print(Fore.RED + f"Error running C3538: {e}" + Style.RESET_ALL)

    try:
        C3539_auto_enter_session()
    except Exception as e:
        print(Fore.RED + f"Error running C3539: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3482_notification_open(driver)
    except Exception as e:
        print(Fore.RED + "Error running C3482: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3542_client(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3542: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3568_client_act_mess(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3568: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3569_client_comp(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3569: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3570_client_close(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3570: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3566_info_hidden_without_comment(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3566 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3586_client_comment_cannot_with_spaces(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3586 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3573_client_comment(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3573: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3567_info_disclosed_with_comment(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3567 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3574_client_comment_redact(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3574: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3575_client_comment_del(driver)
    except Exception as e:
        print(Fore.RED + f"Error running C3575: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3466_usp_Moderation(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3466 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3467_usp_Moderation_btn(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3467 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3469_usp_not_available(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3469 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3470_mess_btn_red(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3470 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3476_message_thumb_up(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3476 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3472_mess_btn_green(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3472 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3473_message_moderation_form(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3473 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3474_message_moderation_btn(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3474 failed: {e}" + Style.RESET_ALL)

    try:
        if driver is None:
            driver = setup_driver()
            navigate_and_login(driver)
        C3475_message_moderation_send(driver)
    except Exception as e:
        print(Fore.RED + f"Test C3475 failed: {e}" + Style.RESET_ALL)
