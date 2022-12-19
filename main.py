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
        self.d = webdriver.Chrome(
            r"\chromedriver_win32\chromedriver.exe")

    # Se ejecuta la prueba
    def test_llenado(self):
        d = self.d  # Se define el friver en la función
        self.d.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")  # se obtiene la URL

        # Definición de variables
        sources = ["box1", "box2", "box3", "box4", "box5", "box6", "box7"]
        targets = ["box101", "box102", "box103", "box104", "box105", "box106", "box107"]

        # Inicio de la prueba
        d.maximize_window()  # Maximizar Ventana
        for i in range(0, 7):  # Se itera sobre la cantidad de elementos para realizar las acciones
            source = d.find_element(By.ID, sources[i])
            target = d.find_element(By.ID, targets[i])
            ActionChains(d).drag_and_drop(source, target).perform()
        time.sleep(10)  # Tiempo de espera final

    # Función para cerrar el navegador
    def tearDown(self):
        self.d.quit()


# Ejecuta el main y genera el reporte en HTML
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output'))