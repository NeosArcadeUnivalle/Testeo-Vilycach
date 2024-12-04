from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
 
class TestMateriaPrima:
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
 
        self.driver.get('http://127.0.0.1:8000/materiaprima')
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/materiaprima/1/edit')]").click()
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//input[@name='nombreProveedor']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='nombreProveedor']").send_keys("Proveedor Editado")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='telefonoProveedor']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='telefonoProveedor']").send_keys("987654321")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='direccionProveedor']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='direccionProveedor']").send_keys("Dirección Editada")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='nombreMateriaPrima']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='nombreMateriaPrima']").send_keys("Materia Prima Editada")
        time.sleep(2)
 
        print("Guardando los cambios en el formulario...")
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Actualizar')]").click()
        time.sleep(5)
 
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(2)
       
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Proveedor Editado')]").text
        esperado = "Proveedor Editado"
        assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
    def test_agregar(self):
 
        self._login()
 
        self.driver.get('http://127.0.0.1:8000/materiaprima')
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//a[text()='Agregar Materia Prima y Proveedor']").click()
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//input[@name='nombreProveedor']").send_keys("Nuevo Proveedor")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='telefonoProveedor']").send_keys("123456789")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='direccionProveedor']").send_keys("Nueva Dirección")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='nombreMateriaPrima']").send_keys("Nueva Materia Prima")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='cantidadDisponible']").send_keys("500")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(5)
 
       
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(2)
       
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Proveedor')]").text
        esperado = "Nuevo Proveedor"
        assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
    def test_buscar_y_eliminar(self):
        self._login()
 
        self.driver.get('http://127.0.0.1:8000/materiaprima')
        time.sleep(5)
 
        # Buscar el registro
        search_box = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_box.clear()
        search_box.send_keys("Nuevo Proveedor")
        time.sleep(3)
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Proveedor')]").text
        esperado = "Nuevo Proveedor"
        assert actual == esperado, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
        # Eliminar el registro
        eliminar_boton = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Nuevo Proveedor')]/..//button[text()='Eliminar']")
        eliminar_boton.click()
        time.sleep(5)
 
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert adicional: {alert.text}")
        alert.accept()
        time.sleep(3)
       
 
    
    def _login(self):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("david@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("987654321")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']").click()
        time.sleep(5)