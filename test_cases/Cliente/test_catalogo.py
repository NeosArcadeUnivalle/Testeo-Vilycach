from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestCatalogo:
    def setup_method(self):
        self.driver = webdriver.Edge();
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/catalogo')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("\tPrueba Completada")

    def test_botones_rayado(self):
        i = 0
        j = 0
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity13']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity13']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity13']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '13']").text
        print("**********", actual)
        esperado = "6 huecos (0.68 Bs) - Tipo: Rayado"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"

    def test_botones_liso(self):
        i = 0
        j = 0
        element = self.driver.find_element(By.XPATH, "//input[@id='quantity3']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity3']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity3']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity3']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '3']").text
        print("**********", actual)
        esperado = "6 huecos (0.67 Bs) - Tipo: Liso"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"

    def test_botones_gamboote(self):
        i = 0
        j = 0
        element = self.driver.find_element(By.XPATH, "//input[@id='quantity5']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity5']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity5']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity5']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '5']").text
        print("**********", actual)
        esperado = "18 huecos (2.10 Bs) - Tipo: Gambote"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"

    def test_botones_dos_caida(self):
        i = 0
        j = 0
        element = self.driver.find_element(By.XPATH, "//input[@id='quantity16']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity16']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity16']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity16']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '16']").text
        print("**********", actual)
        esperado = "5 huecos (2.30 Bs) - Tipo: Bota Agua dos caidas"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"

    def test_botones_una_caida(self):
        i = 0
        j = 0
        element = self.driver.find_element(By.XPATH, "//input[@id='quantity4']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity4']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity4']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity4']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '4']").text
        print("**********", actual)
        esperado = "3 huecos (2.20 Bs) - Tipo: Bota Agua una caida"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"

    def test_botones_dos_caidas(self):
        i = 0
        j = 0
        element = self.driver.find_element(By.XPATH, "//input[@id='quantity12']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        while(i < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity12']//following-sibling::button[text() = '+']").click();
            time.sleep(1)
            i = i + 1

        while(j < 5):
            self.driver.find_element(By.XPATH, "//input[@id= 'quantity12']//parent::div//following-sibling::button[text() = '-']").click();
            time.sleep(1)
            j = j + 1
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id = 'quantity12']//following-sibling::button[text() = 'Comprar!']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//option[@value = '12']").text
        print("**********", actual)
        esperado = "Sin huecos (2.00 Bs) - Tipo: Pavic"
        assert esperado == actual, "El tipo no es el mismo seleccionado en el Catalogo"
