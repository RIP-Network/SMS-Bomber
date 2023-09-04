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
echo " RIP-Network V21.5 "
echo ""
echo "1. Spam-SMS (Linux) (Manual)"
echo "2. Spam-SMS (Termux) (Manual) (No Funcional)"
echo "3. Spam-Whatsapp (Linux/Termux)"
echo "4. Spam-SMS (Linux) (Automatico)"
echo "5. SMS Anonimo (Linux/Termux)"
echo "99. Salir"
echo ""

echo -n "C:\RIP-Network@root >  "
read opcion

case $opcion in
1) echo "Spam-SMS (Linux)"
clear
python3 modules/SMS.py
read foo
;;

2) echo "2. Spam-SMS (Termux)"
clear
cd tools
python3 Termux.py
read foo
;;

3) echo "3. Spam-Whatsapp (Linux Termux)"
clear
python3 modules/spamWa.py
read foo 
;;

4) echo "4. Impulse (Linux)"
clear
cd tools
bash modules/SETSMS.sh
read foo
;;

5) echo "5. SMS Anonimo"
clear
cd tools
bash modules/darksms.sh
read foo
;;

99)exit 0;;

*)echo "Opcion invalida..."
sleep 1
esac
done
