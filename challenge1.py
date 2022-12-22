from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

data = pd.read_excel("challenge.xlsx")

p_number = list(data["Phone Number"])
l_name = list(data["Last Name "])
r_company = list(data["Role in Company"])
c_name = list(data["Company Name"])
address = list(data["Address"])
f_name = list(data["First Name"])
email = list(data["Email"])

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.maximize_window()

navegador.get("https://www.rpachallenge.com/")

navegador.find_element("class name", 'btn-large.uiColorButton').click()

for i in range(len(data.index)):
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelFirstName"]').send_keys(f_name[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelLastName"]').send_keys(l_name[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelCompanyName"]').send_keys(c_name[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelRole"]').send_keys(r_company[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelAddress"]').send_keys(address[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelEmail"]').send_keys(email[i])
    navegador.find_element("xpath", '//*[@ng-reflect-name="labelPhone"]').send_keys(p_number[i])
    navegador.find_element("class name", 'btn.uiColorButton').click()

