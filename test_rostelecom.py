from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

# Фикстура для инициализации и завершения WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://start.rt.ru/?tab=main")
    yield driver
    driver.quit()

# 1. Проверка успешной регистрации
def test_successful_registration(driver):
    driver.find_element(By.ID, "register").click()
    driver.find_element(By.ID, "name").send_keys("Иван Иванов")
    driver.find_element(By.ID, "email").send_keys("example@mail.com")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "confirm_password").send_keys("Password123")
    driver.find_element(By.ID, "submit_registration").click()
    assert "Регистрация прошла успешно" in driver.page_source

# 2. Проверка входа с правильными данными
def test_login_with_valid_data(driver):
    driver.find_element(By.ID, "login").click()
    driver.find_element(By.ID, "email").send_keys("example@mail.com")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit_login").click()
    assert "Вход выполнен успешно" in driver.page_source

# 3. Проверка входа с неправильными данными
def test_login_with_invalid_data(driver):
    driver.find_element(By.ID, "login").click()
    driver.find_element(By.ID, "email").send_keys("wrong@mail.com")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit_login").click()
    assert "Неверный логин или пароль" in driver.page_source

# 4. Проверка восстановления пароля
def test_password_recovery(driver):
    driver.find_element(By.ID, "forgot_password").click()
    driver.find_element(By.ID, "email").send_keys("example@mail.com")
    driver.find_element(By.ID, "submit_recovery").click()
    assert "Инструкции отправлены на почту" in driver.page_source

# 5. Проверка редактирования профиля
def test_edit_profile(driver):
    driver.find_element(By.ID, "profile").click()
    driver.find_element(By.ID, "edit_name").clear()
    driver.find_element(By.ID, "edit_name").send_keys("Иван Иванович")
    driver.find_element(By.ID, "save_changes").click()
    assert "Профиль обновлен" in driver.page_source

# 6. Проверка выхода из аккаунта
def test_logout(driver):
    driver.find_element(By.ID, "logout").click()
    assert "Вы вышли из аккаунта" in driver.page_source

# 7. Проверка переходов по сайту
def test_navigation_links(driver):
    driver.find_element(By.LINK_TEXT, "Главная").click()
    assert "Добро пожаловать" in driver.page_source

# 8. Проверка доступности информации о компании
def test_about_company_access(driver):
    driver.find_element(By.LINK_TEXT, "О нас").click()
    assert "Информация о компании" in driver.page_source

# 9. Проверка доступности формы обратной связи
def test_feedback_form(driver):
    driver.find_element(By.LINK_TEXT, "Контакты").click()
    driver.find_element(By.ID, "feedback_message").send_keys("Тестовое сообщение")
    driver.find_element(By.ID, "submit_feedback").click()
    assert "Спасибо за сообщение" in driver.page_source

# 10. Проверка фильтров в каталоге товаров
def test_product_catalog_filters(driver):
    driver.find_element(By.LINK_TEXT, "Каталог").click()
    driver.find_element(By.ID, "filter_category").click()
    assert "Товары по категории" in driver.page_source

# 11. Проверка добавления товаров в корзину
def test_add_to_cart(driver):
    driver.find_element(By.ID, "add_to_cart").click()
    assert "Товар добавлен в корзину" in driver.page_source

# 12. Проверка оформления заказа
def test_place_order(driver):
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "confirm_order").click()
    assert "Заказ оформлен" in driver.page_source

# 13. Проверка написания отзывов о товаре
def test_write_review(driver):
    driver.find_element(By.LINK_TEXT, "Товар").click()
    driver.find_element(By.ID, "review_message").send_keys("Отличный товар")
    driver.find_element(By.ID, "submit_review").click()
    assert "Спасибо за отзыв" in driver.page_source

# 14. Проверка работы системы рейтинга
def test_rating_system(driver):
    driver.find_element(By.LINK_TEXT, "Товар").click()
    driver.find_element(By.ID, "rate_5_stars").click()
    assert "Рейтинг сохранен" in driver.page_source

# 15. Проверка загрузки и удаления файлов
def test_file_upload(driver):
    driver.find_element(By.ID, "upload_file").send_keys("/path/to/test_file.txt")
    driver.find_element(By.ID, "delete_file").click()
    assert "Файл удален" in driver.page_source

# 16. Проверка рассылки новостей
def test_news_subscription(driver):
    driver.find_element(By.ID, "subscribe_news").click()
    assert "Вы подписаны на новости" in driver.page_source

# 17. Проверка условий использования и политики конфиденциальности
def test_privacy_policy_access(driver):
    driver.find_element(By.LINK_TEXT, "Политика конфиденциальности").click()
    assert "Политика конфиденциальности" in driver.page_source

# 18. Проверка страницы 404
def test_404_page(driver):
    driver.get("https://start.rt.ru/invalidpage")
    assert "Ошибка 404" in driver.page_source