#!/bin/bash
#Dependencias

dependencias() {

        clear
        printf "\e[1;93mInstalando dependencias\e[0m\n"
        printf "\e[1;93mRIP-Network\e[0m\n"
        apt-get upgrade && update
        apt-get install python3
        pip3 install -r requeriments.txt
        pip3 install sys
        pip3 install os
        pip3 install webbrowser
        pip3 install selenium
        pip3 install platform
        pip3 install subprocess
        pip3 install time
        pip3 install colorama
        pip3 install importlib_metadata
        printf "\e[1;93mDependencias Instaladas con exito\e[0m\n"


}

dependencias
