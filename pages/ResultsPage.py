from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ResultsPage(BasePage):
    FIRST_RESULT = (By.XPATH, '//a[contains(@jsname, "")]//h3|//li//h3[contains(@class, "title")]/a[contains(@class, "d-ib")]|//li//h2//b')
    ELEMENT_ON_PAGE = (By.XPATH, '//*[@class="main"]|//*[@class="browserExtensionPromotionWrapper"]|//*[@class="HeaderDesktopLogin"]')

    def get_first_result_link_text(self) -> str:
        self.wait_for_element(self.ELEMENT_ON_PAGE)
        return self.get_text_from_element(self.FIRST_RESULT)
