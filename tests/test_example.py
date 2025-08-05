import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.driver.get(OLLAMA_URL)
        self.assertIn('Ollama UI', self.driver.title)
    
    def test_send_message(self):
        self.driver.get(OLLAMA_URL)
        dropdown=self.driver.find_element(By.CSS_SELECTOR,"button[role='combobox']")
        dropdown.click()
        gemma3 = self.driver.find_element(By.XPATH, "//*[text()='gemma3:1b']")
        gemma3.click()
        button = self.driver.find_element(By.NAME, "message")
        button.click()
        button.send_keys("Hello! Can you help me with Python?")
        button1 = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button1.click()
        textarea = self.driver.find_element(By.NAME, "message")
        self.assertEqual(textarea.text,'')
        responseArea= self.driver.find_element(By.XPATH, "//p[text()='Hello! Can you help me with Python?']")
        self.assertEqual(responseArea.text,'Hello! Can you help me with Python?')
        response_area = self.driver.find_element(By.CSS_SELECTOR, ".p-4.bg-secondary.text-secondary-foreground.rounded-r-lg.rounded-tl-lg.break-words.max-w-full.whitespace-pre-wrap")
        self.assertTrue(response_area.is_displayed())

    def test_change_name(self):
        self.driver.get(OLLAMA_URL)
        self.driver.maximize_window()
        profile_button=self.driver.find_element(By.ID,"radix-:Rln7mjt6:")
        profile_button.click()
        profile_button_clicked=self.driver.find_element(By.ID,"radix-:Rln7mjt6:")
        self.assertEqual(profile_button_clicked.get_attribute("aria-expanded"),"true")
        settings=self.driver.find_element(By.XPATH,"//button[@class='w-full']")
        settings.click()
        name=self.driver.find_element(By.XPATH,"//input[@placeholder='Enter your name']")
        name.send_keys(Keys.CONTROL + "a")   # Select all text
        name.send_keys(Keys.DELETE)         # Delete it
        name.send_keys("Tameer")
        change_name=self.driver.find_element(By.XPATH,"//button[normalize-space()='Change name']")
        change_name.click()
        self.assertEqual(self.driver.find_element(By.XPATH,"//p[normalize-space()='Tameer']").text,"Tameer")

if __name__ == '__main__':
    unittest.main()