from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_elements.Cliente.url import URLManager
import time

class TestNavbar:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get(URLManager.BASE_URL)
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("\tPrueba Completada")

    def test_nombre_empresa(self):
        actual = self.driver.find_element(By.XPATH, "//a[@class = 'navbar-brand d-flex align-items-center']").text
        print("********", actual)
        esperado = "Vilycach"
        assert esperado == actual, "El nombre de la empresa equivocado en el Navbar"

    def test_boton_inicio(self):
        self.driver.find_element(By.XPATH, "//a[text() = 'Inicio']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//section[@class = 'hero-section']//h1").text
        print("*******", actual)
        esperado = "¡Bienvenidos a Vilycach!"
        assert esperado == actual, "La redirección del Boton de Inicio es incorrecta"

    def test_boton_comprar(self):
        self.driver.find_element(By.XPATH, "//a[text() = 'Comprar']").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, "//h1[@class = 'mb-4 text-center']").text
        print("*******", actual)
        esperado = "Comprar"
        assert esperado == actual, "La redirección del Boton de Comprar es incorrecta"

    def test_boton_catalogo(self):
        self.driver.find_element(By.XPATH, "//a[text() = 'Catálogo']").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, "//h1").text
        print("*******", actual)
        esperado = "Catálogo de Productos"
        assert esperado == actual, "La redirección del Boton de Catalogo es incorrecta"

    def test_boton_login(self):
        self.driver.find_element(By.XPATH, "//a[text() = 'Login']").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, "//h2").text
        print("*******", actual)
        esperado = "Iniciar Sesión - Empleados"
        assert esperado == actual, "La redirección del Boton de Login es incorrecta"