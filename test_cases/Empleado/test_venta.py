from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestVentas:
    def setup_method(self):
        self.driver = webdriver.Edge()  
        self.driver.maximize_window() 
        self.driver.get('http://127.0.0.1:8000/empleado/login')  
        time.sleep(5)  

    def teardown_method(self):
        self.driver.quit()  # Cierra el navegador
        print("Prueba Completada y navegador cerrado.")

    def test_confirmar_venta(self):
        self._login()

        self.driver.get('http://127.0.0.1:8000/ventas')
        time.sleep(5)

        boton = self.driver.find_element(By.XPATH, "//button[text()='Completar Venta']")
        actual_text = boton.text
        esperado_text = "Completar Venta"
        assert actual_text == esperado_text, f"Falla: Se esperaba '{esperado_text}' pero se obtuvo '{actual_text}'"
        boton.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        actual_alert_text = alert.text
        esperado_alert_text = "¿Estás seguro de que deseas completar esta venta?"
        assert actual_alert_text == esperado_alert_text, f"Falla: Se esperaba '{esperado_alert_text}' pero se obtuvo '{actual_alert_text}'"
        alert.accept()
        time.sleep(3)


    def test_buscar_y_eliminar_venta(self):
        self._login()

        self.driver.get('http://127.0.0.1:8000/ventas')
        time.sleep(5)

        search_box = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_box.clear()
        search_box.send_keys("EdiIo")
        time.sleep(3)

        actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'EdiIo')]").text
        esperado = "EdiIo"
        assert esperado in actual, f"Falla: Se esperaba '{esperado}' en '{actual}'"

        eliminar_boton = self.driver.find_element(By.XPATH, "//td[contains(text(), 'EdiIo')]/..//button[text()='Eliminar']")
        eliminar_boton.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        actual_alert_text = alert.text
        esperado_alert_text = "¿Estás seguro de que deseas eliminar esta venta?"
        assert actual_alert_text == esperado_alert_text, f"Falla: Se esperaba '{esperado_alert_text}' pero se obtuvo '{actual_alert_text}'"
        alert.accept()
        time.sleep(3)

        try:
            alert = self.driver.switch_to.alert
            actual_alert_text = alert.text
            print(f"Mensaje del alert adicional: {actual_alert_text}")
            alert.accept()
            time.sleep(3)
        except:
            print("No se detectó una alerta ")

        elementos = self.driver.find_elements(By.XPATH, "//td[contains(text(), 'EdiIo')]")
        assert len(elementos) == 0, "Falla: El registro no fue eliminado correctamente."

    def test_ir_a_notificaciones(self):
        self._login()

        self.driver.get('http://127.0.0.1:8000/ventas')
        time.sleep(5)

        notificacion_icono = self.driver.find_element(By.CSS_SELECTOR, "a.notification-icon")
        actual_text = notificacion_icono.text.strip()  # Quitar espacios adicionales
        print(f"Texto en la campanita: '{actual_text}'")

        assert actual_text.isdigit() or actual_text == "", f"Falla: Se esperaba un número o vacío, pero se obtuvo '{actual_text}'"
        notificacion_icono.click()
        time.sleep(5)

        actual_url = self.driver.current_url
        assert "notificaciones" in actual_url, f"No se redirigió correctamente a la página de notificaciones. URL actual: {actual_url}"



    def _login(self):
        email_input = self.driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys("david@gmail.com")
        time.sleep(2)

        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys("987654321")
        time.sleep(2)

        iniciar_sesion_boton = self.driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']")
        iniciar_sesion_boton.click()
        time.sleep(5)
