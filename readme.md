# Запуск проекта на Selenium с использованием Python

Этот проект демонстрирует пример запуска тестов с использованием Selenium и Python.

## Установка

1. Убедитесь, что у вас установлен Python и pip.
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

4. Установите Selenium и другие зависимости (если они необходимы) с помощью pip:

    ```sh
    pip install selenium
    ```
#### В файле var.py - можно задать переменные, в том числе для пути к плагину
   ### Для запуска нажать на Run в IDE 

___
1. Weblancer - блокер (капча)

---
#### Шаблон проверки с учетом логина
```sh
def name_check():
    with setup_driver() as driver:
        navigate_and_login(driver)
#Проверка 
```

#### Использование команды для ввода текста
<code>
    enter_text(driver, "ID", var.uspForm, "var.uspForm")
</code>

#### Использование команды для нажатия на селектор
<code>
    click_element(driver, "ID", var.uspModeration)
</code>