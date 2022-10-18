#Dependencias

dependencias() {

        clear
        printf "\e[1;93mInstalando dependencias\e[0m\n"
        printf "\e[1;93mRIP-Network\e[0m\n"
        sudo apt-get upgrade && update -y
        pip install sys
        pip install os
        pip install webbrowser
        pip install selenium
        pip install platform
        pip install subprocess
        pip install time
        pip install colorama
         printf "\e[1;93mDependencias Instaladas con exito\e[0m\n"


}

dependencias
