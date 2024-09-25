# Kinopoisk-Test-NP
Дипломная работа. Архитектура фреймворка

- Для запуска только UI-тестов:

bash
pytest tests/test_ui.py --alluredir=reports/


- Для запуска только API-тестов:

bash
pytest tests/test_api.py --alluredir=reports/


- Для запуска всех тестов:

bash
pytest tests/ --alluredir=reports/


- Чтобы сгенерировать отчет Allure после выполнения тестов, выполните:

bash
allure serve reports/