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
print(rojo+"Happy Hacking"+cierre)
os.system('sleep 5')
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
print(Fore.BLUE + "              RIP-Network")
print(azul+"                 V8.0"+cierre)
time.sleep(3)


def menu():
    while True:
     print(Fore.BLUE + "Opciones\n")     
     print(azul+"1) Spam-SMS (Linux)                     RIP-Network                             "+cierre)                    
     print(azul+"2) Instalar requisitos                  Version 8.0                             "+cierre)
     print(azul+"3) Version de la herramienta "+cierre)
     print(azul+"4) Spam-SMS (Termux)"+cierre)
     print(azul+"5) Como usar "+cierre)
     print(azul+"99)Salir"+cierre)

     d = input(Fore.LIGHTBLUE_EX + "C:\RIP-Network@root > ")

     if d == "1":
        print ("Por favor espere... ")
        os.system('sleep 3')
        os.system('clear')
        print ("Nota : No funciona con numeros virtuales.")
        time.sleep(2)
        webbrowser.open('https://www.instagram.com/accounts/password/reset/')
        time.sleep(2)
        webbrowser.open('https://accounts.snapchat.com/accounts/password_reset/phone')
        time.sleep(2)
        webbrowser.open('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
        time.sleep(2)
        webbrowser.open('https://www.paypal.com/es/welcome/signup/#/mobile_conf')
        time.sleep(2)
        webbrowser.open('https://passport.yandex.com/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1')
        time.sleep(2)
        webbrowser.open('https://web.telegram.org/k/')
        time.sleep
        webbrowser.open('https://www.tiktok.com/signup/phone-or-email?redirect_url=https%3A%2F%2Fwww.tiktok.com%2Fupload%3Flang%3Des&lang=es')
        time.sleep(2)
        webbrowser.open('https://accounts.google.com/signup/v2/webgradsidvverify?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AM3QAYa48CweUwImQCw_3Elte75AVCrYB6qeOJD4bRLxRrQfDjza1njxfXURCntM')
        time.sleep(2)
        webbrowser.open('https://help.steampowered.com/es/wizard/HelpWithLoginInfo?issueid=406')
        time.sleep(2)
        webbrowser.open('https://account.live.com/username/recover?wreply=https://login.live.com/login.srf%3flc%3d3082%26mkt%3dES-ES%26wa%3dwsignin1.0%26rpsnv%3d13%26ct%3d1666198253%26rver%3d7.0.6737.0%26wp%3dMBI_SSL%26wreply%3dhttps%253a%252f%252foutlook.live.com%252fowa%252f0%252f%253fstate%253d1%2526redirectTo%253daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%2526RpsCsrfState%253df0538ed8-93f0-d07e-bf5a-7a46544e907d%26id%3d292841%26aadredir%3d1%26whr%3drevtxt.com%26CBCXT%3dout%26lw%3d1%26fl%3ddob%252cflname%252cwld%26cobrandid%3d90015%26contextid%3d5015B1DD9156F9A2%26bk%3d1666198254%26uaid%3d3969d24881894986a209dd5917148ab9&id=292841&cobrandid=90015&mkt=ES-ES&lc=3082&uaid=3969d24881894986a209dd5917148ab9&uiflavor=web')
        time.sleep(2)
        webbrowser.open('https://tinder.com/es-ES')
        time.sleep(2)
        webbrowser.open('https://badoo.com/landing')

     if d == "2":
        print("Vuelva atras del programa y ejecute en la terminal bash install.sh")

     if d == "3":
         print("version 8.0 by RIP-Network")
    
     elif d == "4":
        print("Espere por favor...")
        os.system('clear')
        print("El spam SMS de termux no esta disponible en python ejecute el bash por favor.")
        time.sleep(2)



     elif d == "5":
        print(rojo+"Cuando se habran las paginas deveras poner el numero de la victima en las casillas que te ponga el numero , esta herramienta es muy simple pero la estare actualizando en poco tiempo , gracias por usarla y espero le des una estrella en mi github y te suscribas a mi canal."+cierre)

      
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
