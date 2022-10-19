import sys, os, webbrowser, platform, subprocess, time
from colorama import Fore
from importlib_metadata import version

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

os.system('clear')
print(Fore.GREEN + "              RIP-Network")
print("                 V6.0")
time.sleep(3)


def menu():
    while True:
     print(Fore.GREEN + "Opciones\n")     
     print("1) 1                  RIP-Network                             ")                    
     print("2) 2                  Version 6.0                             ")
     print("3) 3")
     print("4) 4")
     print("5) 5")
     print("6) 6")

     d = input(Fore.LIGHTBLUE_EX + "Seleccione todas las opciones de 1 en 1 > ")

     if d == "1":
        print ("Por favor espere... ")
        os.system('clear')
        os.system("termux-open-url https://www.instagram.com/accounts/password/reset/")

        

     if d == "2":
        os.system('clear')
        os.system("termux-open-url https://accounts.snapchat.com/accounts/password_reset/phone")

     if d == "3":
        os.system("termux-open-url https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        os.system('clear')
    

     elif d == "4":
        os.system('clear')
        os.system("termux-open-url https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D")
        os.system("termux-open-url https://web.telegram.org/k/")
        time.sleep(2)



     elif d == "5":
        os.system('clear')
        os.system("termux-open-url https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D")
        
      
     elif d == "6":
        os.system('clear')
        os.system("termux-open-url https://web.telegram.org/k/")

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
