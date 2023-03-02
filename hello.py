try:
    import fade
    import os, sys, ctypes, time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from colorama import Fore
except ModuleNotFoundError:
    print("installing requirements......")
    os.system("pip install -r requirements.txt")



banner = """

 █    ██  ███▄    █  ██ ▄█▀ ███▄    █  ▒█████   █     █░███▄    █ 
 ██  ▓██▒ ██ ▀█   █  ██▄█▒  ██ ▀█   █ ▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ 
▓██  ▒██░▓██  ▀█ ██▒▓███▄░ ▓██  ▀█ ██▒▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄ ▓██▒  ▐▌██▒▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
▒▒█████▓ ▒██░   ▓██░▒██▒ █▄▒██░   ▓██░░ ████▓▒░░░██▒██▓▒██░   ▓██░
░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ 
░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░░ ░░   ░ ▒░  ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
 ░░░ ░ ░    ░   ░ ░ ░ ░░ ░    ░   ░ ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ 
   ░              ░ ░  ░            ░     ░ ░      ░            ░ 



"""
faded_text = fade.fire(banner)
print(faded_text)

inp = """ 
                  Made by Unknown
            discord - ! . Unknown.ly#0001
               github - ishrak3232
               
              Input your token below"""

faded_txt = fade.fire(inp)
print(faded_txt)





token = input("          : ")
try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    time.sleep(3)
    driver.execute_script(js + f'login("{token}")')
    time.sleep(3.156e+7)
    os.system('cls')
    print(faded_text)
    print("")
    print(f"{Fore.GREEN}[+] {Fore.WHITE}succesfully loged in")
    time.sleep(3.156e+7)

except Exception as e:
    print(faded_text)
    print(f'{Fore.RED}[-] {Fore.WHITE}Cant Login error: ')
    print(f'{e}')