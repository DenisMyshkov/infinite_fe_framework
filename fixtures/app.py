import pytest
from selenium import webdriver
from application.application import Application


@pytest.fixture(scope="session")
def app() -> None:
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.set_window_position(0, 0)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(20)
    driver.implicitly_wait(10)
    application = Application(driver)
    yield application
    driver.quit()
