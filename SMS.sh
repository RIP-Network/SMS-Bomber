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
echo " RIP-Network V5.0 "
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
echo "Version 5.0"
sleep 4
read foo
;;
4) echo "Spam-SMS (Termux)"
open https://www.instagram.com/accounts/password/reset/
open https://accounts.snapchat.com/accounts/password_reset/phone
open https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0
open https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D
open https://mail.yandex.com/
open https://web.telegram.org/k/
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
