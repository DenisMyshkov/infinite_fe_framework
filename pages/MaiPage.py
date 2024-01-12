from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    SEARCH_INPUT_FIELD = (By.XPATH, '//*[@name="q"]|//*[@name="p"]|//*[@id="text"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@name="btnK"]|//*[@id="ybar-search"]|//*[@type="submit"]')

    def search_the_text(self, text: str) -> None:
        self.input_text(text, self.SEARCH_INPUT_FIELD)
        self.do_click(self.SEARCH_BUTTON)
