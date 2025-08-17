from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class SettingsPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your name']")
    CHANGE_BTN = (By.XPATH, "//button[normalize-space()='Change name']")
    NAME_TEXT = lambda self, name: (By.XPATH, f"//p[normalize-space()='{name}']")

    def change_name(self, name):
        el = self.driver.find_element(*self.NAME_INPUT)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(name)
        self.click(self.CHANGE_BTN)

    def get_name(self, name):
        return self.get_text(self.NAME_TEXT(name))
