import requests
from colorama import Fore, init
from os import system
from sites import sites

init(autoreset=True)

while True:
    system("clear||cls")
    print(Fore.GREEN + " ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄ ")
    print(Fore.GREEN + "▐  ▄▀   ▐ █    █   █ █   █   █ █      █ █ █   ▐ ▐  ▄▀   ▐ ")
    print(Fore.GREEN + "  █▄▄▄▄▄  ▐     ▀▄▀  ▐  █▀▀▀▀  █      █    ▀▄     █▄▄▄▄▄  ")
    print(Fore.GREEN + "  █    ▌       ▄▀ █     █      ▀▄    ▄▀ ▀▄   █    █    ▌  ")
    print(Fore.GREEN + " ▄▀▄▄▄▄       █  ▄▀   ▄▀         ▀▀▀▀    █▀▀▀    ▄▀▄▄▄▄   ")
    print(Fore.GREEN + " █    ▐     ▄▀  ▄▀   █                   ▐       █    ▐   ")
    print(Fore.GREEN + " ▐         █    ▐    ▐                           ▐        \n\nversion1.0\n\n ")
    
    user_name = input(Fore.MAGENTA + "Enter Nick Name: ")
    
    for site in sites:
        try:
            url = f"{site}{user_name}"
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + f"Profil Mevcut: {url}")
            else:
                print(Fore.RED + f"Profil Mevcut Değil: {url}")
        except requests.exceptions.RequestException:
            print(Fore.YELLOW + f"Tespit Edemedim: {site}")

    input("devam etmek için entere basın")