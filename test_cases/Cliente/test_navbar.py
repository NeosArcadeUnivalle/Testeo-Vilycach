from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class testNavbar:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba Completada")