from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestProductos:
    def setup_method(self):
        self.driver = webdriver.Edge()  
        self.driver.maximize_window()  
        self.driver.get('http://127.0.0.1:8000/empleado/login')  
        time.sleep(5) 
        
    def teardown_method(self):
        self.driver.quit()
        print("Prueba Completada")
  
      
    def test_editar(self):
            self._login()
            self.driver.get('http://127.0.0.1:8000/productos')
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//a[contains(@href, '/productos/2/edit')]").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@name='nombreProducto']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='nombreProducto']").send_keys("Producto Editado")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='cantidadDisponible']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='cantidadDisponible']").send_keys("200")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='precio']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='precio']").send_keys("50.00")
            time.sleep(2)
            tipo_ladrillo_dropdown = self.driver.find_element(By.XPATH, "//select[@id='idTipoLadrillo']")
            tipo_ladrillo_dropdown.click()
            time.sleep(1)
            tipo_ladrillo_dropdown.send_keys("Especial")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Actualizar')]").click()
            time.sleep(5)
            alert = self.driver.switch_to.alert
            print(f"Mensaje del alert: {alert.text}")
            alert.accept()
            time.sleep(5)

            actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Producto Editado')]").text
            esperado = "Producto Editado"
            assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
       

    def test_agregar(self):
            self._login()
            self.driver.get('http://127.0.0.1:8000/productos')
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//a[text()='Agregar Producto']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@name='nombreProducto']").send_keys("Nuevo Producto")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='cantidadDisponible']").send_keys("1000")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='precio']").send_keys("20.00")
            time.sleep(2)
            tipo_ladrillo = self.driver.find_element(By.XPATH, "//select[@id='idTipoLadrillo']")
            tipo_ladrillo.click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//option[text()='Liso']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
            time.sleep(5)

            alert = self.driver.switch_to.alert
            print(f"Mensaje del alert: {alert.text}")
            alert.accept()
            time.sleep(5)

            actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Producto')]").text
            esperado = "Nuevo Producto"
            assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"  

    def test_buscar_y_eliminar(self):
        self._login()

        self.driver.get('http://127.0.0.1:8000/productos')
        time.sleep(5)

        search_box = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_box.clear()
        search_box.send_keys("Nuevo Producto")
        time.sleep(3)

        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Producto')]").text
        esperado = "Nuevo Producto"
        assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"

        eliminar_boton = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Producto')]/..//button[text()='Eliminar']")
        eliminar_boton.click()
        time.sleep(5)

        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(5)

    def _login(self):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("david@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("987654321")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']").click()
        time.sleep(5)
