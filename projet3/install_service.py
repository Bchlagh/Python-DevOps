import os
import platform

def install_services():
    print("Mise à jour du système...")
    os.system("sudo apt update")

    print("Installation d'Apache (httpd)...")
    os.system("sudo apt install apache2")
    print("Apache a été installé avec succès.")

    print("Installation d'OpenSSH...")
    os.system("sudo apt install openssh-server")
    print("OpenSSH a été installé avec succès.")

if __name__ == "__main__":
    install_services()


