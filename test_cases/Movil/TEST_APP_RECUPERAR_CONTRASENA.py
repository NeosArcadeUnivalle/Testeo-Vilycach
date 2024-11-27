import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TEST_RECUPERARCONTRA(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'TEST_RECUPERARCONTRA'
    driver = None
    
    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = ''  # ID de dispositivo, si corresponde
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testTEST_RECUPERARCONTRA(self):
        # Inicio de sesión
        self.driver.find_element_by_xpath("//*[@id='usernameEditText']").send_keys('matheus@gmail.com')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='passwordEditText']"))
        )
        self.driver.find_element_by_xpath("//*[@id='passwordEditText']").click()
        self.driver.find_element_by_xpath("//*[@id='showPasswordButton']").click()
        self.driver.find_element_by_xpath("//*[@id='passwordEditText']").send_keys('123456789a')
        self.driver.find_element_by_xpath("//*[@text='INICIAR SESIÓN']").click()

        # Selección de producto
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='      6 huecos   |   0.67 Bs   |   Cantidad: 93642']"))
        )
        self.driver.find_element_by_xpath("//*[@text='      6 huecos   |   0.67 Bs   |   Cantidad: 93642']").click()

        # Cerrar sesión
        self.driver.find_element_by_xpath("//*[@text='CERRAR SESIÓN']").click()

        # Recuperación de contraseña
        self.driver.find_element_by_xpath("//*[@text='¿Olvidaste tu contraseña?']").click()
        self.driver.find_element_by_xpath("//*[@id='correoEditText']").send_keys('matheus@gmail.com')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='nombreEditText']"))
        )
        self.driver.find_element_by_xpath("//*[@id='nombreEditText']").send_keys('Matheus')
        self.driver.swipe(300, 806, 300, 937, 609)
        self.driver.find_element_by_xpath("//*[@id='apellidoEditText']").send_keys('Lisboa')
        self.driver.find_element_by_xpath("//*[@id='fechaContratacionEditText']").send_keys('2024/11/25')
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='ACEPTAR']"))
        )
        self.driver.find_element_by_xpath("//*[@text='ACEPTAR']").click()

        # Nueva contraseña
        self.driver.find_element_by_xpath("//*[@id='nuevaContrasenaEditText']").send_keys('123456789ab')
        self.driver.find_element_by_xpath("//*[@id='confirmarContrasenaEditText']").send_keys('123456789ab')
        self.driver.find_element_by_xpath("//*[@text='GUARDAR']").click()

        # Inicio de sesión con nueva contraseña
        self.driver.find_element_by_xpath("//*[@id='usernameEditText']").send_keys('matheus@gmail.com')
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='passwordEditText']"))
        )
        self.driver.find_element_by_xpath("//*[@id='passwordEditText']").send_keys('123456789ab')
        self.driver.find_element_by_xpath("//*[@text='INICIAR SESIÓN']").click()

        # Cerrar sesión nuevamente
        self.driver.swipe(681, 1421, 681, 1553, 580)
        self.driver.find_element_by_xpath("//*[@text='CERRAR SESIÓN']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
