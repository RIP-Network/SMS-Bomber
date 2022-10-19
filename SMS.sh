#!bin/bash

clear
sleep 2
echo "…………..$……………………………………..$………….."
echo "…………$$……………………………………..$$…………"
echo "…………$$……………………………………..$$…………"
echo "…………..$$s………………………………s$$………….."
echo "…………….$$$$……………………….$$$$……………."
echo "………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………"
echo "………………..³$$$$..¶¶¶¶¶¶..$$$$³……………….."
echo "………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………"
echo "…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………"
echo "…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………"
echo "…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………"
echo "………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶……………….."
echo "………………..¶¶……..¶¶¶¶……….¶……………………"
echo "………………..¶¶……..¶¶¶¶……….¶¶…………………."
echo "………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶…………………."
echo "………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶…………………."
echo "……………………….¶¶¶¶¶¶¶¶¶…………………………"
echo "……………………….¶..¶..¶..¶..¶…………………………"
echo "…………¶…………..¶…………..¶…………..¶………….."
echo "……….¶¶……………………………………….¶¶…………"
echo "……….¶¶……………………………………….¶¶…………"
echo "……….¶¶…………..¶¶……….¶¶…………..¶¶…………"
echo "……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………"
echo "……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶…….."
echo "….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……"
echo "……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶…….."

while :
do

echo -e "\e[1;32m"
echo " RIP-Network V6.0 "
echo ""
echo "1. Spam-SMS (Linux)"
echo "2. Instalar requisitos"
echo "3. Version de la herramienta"
echo "4. Spam-SMS (Termux)"
echo "5. Como usar "
echo "99. Salir"
echo ""

echo -n "C:\RIP-Network@root >  "
read opcion

case $opcion in
1) echo "Spam-SMS (Linux)"
open https://www.instagram.com/accounts/password/reset/
open https://accounts.snapchat.com/accounts/password_reset/phone
open https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0
open https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D
open https://mail.yandex.com/
open https://web.telegram.org/k/
open https://account.live.com/username/recover?wreply=https://login.live.com/login.srf%3flc%3d3082%26mkt%3dES-ES%26wa%3dwsignin1.0%26rpsnv%3d13%26ct%3d1666198253%26rver%3d7.0.6737.0%26wp%3dMBI_SSL%26wreply%3dhttps%253a%252f%252foutlook.live.com%252fowa%252f0%252f%253fstate%253d1%2526redirectTo%253daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%2526RpsCsrfState%253df0538ed8-93f0-d07e-bf5a-7a46544e907d%26id%3d292841%26aadredir%3d1%26whr%3drevtxt.com%26CBCXT%3dout%26lw%3d1%26fl%3ddob%252cflname%252cwld%26cobrandid%3d90015%26contextid%3d5015B1DD9156F9A2%26bk%3d1666198254%26uaid%3d3969d24881894986a209dd5917148ab9&id=292841&cobrandid=90015&mkt=ES-ES&lc=3082&uaid=3969d24881894986a209dd5917148ab9&uiflavor=web
open https://help.steampowered.com/es/wizard/HelpWithLoginInfo?issueid=406

read foo
;;
2) echo "Instalar requisitos"
pip install sys
pip install os
pip install webbrowser
pip install selenium
pip install platform
pip install subprocess
pip install time
pip install colorama
pip install importlib_metadata
read foo
;;
3) echo "Version de la herramienta"
echo "Version 6.0"
sleep 4
read foo
;;
4) echo "Spam-SMS (Termux)"
cd tools
bash Termux.sh
read foo
;;
5) echo "Como usar"
echo "Cuando se habran las paginas deveras poner el numero de la victima en las casillas que te ponga el numero , esta herramienta es muy simple pero la estare actualizando en poco tiempo , gracias por usarla y espero le des una estrella en mi github y te suscribas a mi canal."
sleep 5
read foo
;;
99)exit 0;;

*)echo "Opcion invalida..."
sleep 1
esac
done
