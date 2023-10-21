#!/bin/bash
#Dependencias

dependencias() {

        clear
        printf "\e[1;93mInstalando dependencias\e[0m\n"
        printf "\e[1;93mRIP-Network\e[0m\n"
        apt-get upgrade -y
        apt-get update -y
        pip3 install -r requeriments.txt
        pip install sys
        pip install os
        pip install webbrowser
        pip install selenium
        pip install platform
        pip install subprocess
        pip install time
        pip install colorama
        pip install importlib_metadata
        printf "\e[1;93mDependencias Instaladas con exito\e[0m\n"


}

dependencias
