from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



import time
import pandas as pd

def inicializar_navegador():
    navegador = webdriver.Firefox()
    navegador.maximize_window()

    navegador.get("https://rpachallenge.com/")
    return navegador

def formulario(navegador):
    challenge = pd.read_excel("challenge.xlsx")

    # Inserindo dados do Excel nas variáveis
    firstName = challenge[challenge.columns[0]]
    lastName = challenge[challenge.columns[1]]
    companyName = challenge[challenge.columns[2]]
    roleCompany = challenge[challenge.columns[3]]
    addr = challenge[challenge.columns[4]]
    email = challenge[challenge.columns[5]]
    phone = challenge[challenge.columns[6]]

    


    btn_start = navegador.find_element(By.XPATH, "//button[text()='Start']")
    btn_start.click()
    btn_submit = navegador.find_element(By.XPATH, "//input[@value='Submit']")

    # Inserindo variáveis no formulário
    for i in range(len(challenge)):
        form_firstName = navegador.find_element(By.XPATH, "//label[text()='First Name']//following-sibling::input")
        form_lastName = navegador.find_element(By.XPATH, "//label[text()='Last Name']//following-sibling::input")
        form_companyName = navegador.find_element(By.XPATH, "//label[text()='Company Name']//following-sibling::input")
        form_roleCompany = navegador.find_element(By.XPATH, "//label[text()='Role in Company']//following-sibling::input")
        form_addr = navegador.find_element(By.XPATH, "//label[text()='Address']//following-sibling::input")
        form_email = navegador.find_element(By.XPATH, "//label[text()='Email']//following-sibling::input")
        form_phone = navegador.find_element(By.XPATH, "//label[text()='Phone Number']//following-sibling::input")

        form_firstName.send_keys(firstName[i])
        form_lastName.send_keys(lastName[i])
        form_companyName.send_keys(companyName[i])
        form_roleCompany.send_keys(roleCompany[i])
        form_addr.send_keys(addr[i])
        form_email.send_keys(email[i])
        form_phone.send_keys(str(phone[i]))

        time.sleep(1.5)
        
        btn_submit.click()

        time.sleep(0.5)
    print("Sucess!")



def main():
    navegador = inicializar_navegador()
    formulario(navegador)
    time.sleep(5)
    navegador.quit()

if __name__ == "__main__":
    main()
