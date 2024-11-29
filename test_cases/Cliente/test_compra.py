from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_elements.Cliente.url import URLManager
import time

class TestCompra:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get(URLManager.COMPRA)
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba Completada")

    def test_form(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'nombre']").send_keys("1234567-.-.-.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'nombre']").send_keys("Test")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'apellido']").send_keys("1234567..-....")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'apellido']").send_keys("Automatizado")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@id = 'tieneEmpresa']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[@value = 'si']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'empresa']").send_keys("123423..-...")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'empresa']").send_keys("Univalle")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'telefono']").send_keys("aaaaaaa..-....")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'telefono']").send_keys("7364836")
        time.sleep(2)

        element = self.driver.find_element(By.XPATH, "//input[@name = 'cantidad']")
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});", element)
        time.sleep(2)

        if not element.is_displayed():
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(2)

        self.driver.find_element(By.XPATH, "//select[@id = 'producto']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[@value = '13']").click()
        time.sleep(2)

        limpiar = self.driver.find_element(By.XPATH, "//input[@name = 'cantidad']")
        limpiar.clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'cantidad']").send_keys("cr.-.-.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'cantidad']").send_keys("5000")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@name = 'nombreLugarVenta']").send_keys("6473804")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'nombreLugarVenta']").send_keys("Miraflores")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'direccion']").send_keys("Av. Argentina")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'ciudad']").send_keys("748384")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'ciudad']").send_keys("La Paz")
        time.sleep(2)

        element1 = self.driver.find_element(By.XPATH, "//button[text() = 'Solicitar Compra']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});", element1)
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[text() = 'Solicitar Compra']").click()
        time.sleep(2)
