from selene import browser
import pytest
from selenium import webdriver
from allure_attach import *


@pytest.fixture(scope="session", autouse=True)
def browser_start():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://demoqa.com/automation-practice-form')
    # selenoid_capabilities = {
    #     "browserName": "chrome",  # тип браузера
    #     "browserVersion": "100.0",  # версия браузера
    #     "selenoid:options": {  # установка разрешения на запись видео во время теста
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # driver_options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=driver_options)
    #
    # browser = Browser(Config(driver))

    yield browser

    # прикрепляем скриншоты, логи браузера, html-код страницы, видеозапись теста
    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
