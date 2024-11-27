from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestHome:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("\tPrueba Completada")

    def test_mapa(self):
        actual = self.driver.find_element(By.XPATH, "//iframe[@height = '300']").get_attribute("src")
        print("**********", actual)
        esperado = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d8152.484180339703!2d-68.302787604476!3d-16.63450475463702!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x915edbd7fa5321e9%3A0xb28dba774a17ba52!2sGrupo%20Industrial%20Vilycach!5e0!3m2!1ses-419!2sbo!4v1727801153352!5m2!1ses-419!2sbo"
        assert esperado == actual, "Ubicación de la Fabrica Incorrecta"