import sys
import subprocess
 
if __name__ == "__main__":
    args = sys.argv[1:]
    print("Args", args)
    if not args:
        print("Aucune commande donnée")
    else:
        subprocess.run(args)
