from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_elements.Cliente.url import URLManager
import time

class TestFooter:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get(URLManager.BASE_URL)
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("\tPrueba Completada")

    def test_derechos(self):
        actual = self.driver.find_element(By.XPATH, "//div[@class = 'container py-4']//p").text
        print("********", actual)
        esperado = "© 2024 Vilycach. Todos los derechos reservados."
        assert esperado == actual, "Los derechos del pie de pagina son incorrectos"

    def test_facebook(self):
        self.driver.find_element(By.XPATH, "//i[@class = 'fa-brands fa-facebook-f']//parent::a").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Cerrar']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h1[@class = 'html-h1 xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1vvkbs x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz']").text
        time.sleep(2)
        print("********", actual)
        esperado = "Grupo Industrial Vilycach "
        assert actual == esperado, "La redirección al facebook de Vilycach es incorrecta"

    def test_whatsapp(self):
        self.driver.find_element(By.XPATH, "//i[@class = 'fa-brands fa-whatsapp']//parent::a").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h2[@class = '_9vd5 _9scb']//child::p").text
        print("********", actual)
        esperado = "Chatea en WhatsApp con el +591 76546965"
        assert esperado == actual, "La redirección al chat de whatsapp es incorrecta"