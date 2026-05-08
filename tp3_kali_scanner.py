import os
import datetime

def create_report_dir():
    if not os.path.exists("reports"):
        os.makedirs("reports")

def save_report(content):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/scan_{now}.txt"
    with open(filename, "w") as f:
        f.write(content)
    print(f"[+] Rapport sauvegardé : {filename}")

def run_scan(command):
    print(f"[+] Exécution : {command}")
    result = os.popen(command).read()
    save_report(result)

def menu():
    while True:
        print("\n=== MINI SCANNER ===")
        print("1) Scan rapide (top ports)")
	print("=== Scanner lancé ===")
        print("2) Scan services")
        print("3) Scan personnalisé")
        print("4) Quitter")

        choice = input("Choix : ")

        if choice == "1":
            run_scan("nmap 127.0.0.1")
        elif choice == "2":
            run_scan("nmap -sV 127.0.0.1")
        elif choice == "3":
            opt = input("Options nmap : ")
            run_scan(f"nmap {opt} 127.0.0.1")
        elif choice == "4":
            break

create_report_dir()
menu()
