from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

os.system('clear')

print("Created by RIP-Network        Version ( Demo ) 10.0")
print()

a=input("Ingresa el numero completo con +34 : ")
sleep(2)
b=input("Ingresa el numero completo sin +34 : ")
sleep(2)
os.system('clear')

browser = webdriver.Chrome()
browser.get('https://www.paypal.com/es/welcome/signup/#/mobile_conf')
sleep(3)
a=input("Acepta el capcha para continuar, cuando lo hayas echo escribe lo que sea y dale enter : ")
sleep(4)
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div[1]/div/form/fieldset/div/div/div[3]/div/div[2]/div/input').send_keys(b)
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div[1]/div/form/fieldset/div/div/div[5]/div/button').send_keys(Keys.RETURN)
sleep(3)
browser.close()

print("Mensaje enviado")
sleep(2)

browser = webdriver.Chrome()
browser.get('https://accounts.snapchat.com/accounts/password_reset/phone')
sleep(3)
a=input("Acepta el capcha para continuar, cuando lo hayas echo escribe lo que sea y dale enter : ")
sleep(4)
browser.find_element_by_xpath('/html/body/div/div/main/div[1]/div/div/div[3]/form/div[1]/div/div[2]/div/input').send_keys(b)
browser.find_element_by_xpath('/html/body/div/div/main/div[1]/div/div/div[3]/form/div[3]/button').send_keys(Keys.RETURN)
sleep(6)
browser.close()

print("Mensaje enviado")
sleep(2)

print("Mensaje enviado")
sleep(2)

