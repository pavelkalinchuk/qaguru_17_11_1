from selene import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_start():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
