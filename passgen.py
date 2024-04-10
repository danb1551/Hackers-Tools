import subprocess

def vycistit():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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


print("Your  password list was saved to the same folder and the name is wordlist.txt")
ano = input("Go back to the main menu[Y/N]:")
anone(ano)
def hlavni_cast():
    print(Fore.RED + "#######################################################################")
    print(Fore.GREEN + "#.....................................................................#")
    print(Fore.BLUE + "#.....................................................................#")
    print(Fore.MAGENTA + "#.....................................................................#")
    print(Fore.CYAN + "#.....................................................................#")
    print(Fore.RED + "#................." + Style.RESET_ALL + "Welcome in Password list generator" + Fore.RED + "..................#")
    print(Fore.GREEN + "#........................" + Style.RESET_ALL + "Created by: Danb1551" + Fore.GREEN + ".........................#")
    print(Fore.BLUE + "#.........................." + Style.RESET_ALL + "Web: TERMUX.WZ.CZ" + Fore.BLUE + "..........................#")
    print(Fore.MAGENTA + "#......................" + Style.RESET_ALL + "Instagram: hackit.121212" + Fore.MAGENTA + ".......................#")
    print(Fore.CYAN + "#..................." + Style.RESET_ALL + "E-mail: hackit.121212@gmail.com" + Fore.CYAN + "...................#")
    print(Fore.RED + "#...................." + Style.RESET_ALL + "ONLY FOR EDUCATIONAL PURPOSES" + Fore.RED + "....................#")
    print(Fore.GREEN + "#.....................................................................#")
    print(Fore.BLUE + "#.....................................................................#")
    print(Fore.MAGENTA + "#.....................................................................#")
    print(Fore.CYAN + "#.....................................................................#")
    print(Fore.RED + "#######################################################################")

vycistit()
hlavni_cast()
time.sleep(0.25)

list=[]
names=[]
temp_names=[]
phoneNo=''
dob=input("Date of birth(DDMMYYYY):")
if(len(dob)==8):
    day=dob[:2]
    month=dob[2:4]
    year=dob[4:]
else:
    print("Wrong format for DOB, make sure it is 8 numbers in DDMMYYYY")
    exit()

phoneNo=input("Enter phone number:")

def ListOfImportantWords():
    names.append(input("First name:"))
    names.append(input("Surname:"))
    names.append(input("Nickname:"))
    print("\n")
    names.append(input("Partners name:"))
    names.append(input("Partners Nickname:"))
    print("\n")
    names.append(input("Pets name:"))
    names.append(input("Company name:"))
    print("\n")
    names.append(input("Childs name:"))
    names.append(input("Childs nickname:"))
    print("\n")
    names.append(input("City:"))
    names.append(input("Country:"))
    names.append(input("Favourite colour:"))
    print("Enter all other keywords: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while('' in names) :
        names.remove('')

def permute(inp):
    n = len(inp)

    mx = 1 << n

    inp = inp.lower()

    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()

        temp = ""
        for i in combination:
            temp += i
        temp_names.append(temp)


def WordListCreator(list):
    for word in names:
        for i in range(0,len(word)+1):
            list.append(word[:i]+day+word[i:])
            list.append(word[:i]+month+word[i:])
            list.append(word[:i]+year+word[i:])
            if len(year)==4:
                list.append(word[:i]+year[2:]+word[i:])
            list.append(word[:i]+phoneNo+word[i:])
    if not phoneNo=='':
        list.append(phoneNo)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)



ListOfImportantWords()
for i in names:
    permute(i)
names=names+temp_names
WordListCreator(list)
WriteToFile(list)

print("Your  password list was saved to the same folder and the name is wordlist.txt")
ano = input("Go back to the main menu[Y/N]:")
anone()