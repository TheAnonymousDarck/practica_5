# Importes 
import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestUntils(unittest.TestCase):
    # Define el driver
    def setUp(self):
        self.d = webdriver.Chrome(r"D:\marioAdair\Universidad\SeptimoSemestre\testing\chromedriver_win32\chromedriver.exe")

    # Se ejecuta la prueba
    def test_testcheckbox(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/") # se obtiene la URL
        d.maximize_window()
        time.sleep(3)
        d.find_element(By.CSS_SELECTOR, 'div.avatar').click()
        d.find_element(By.ID, 'item-1').click()
        time.sleep(6)
        elemento = d.find_element(By.XPATH, '//*[@id="tree-node-home"]')
    
        d.execute_script("arguments[0].click();", elemento)
        
        # inicio(d)
        time.sleep(3)

    def test_testradiobutton(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/") # se obtiene la URL
        d.maximize_window()
        time.sleep(3)
        d.find_element(By.CSS_SELECTOR, 'div.avatar').click()
        d.find_element(By.ID, 'item-2').click()
        time.sleep(6)

        elemento = d.find_element(By.XPATH, '//*[@id="yesRadio"]')
    
        d.execute_script("arguments[0].click();", elemento)
        
        time.sleep(5)


    def test_testalerts(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/alertsWindows") # se obtiene la URL
        d.maximize_window()
        time.sleep(3)
        d.find_element(By.ID, 'item-1').click()
        time.sleep(6)

        alert = Alert(d)
        d.find_element(By.ID, 'alertButton').click()
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        d.find_element(By.ID, 'timerAlertButton').click()
        time.sleep(6)
        alert.accept()
        time.sleep(2)
        d.find_element(By.ID, 'confirmButton').click()
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        d.find_element(By.ID, 'promtButton').click()
        time.sleep(2)
        alert.send_keys("test")
        time.sleep(2)
        alert.accept()
        time.sleep(5)

    def test_progressbar(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/progress-bar") # se obtiene la URL
        d.maximize_window()
        time.sleep(3)
        d.find_element(By.ID, 'item-4').click()
        time.sleep(6)

        btn = d.find_element(By.ID, 'startStopButton')
        btn.click()
        time.sleep(2)
        btn.click()
        time.sleep(2)
        btn.click()
        time.sleep(10)


    def test_textbox(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/") # se obtiene la URL
        d.maximize_window()
        d.find_element(By.CSS_SELECTOR, 'div.avatar').click()
        time.sleep(6)
        d.find_element(By.ID, 'item-0').click()
        time.sleep(2)
        d.find_element(By.ID, "userName").send_keys("test")
        time.sleep(2)
        d.find_element(By.ID, "userEmail").send_keys("test@test.com")
        time.sleep(2)
        d.find_element(By.ID, "currentAddress").send_keys("USA 11941 Marcel Neck Suite 529 Minnesota")
        time.sleep(2)
        d.find_element(By.ID, "permanentAddress").send_keys("USA 11941 Marcel Neck Suite 529 Minnesota")
        time.sleep(3)
        d.find_element(By.ID, "submit").click()
        time.sleep(10)


    def test_banner(self):
        d = self.d # Se define el friver en la función
        self.d.get("https://demoqa.com/") # se obtiene la URL
        d.maximize_window()
        d.find_element(By.XPATH, '//*[@id="app"]/header/a').click()
        time.sleep(5)


    def tearDown(self):
        self.d.quit()

# Ejecuta el main y genera el reporte en HTML
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output'))