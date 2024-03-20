import time
import os

def vycistit():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

slovo_k_uhadnuti = "Ahoj, tak se alespoň někdo dostal k mé tajné zprávě. Nechal jsem zde tuto zprávu, aby jsi věděl, že nejsi jediný hacker v okolí. Pokud toto čteš chceš se stát nebo už jsi hacker, každopádně bych ti doporučil naučit se Python a pokud chceš, rád budu tvým učitelem(samozřejmě zadarmo. Stačí poslat zprávu přes Whatsapp nebo smsku na tel.: +420 737 658 015.). Jinak vše nejlepší a ahoj. Doufám, že brzy zavoláš a budu tě moci učit. Ahoj, tvůj přítel MR.ROBOT."
pocet_opakovani = 1000

vycistit()

for _ in range(pocet_opakovani):
    for letter in slovo_k_uhadnuti:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    time.sleep(0.5)
    vycistit()
 #   print()  # Nový řádek po vypsání celého slova