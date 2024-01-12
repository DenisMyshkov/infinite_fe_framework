from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def open_URL(self, url: str) -> None:
        try:
            self.driver.get(url)
        except Exception as error:
            print("BasePage.open_URL: ", type(error).__name__, "-", error)

    def do_click(self, by_locator) -> None:
        try:
            self.driver.find_element(*by_locator).click()
        except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException) as error:
            print("BasePage.do_click: ", type(error).__name__, "-", error)

    def input_text(self, text: str, by_locator) -> None:
        try:
            input_field = self.driver.find_element(*by_locator)
            input_field.clear()
            input_field.send_keys(text)
        except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException) as error:
            print("BasePage.input_text: ", type(error).__name__, "-", error)

    def get_text_from_element(self, by_locator) -> str:
        try:
            element = self.driver.find_element(*by_locator)
            return element.text
        except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException) as error:
            print("BasePage.get_text_from_element: ", type(error).__name__, "-", error)

    def wait_for_element(self, by_locator) -> None:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except (ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException) as error:
            print("BasePage.wait_for_element: ", type(error).__name__, "-", error)
