from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import sys

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.get('http://172.16.0.1:8090')
uname = '<type-your-user-name-here>'
password = '<type-your-password-here>'
wait = WebDriverWait(driver, 10)
#Logout
if sys.argv[0] == 'logout':
	#Username
	time.sleep(5)
	user = driver.find_element_by_class_name('textbox')
	user.clear()
	user.send_keys(uname)
	#Password
	time.sleep(5)
	user = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input")))
	user.clear()
	user.send_keys(password)
	#Login
	login = driver.find_element_by_id('logincaption')
	login.click()
	print("Login")
	#Logout
	logout = driver.find_element_by_id('')
	logout.click()
	print("Logut")
	driver.close()
#Login
else :
  	#Username
	time.sleep(5)
	user = driver.find_element_by_class_name('textbox')
	user.clear()
	user.send_keys(uname)
	#Password
	time.sleep(5)
	user = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input")))
	user.clear()
	user.send_keys(password)
	#Login
	login = driver.find_element_by_id('logincaption')
	login.click()
	print("Login")
