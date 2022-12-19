from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert 


d = webdriver.Chrome(r"\chromedriver_win32\chromedriver.exe")
# d.get("https://demoqa.com/text-box")
# d.get("https://demoqa.com/checkbox")
# d.get("https://demoqa.com/radio-button")
# d.get("https://demoqa.com/alerts")
d.get("https://demoqa.com/progress-bar")
# d.implicitly_wait(10)

d.maximize_window()


def inicio(d):
    d.find_element(By.XPATH, '//*[@id="app"]/header/a').click()
    
def test_a(d):
    d.find_element(By.ID, "userName").send_keys("test")
    time.sleep(2)
    d.find_element(By.ID, "userEmail").send_keys("test@test.com")
    time.sleep(2)
    d.find_element(By.ID, "currentAddress").send_keys("USA 11941 Marcel Neck Suite 529 Minnesota")
    time.sleep(2)
    d.find_element(By.ID, "permanentAddress").send_keys("USA 11941 Marcel Neck Suite 529 Minnesota")
    time.sleep(2)
    d.find_element(By.ID, "submit").click()
    # inicio(d)
    time.sleep(5)
    
    
def test_b(d):
    # d.get("https://demoqa.com/checkbox")
    elemento = d.find_element(By.XPATH, '//*[@id="tree-node-home"]')
    
    d.execute_script("arguments[0].click();", elemento)
    
    # inicio(d)
    time.sleep(5)


def test_c(d):
    # d.get("https://demoqa.com/checkbox")
    elemento = d.find_element(By.XPATH, '//*[@id="yesRadio"]')
    
    d.execute_script("arguments[0].click();", elemento)
    
    
    # inicio(d)
    time.sleep(5)
    
def test_d(d):
    alert = Alert(d)
    # d.get("https://demoqa.com/checkbox")
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

def test_e(d):
    btn = d.find_element(By.ID, 'startStopButton')
    btn.click()
    time.sleep(2)
    btn.click()
    time.sleep(2)
    btn.click()
    time.sleep(10)
    
    
test_e(d)