from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os

# Inicializa o recurso selenium
driver = webdriver.Firefox()

#Inicializa os parametros de busca
web_site = "https://e2etec.com.br"
search_pattern =  "//div[@id='panel-w5f11b62f8fe0c-0-0-0']/div[1]/div[1]/p[1]"

driver.get(web_site)
telefoneEmail = driver.find_element(
    By.XPATH, search_pattern)
driver.implicitly_wait(2)

#Prepara os dados para criar o arquivo txt
pasta = Path("c:/temp/")
if not os.path.exists(pasta):
    os.makedirs(pasta)
arquivo = pasta / "e2etec_py.txt"
with open(arquivo, 'w+') as file:
    file.write(telefoneEmail.text)
#Encerra o recusro selenium
driver.close()

