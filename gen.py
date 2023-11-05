
#color
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"
#imports
import time, os, sys, random
from os import system as sm
from sys import platform as pf
from time import sleep as sp


#logo

logo = f"""
\033[1;33m
$$\   $$\  $$$$$$\.
$$ |  $$ |$$  __$$\.
$$ |  $$ |$$ /  $$ |.
$$ |  $$ |$$$$$$$$ |. \033[1;31mP   \033[1;33mA
$$ |  $$ |$$  __$$ |. \033[1;31mA   \033[1;33mL
$$ |  $$ |$$ |  $$ |. \033[1;31mB \033[1;32m& \033[1;33mE
\$$$$$$  |$$ |  $$ |. \033[1;31mL   \033[1;33mX
 \______/ \__|  \__|. \033[1;31mO


{G}DEVELOPER:   Alexander Grayson & Pablo Y Joaquin Guzman"""
sm("mkdir /sdcard/UA-GEN")
#clear
def clear():
    if pf in ["win32","win64"]:
        sm("cls")
    else:
        sm("clear")
    print(logo)
#line
def line():
    print(55*"\033[1;36m═")
#menu
fb = []
def main():
    clear()
    line()
    print(f"DEVICE MODEL\n{C}[{Y}1{C}] {G}VIVO\n{C}[{Y}2{C}] {G}XIAOMI\n{C}[{Y}3{C}] {G}SAMSUNG\n{C}[{Y}4{C}] {G}OPPO\n{C}[{Y}5{C}] {G}TECNO\n{C}[{Y}0{C}] {R}EXIT")
    line()
    select = input("Choose Device: ")
    if select == "1":
        vivo()
    elif select == "2":
        xiaomi()
    elif select == "3":
        samsung()
    elif select == "0":
        sys.exit(f"{R}BYE BYE")
    else:
        exit()
    line()

def vivo():
    clear()
    line()
    print("[1]Combine With FBAN UA\n[2]Just FBAN UA\n[3]No FBAN UA")
    line()
    fban = input("Choose Number: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    else:
        fb.append("3")
    line()
    num = int(input("How Many UA? "))
    line()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 VivoBrowser/"+str(random.randrange(5,11))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/en_PH;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
            sp(3)
            print(f"UA[{i+1}]: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/en_PH;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
            sp(3)
            print(f"UA[{i+1}]: {ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 VivoBrowser/"+str(random.randrange(5,11))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))
            sp(3)
            print(f"UA[{i+1}]: {ua}\n")
    else:
        exit()
#end
main()
