from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.get('http://172.16.0.1:8090')
uname = '<type-your-user-name-here>'
password = '<type-your-password-here>'
wait = WebDriverWait(driver, 10)
#Username
time.sleep(3)	
user = driver.find_element_by_class_name('textbox')
user.clear()
user.send_keys(uname)
#Password
time.sleep(3)
user = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input")))
user.clear()
user.send_keys(password)
#Login
el = driver.find_element_by_id('logincaption')
el.click()
print("Login done")
driver.close()
