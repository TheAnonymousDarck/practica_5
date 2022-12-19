from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome(r"\chromedriver_win32\chromedriver.exe")
# d.get("https://demoqa.com/text-box")
# d.get("https://demoqa.com/checkbox")
d.get("https://demoqa.com/radio-button")
d.implicitly_wait(10)

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


test_c(d)