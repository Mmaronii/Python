from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()

nav.get('https://sed.educacao.sp.gov.br/')

time.sleep(1)

user = nav.find_element(By.XPATH,'//*[@id="name"]')
user.send_keys('00001089742113sp')

time.sleep(10)

senha = nav.find_element(By.XPATH,'//*[@id="senha"]')
senha.send_keys('Af2023@@')

time.sleep(10)

nav.find_element(By.XPATH,'//*[@id="botaoEntrar"]').click()

time.sleep(10)
