from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.free_strategy_session_button = (By.XPATH,"//a[contains(.,'Strategy')]")

    def click_free_strategy_session(self):
        self.click(self.free_strategy_session_button)

    def is_button_present(self):
        return self.is_element_present(self.free_strategy_session_button)