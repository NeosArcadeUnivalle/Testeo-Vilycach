from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
 
 
class TestEmpleados:
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
 
        self.driver.get('http://127.0.0.1:8000/empleados')
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/empleados/2/edit')]").click()
        time.sleep(5)
 
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("EdiItado")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='apellido']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys("ediIt")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='correoElectronico']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='correoElectronico']").send_keys("editYado@gmail.com")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("987651321")
        time.sleep(2)
 
        self.driver.find_element(By.XPATH, "//input[@name='puesto']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='puesto']").send_keys("Administrador")
        time.sleep(2)
 
        fecha_campo = self.driver.find_element(By.XPATH, "//input[@name='fechaContratacion']")
        self.driver.execute_script("arguments[0].value = '2024-10-28';", fecha_campo)
        time.sleep(2)
 
 
 
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Actualizar')]").click()
        time.sleep(5)
 
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(5)
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'EdiItado')]").text
        esperado = "EdiItado"
        assert esperado == actual, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
 
    def test_agregar(self):
        self._login()
 
        self.driver.get('http://127.0.0.1:8000/empleados')
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[text()='Agregar Empleado']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='nombre']").send_keys("prueba")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='apellido']").send_keys("preubas")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='correoElectronico']").send_keys("pruebaas@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("555555555")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='puesto']").send_keys("Administrador")
        time.sleep(2)
 
        fecha_campo = self.driver.find_element(By.XPATH, "//input[@name='fechaContratacion']")
        self.driver.execute_script("arguments[0].value = '2024-12-01';", fecha_campo)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(5)
 
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(5)
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'prueba')]").text
        esperado = "prueba"
        assert esperado == actual, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
    def test_buscar_y_eliminar(self):
        self._login()
 
        self.driver.get('http://127.0.0.1:8000/empleados')
        time.sleep(5)
 
        # Buscar el registro
        search_box = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_box.clear()
        search_box.send_keys("prueba")
        time.sleep(3)
 
        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'prueba')]").text
        esperado = "prueba"
        assert esperado == actual, f"Falla: Se esperaba '{esperado}' pero se obtuvo '{actual}'"
 
        # Eliminar el registro
        eliminar_boton = self.driver.find_element(By.XPATH, "//td[contains(text(), 'prueba')]/..//button[text()='Eliminar']")
        eliminar_boton.click()
        time.sleep(5)
 
        # Manejo de la primera alerta
        alert = self.driver.switch_to.alert
        print(f"Mensaje del alert: {alert.text}")
        alert.accept()
        time.sleep(3)
 
        # Manejo de la alerta adicional
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