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
print(azul+"                 V21.5"+cierre)
time.sleep(3)


def menu():
    while True:
     print(Fore.BLUE + "Opciones\n")     
     print(azul+"1) Spam-SMS (Linux)                     RIP-Network                             "+cierre)                    
     print(azul+"2) Instalar requisitos                  Version 21.5                             "+cierre)
     print(azul+"3) Version de la herramienta "+cierre)
     print(azul+"4) Spam-SMS (Termux) (No Funcional)"+cierre)
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
        webbrowser.open('https://passport.yandex.com/auth?retpath=%2F%2Fyandex.com%2Fsupport%2Fid%2Fauthorization%2Fphone-number.html')
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
        time.sleep(2)
        webbrowser.open('https://id.vk.com/auth?app_id=7733222&response_type=silent_token&v=1.60.0&redirect_uri=https%3A%2F%2Fyoula.ru%2F&uuid=Albm6l5p2NTldu5afUCZh&redirect_state=vk-connect-auth-redirect&app_settings=eyJ2a2NfYmVoYXZpb3IiOiJ3aXRob3V0X3Bob25lIiwic2VydmljZV9ncm91cHMiOnsiZnVsbF9hdXRoX3ZpYV92a2Nvbm5lY3QiOiJleHAifSwiZXh0ZXJuYWxfZGV2aWNlX2lkIjoiNjRmNTNmMTM0YWNhNiJ9')
        time.sleep(2)
        webbrowser.open('https://cloud.mail.ru')
        time.sleep(2)
        webbrowser.open('https://oferta.vodafone.es/vodafone-one/?cid=1938872349:dt-20190501:cp-vdf_tol_continuidad:cn-sem:kw-13038396:cc-:cl-no_cliente:sp-Google:cr-:gk-marca:st-prospecting:ta-base:md-marca:ds-responsive:pr-blended:wn-tol:pl-/VDF-TOL-BrandPura-Def-BASEPC&gad=1&gclid=CjwKCAjw3dCnBhBCEiwAVvLcu0H8WOPPtSdwicQo0FH7g4yJ5uRQtO3oX1B7PegELZxDZmBPxtO6PxoCdTsQAvD_BwE')
        time.sleep(2)
        webbrowser.open('https://www.finetwork.com/tarifas-movil?utm_campaign=8704888074&g_id=89205114442&utm_source=google&utm_term=compañias%20moviles%20españa&p_n=&utm_medium=paid_search&gad=1&gclid=CjwKCAjw3dCnBhBCEiwAVvLcu0ArRPJ92wEsEfiR7QNa13AWkbh7_kmumSquXDQhG1S47WwjRzGrGBoCzkUQAvD_BwE&gclsrc=aw.ds&adfcd=1693796996.LEq1fimdGkumeyMoC2Ludg.MjA4NTM5Niw3NzI1NjQ')
        time.sleep(2)
        webbrowser.open('https://www.avatel.es/fibra/?gclid=CjwKCAjw3dCnBhBCEiwAVvLcu6z1ChJ3S-zAP9qcOx1LdtU9-0afNxm07Bz1AtH1xjI9c5R0WfuZ8BoCCKQQAvD_BwE')
        time.sleep(2)

     if d == "2":
        os.system('bash install.sh')

     if d == "3":
         print("version 21.5 by RIP-Network")
    
     elif d == "4":
        print("Espere por favor...")
        os.system('clear')
        print("El spam SMS de termux no esta disponible.")
        time.sleep(2)



     elif d == "5":
        print(rojo+"Cuando se habran las paginas tendras poner el numero de la victima en las casillas que te ponga solicitar el numero y aceptar o continuar de esa manera se enviara 1 sms por cada pagina, puedes repetir el proceso muchas veces creando un buen spammer, esta herramienta es muy simple de usar y gracias a vuestro apoyo se sigue mejorando cada vez mas, gracias por usar esta herramienta para mas cosas nuevas estaria bien una estrella en el repositorio."+cierre)
        time.sleep(15)

      
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
