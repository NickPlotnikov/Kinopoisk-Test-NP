import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from config.settings import BASE_URL
from time import sleep

@allure.feature('UI Tests')
class TestUI:

    @allure.story('Opening the main page')
    def test_open_main_page(self):
        driver = webdriver.Chrome()  # Или используйте другой драйвер
        driver.get(BASE_URL)
        assert "КиноПоиск" in driver.title
        driver.quit()

    @allure.story('Search for a movie')
    def test_search_movie(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        search_box = driver.find_element(By.NAME, "text")
        search_box.send_keys("Тест")  # Используйте данные из test_data.py при необходимости
        search_box.submit()
        assert "Тест" in driver.title
        driver.quit()

    @allure.story('Check movie details page')
    def test_movie_details(self):
        driver = webdriver.Chrome()
        driver.get(f"{BASE_URL}/film/{MOVIE_ID}/")  # Замените на реальный ID
        assert "Тест" in driver.page_source  # Проверьте наличие контента
        driver.quit()

    @allure.story('Check user login functionality')
    def test_login_functionality(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        # Настройка куки для токена авторизации
        driver.add_cookie({"name": "auth_token", "value": TOKEN})
        driver.refresh()
        assert "Войти" not in driver.page_source  # Проверка, что кнопка "Войти" отсутствует
        driver.quit()

    @allure.story('Check footer links')
    def test_footer_links(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        footer_links = driver.find_elements(By.CSS_SELECTOR, "footer a")
        assert len(footer_links) > 0  # Проверяем, что есть ссылки в подвале
        driver.quit()