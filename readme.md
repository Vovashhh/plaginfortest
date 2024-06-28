# Автоматическое тестирование плагина ГГ с помощью Selenium и Python

Автоматические тесты для тестирования плагина ГГ.

## Содержание

1. [Описание](#описание)
2. [Установка](#установка)
3. [Конфигурация](#конфигурация)
4. [Запуск тестов](#запуск-тестов)
5. [Примеры кода](#примеры-кода)

## Описание

Список покрытых тестов можно посмотреть
в [таблице статусов автотестов](https://docs.google.com/spreadsheets/d/1qqlhKPdRqQpEVlrwVBCH4_zuKuKWV_pKTApflPJbY-U/edit?gid=0#gid=0).

В [TestRail](https://qa.dzencode.net/index.php?/suites/view/1&group_by=cases:section_id&group_order=desc&display_deleted_cases=0&group_id=1111)
можно просмотреть какие тесты автоматизированы, выбрав фильтр `Automation Type - renorex`. Для просмотра не
автоматизированных тестов, в фильтре можно выбрать `none`.

## Установка

1. Убедитесь, что у вас установлен Python, pip, а также Selenium.
2. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/Vovashhh/plaginfortest.git
    ```

3. Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # для Linux/Mac
    .venv\Scripts\activate      # для Windows
    ```

4. Установите зависимости с помощью pip:

    ```sh
    pip install selenium pyperclip colorama
    ```

## Конфигурация

В файле `var.py` можно задать переменные, в том числе для пути к плагину.

Для корректной работы автотестов нужно после каждого прогона добавлять актуальную новую заявку в
переменные `urlHabrNew`, `urlKworkNew`, `urlFreelanceNew`, `urlFreelancerNew`.

Так же по заявкам в переменных [биржа]RegNotMeSendUSP - нужно отправить сообщение от имени клиента - для успешного прохождения кейсов

Для биржи Habr периодически нужно прерывать загрузку страницы из-за вечного лоудера.
<br>
В файле [chrome_driver_utils.py](https://git.dzencode.com/qa/ext/-/blob/main/chrome_driver_utils.py) - содержатся кастомные команды

## Запуск тестов

Запуск тестов осуществляется в IDE, нажав кнопку "Run". Результат прохождения тестов будет отображаться в Run-е в
формате:

- Зеленый - тест успешно пройдет
- Красный - тест провален

Также отображается дополнительная информация и номер кейса с TestRail.

### Пример запуска тестов:

![Image](https://img001.prntscr.com/file/img001/qiW1SLJnQneL7qiop2TtBw.png)

---

## Примеры кода

### Шаблон проверки с учетом логина

```sh
def name_check():
driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        #тут проверка
    except NoSuchElementException as e:
        print(f"Test № failed: {e}")
    finally:
        driver.quit()
#Проверка 
```

### Конструкция для запуска тестов в случае их провала

```sh 
if __name__ == "__main__":
    try:
        C3446_dzen_cyrkle_only_with_register()
    except Exception as e:
        print(f"Error running C3446: {e}")
```

### Конструкция для запуска тестов без постоянной логинизации

```sh
def C3467_usp_Moderation_btn(driver):
    try:
        # Проверка
    except NoSuchElementException as e:
        # Исключение
    return driver
```

```sh
if __name__ == "__main__":
    driver = None
    try:
        if driver is None:
            driver = setup_driver() #Если driver не был найден то выполняется логинизация
            navigate_and_login(driver)
        C3467_usp_Moderation_btn(driver)
    except Exception as e:
        print(Fore.RED + "Error running C3467: {e}" + Style.RESET_ALL)
```

#### Использование команды для ввода текста

<code>
    enter_text(driver, "ID", var.uspForm, "var.uspForm")
</code>

#### Использование команды для нажатия на селектор

<code>
    click_element(driver, "ID", var.uspModeration)
</code>

#### Использование команды для проверки формы на соответсвие

<code>
    verify_text_in_element(driver, "XPATH", var.regProjByMe, "Тут текст")
</code>

#### Использование команды для проверки что элемент пристутсвует на странице

<code>
      verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)
</code>

#### Использование команды для проверки что элемент отсутсвует на странице

<code>
      verify_element_not_present(driver, "ID", var.uspModeration)
</code>

#### Использование команды для подмены переменной ссылки в var с помощью parser.py
<code>
    update_variable_in_var_file("urlKworkNew", url)
</code>

#### Команда для изменения каунтера i
<code>
      update_num_variable_in_var_file("i", filename="var.py")
</code>
