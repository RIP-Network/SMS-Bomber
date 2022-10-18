#!/usr/bin/python3

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

#Banner 

os.system('clear')

banner = Fore.RED + """…………..$……………………………………..$…………..
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
………………..¶¶……..¶¶¶¶……….¶……………………
………………..¶¶……..¶¶¶¶……….¶¶………………….
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶…………..
……….¶¶……………………………………….¶¶…………
……….¶¶……………………………………….¶¶…………
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
"""


print(banner)
print(Fore.GREEN + "              RIP-Network")
print("                 V4.0")
time.sleep(3)


def menu():
    while True:
     print(Fore.GREEN + "Opciones\n")     
     print("1) Spam-SMS (Linux)                     RIP-Network                             ")                    
     print("2) Instalar requisitos                  Version 4.0                             ")
     print("3) Version de la herramienta ")
     print("4) Spam-SMS (Termux)")
     print("5) Como usar ")
     print("99)Salir")

     d = input(Fore.LIGHTBLUE_EX + "C:\RIP-Network@root > ")

     if d == "1":
        print ("Por favor espere... ")
        os.system('clear')
        print ("Nota : No funciona con numeros virtuales.")
        time.sleep(5)
        webbrowser.open('https://www.instagram.com/accounts/password/reset/')
        time.sleep(2)
        webbrowser.open('https://accounts.snapchat.com/accounts/password_reset/phone')
        time.sleep(2)
        webbrowser.open('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
        time.sleep(2)
        webbrowser.open('https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D')
        time.sleep(2)
        webbrowser.open('https://mail.yandex.com/')
        time.sleep(2)
        webbrowser.open('https://web.telegram.org/k/')
        time.sleep
        webbrowser.open('https://www.tiktok.com/signup/phone-or-email?redirect_url=https%3A%2F%2Fwww.tiktok.com%2Fupload%3Flang%3Des&lang=es')
        time.sleep(2)
        webbrowser.open('https://ssl.zc.qq.com/v3/index-en.html')
        time.sleep(2)
        webbrowser.open('https://accounts.google.com/signup/v2/webgradsidvverify?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AM3QAYa48CweUwImQCw_3Elte75AVCrYB6qeOJD4bRLxRrQfDjza1njxfXURCntM')

     if d == "2":
        print("Vuelva atras del programa y ejecute en la terminal bash install.sh")

     if d == "3":
         print("version 4.0 by RIP-Network")
    

     elif d == "4":
        print("Espere por favor...")
        os.system('clear')
        time.sleep(4)
        os.system("termux-open-url https://www.instagram.com/accounts/password/reset/")
        time.sleep(2)
        os.system("termux-open-url https://accounts.snapchat.com/accounts/password_reset/phone")
        time.sleep(2)
        os.system("termux-open-url https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        time.sleep(2)
        os.system("termux-open-url https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D")
        time.sleep(2)
        os.system("termux-open-url https://mail.yandex.com/")
        time.sleep(2)
        os.system("termux-open-url https://web.telegram.org/k/")
        time.sleep(2)



     elif d == "5":
        print(rojo+"Cuando se habran las paginas deveras poner el numero de la victima en las casillas que te ponga el numero , esta herramienta es muy simple pero la estare actualizando en poco tiempo , gracias por usarla y espero le des una estrella en mi github y te suscribas a mi canal."+cierre)

      
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
