import os
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def update_num_variable_in_var_file(variable_name, filename="var.py", encoding='utf-8'):
    # Прочитайте содержимое файла с указанием кодировки
    with open(filename, "r", encoding=encoding) as file:
        lines = file.readlines()

    # Найдите строку с указанной переменной и замените её значение
    for i in range(len(lines)):
        if lines[i].startswith(variable_name):
            # Извлечение текущего значения переменной
            current_value = int(lines[i].split('=')[1].strip())
            # Проверка значения переменной и обновление
            if current_value < 11:
                new_value = current_value + 1
            else:
                new_value = 0
            lines[i] = f"{variable_name} = {new_value}\n"
            break

    # Запишите измененное содержимое обратно в файл с указанием кодировки
    with open(filename, "w", encoding=encoding) as file:
        file.writelines(lines)

    # Запишите измененное содержимое обратно в файл с указанием кодировки
    with open(filename, "w", encoding=encoding) as file:
        file.writelines(lines)

def update_variable_in_var_file(variable_name, new_value, filename="var.py", encoding='utf-8'):
    # Прочитайте содержимое файла с указанием кодировки
    with open(filename, "r", encoding=encoding) as file:
        lines = file.readlines()

    # Найдите строку с указанной переменной и замените её значение
    for i in range(len(lines)):
        if lines[i].startswith(variable_name):
            lines[i] = f"{variable_name} = '{new_value}'\n"
            break

    # Запишите измененное содержимое обратно в файл с указанием кодировки
    with open(filename, "w", encoding=encoding) as file:
        file.writelines(lines)

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

def login_and_wait_via_session_forFreelance(driver):
    try:
        # Пробуем войти через автовход по сессии
        login_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Вход"))
        )
        login_button.click()
        time.sleep(2)
        # Клик по автовходу по сессии
        login_button_sess = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Автовход по сессии')]"))
        )
        login_button_sess.click()
        time.sleep(5)
    except (NoSuchElementException, TimeoutException):
        # Если не получилось, пробуем обычный автовход
        try:
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
            time.sleep(5)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Login via session failed: {e}")


def click_element(driver, selector_type, selector, wait_time=3):
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


def enter_text(driver, selector_type, selector, text, wait_time=3):
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


def verify_text_in_element(driver, selector_type, selector, expected_text_part, wait_time=3):
    if selector_type == "ID":
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, selector))
        )
    elif selector_type == "CSS_SELECTOR":
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
    elif selector_type == "XPATH":
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
    elif selector_type == "NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.NAME, selector))
        )
    elif selector_type == "CLASS_NAME":
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, selector))
        )
    else:
        raise ValueError("Unsupported selector type: " + selector_type)

    time.sleep(3)  # Задержка в 3 секунды
    actual_text = element.text
    if expected_text_part in actual_text:
        print(f"Текст '{expected_text_part}' Пристутсвует в указанном элементе.")
    else:
        raise AssertionError(
            f"Partial text '{expected_text_part}' not found in the element. Actual text: '{actual_text}'")


def verify_element_present(driver, selector_type, selector, wait_time=3):
    try:
        if selector_type == "ID":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, selector))
            )
        elif selector_type == "CSS_SELECTOR":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        elif selector_type == "XPATH":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
        elif selector_type == "NAME":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, selector))
            )
        elif selector_type == "CLASS_NAME":
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, selector))
            )
        else:
            raise ValueError("Unsupported selector type: " + selector_type)

        print(f"Элемент {selector_type}='{selector}' Отображается на странице.")
    except:
        raise AssertionError(f"Элемента {selector_type}='{selector}' нет на странице.")

def verify_element_not_present(driver, selector_type, selector, wait_time=3):
    try:
        if selector_type == "ID":
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located((By.ID, selector))
            )
        elif selector_type == "CSS_SELECTOR":
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, selector))
            )
        elif selector_type == "XPATH":
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located((By.XPATH, selector))
            )
        elif selector_type == "NAME":
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located((By.NAME, selector))
            )
        elif selector_type == "CLASS_NAME":
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, selector))
            )
        else:
            raise ValueError("Unsupported selector type: " + selector_type)

        print(f"Элемент {selector_type}='{selector}' отсутсвует.")
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise AssertionError(f"Элемент {selector_type}='{selector}' присутвует на странице.")