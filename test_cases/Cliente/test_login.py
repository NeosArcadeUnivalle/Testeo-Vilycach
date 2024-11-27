from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/empleado/login')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("\tPrueba Completada")

    def test_login_fallido(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("gabrielvillarreal@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("neosarca")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text() = 'Iniciar Sesión']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//li").text
        print("***********", actual)
        esperado = "Las credenciales no coinciden con nuestros registros."
        assert esperado == actual, "Inicio de Sesión no controlado con credenciales incorrectas"

    def test_login_Exitoso(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("gabrielvillarreal@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("neosarcade")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text() = 'Iniciar Sesión']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH, "//h1").text
        print("***********", actual)
        esperado = "Lista de Productos"
        assert esperado == actual, "Inicio de Sesión no controlado para credenciales correctas"