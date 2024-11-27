from appium import webdriver
from appium.options.android import UiAutomator2Options
import unittest


class TEST_INGRESOAPP(unittest.TestCase):
    driver = None

    def setUp(self):
        # Configuración de Desired Capabilities utilizando UiAutomator2Options
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "10.0"  # Cambia según la versión de tu emulador
        options.device_name = "emulator-5554"  # Cambia según el ID de tu dispositivo/emulador
        options.app_package = "com.example.versionantigua"  # Paquete de tu aplicación
        options.app_activity = "com.example.versionantigua.MainActivity"  # Actividad principal
        options.automation_name = "UiAutomator2"

        # Conexión al servidor Appium
        self.driver = webdriver.Remote(command_executor="http://localhost:4725/wd/hub", options=options)

    def testTEST_INGRESOAPP(self):
        # Prueba: Interactuar con elementos de la aplicación
        self.driver.find_element_by_xpath("//*[@id='usernameEditText']").send_keys('movil@gmail.com')
        self.driver.find_element_by_xpath("//*[@id='passwordEditText']").send_keys('159')
        self.driver.find_element_by_xpath("//*[@text='INICIAR SESIÓN']").click()

    def tearDown(self):
        # Cerrar la aplicación después de la prueba
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
