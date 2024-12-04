from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAnalisis:
    def setup_method(self):
        self.driver = webdriver.Edge()  
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/empleado/login')
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba Completada")

    def test_visualizar_analisis(self):
        self._login()

        self.driver.get('http://127.0.0.1:8000/bi')  # Ruta de la página de análisis
        time.sleep(5)

        previous_height = 0
        while True:
            current_height = self.driver.execute_script("return document.body.scrollHeight")

            if current_height == previous_height:
                print("Se alcanzó el final de la página.")
                break
            else:
                self.driver.execute_script("window.scrollBy(0, 300);")
                time.sleep(2)
                previous_height = current_height

        self.driver.execute_script("window.scrollTo(0, 0);")  # Volver al inicio
        time.sleep(2)

        actual = self.driver.find_element(By.XPATH, "//h2[@class='chart-title']").text
        print("********", actual)
        esperado = "Productos Más Vendidos por Cantidad" 
        assert esperado == actual, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"


    def _login(self):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("david@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("987654321")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']").click()
        time.sleep(5)
