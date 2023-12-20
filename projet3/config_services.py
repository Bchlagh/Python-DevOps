#!/usr/bin/env python3

import os

def configure_services():
    # Modifier le fichier de configuration Apache (exemple : /etc/apache2/apache2.conf)
    # Ajouter/modifier les directives nécessaires
    apache_conf_path = "/etc/apache2/apache2.conf"
    os.system(f"echo '\n# Nouvelle directive ajoutée par le script' | sudo tee -a {apache_conf_path}")
    os.system("sudo systemctl restart apache2")

    # Commit et push des changements dans la branche 'develop'
    os.system("git add .")
    os.system("git commit -m 'Configurer les services'")
    os.system("git push origin develop")

    # Fusion avec la branche 'master'
    os.system("git checkout master")
    os.system("git merge develop")
    os.system("git push origin master")
    os.system("git checkout develop")

if __name__ == "__main__":
    configure_services()
