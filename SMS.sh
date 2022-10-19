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
echo " RIP-Network V4.0 "
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
ls
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
ls
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