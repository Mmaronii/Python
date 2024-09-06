from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()

nav.get('https://cmspweb.ip.tv/')

nav.find_element(By.XPATH,'//*[@id="access-student"]').click()

time.sleep(5)

ra = nav.find_element(By.XPATH,'//*[@id="ra-student"]')
ra.send_keys('0000108974211')

time.sleep(5)

dig = nav.find_element(By.XPATH,'//*[@id="digit-student"]')
dig.send_keys('3')

time.sleep(5)

senha = nav.find_element(By.XPATH,'//*[@id="password-student"]')
senha.send_keys('Af2023@@')

time.sleep(5)

nav.find_element(By.XPATH,'//*[@id="btn-login-student"]').click()

time.sleep(5)

nav.find_element(By.XPATH,'//*[@id="lproom_rdfd7ef188e5d46df3-l"]').click()

time.sleep(5)

nav.find_element(By.XPATH,'//*[@id="roomDetailConference"]').click()

time.sleep(15)