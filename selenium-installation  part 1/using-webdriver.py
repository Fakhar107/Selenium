from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = 'http://the-internet.herokuapp.com/login'

driver.get(url)

driver.find_element(By. XPATH,'//*[@id="username"]').send_keys('tomsmith')
driver.find_element(By. XPATH,'//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element(By. XPATH,'//*[@id="login"]/button').click()

