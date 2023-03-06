try:
    import fade
    import os, sys, ctypes, time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from colorama import Fore
    from fp.fp import FreeProxy
    from selenium import webdriver
    from selenium.webdriver.common.proxy import Proxy, ProxyType   
    from selenium import webdriver
    from selenium.webdriver.common.proxy import *
    from selenium.webdriver.firefox.options import Options
except ModuleNotFoundError:
    print("installing requirements......")
    os.system("pip install fade selenium free-proxy")









def login(token):
    trey = """
    [1] use custom proxy
    [2] use generated proxy
    [3] none. use your proxy
    """
    yyyy = fade.fire(trey)
    print(yyyy+"\n")
    prox = input(" >> ")

    if prox == "3":
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
            time.sleep(100)
    elif prox == "1":
        try:
             ewq = input("proxy >> ")
             myProxy = ewq
             proxy = Proxy({
             'proxyType': ProxyType.MANUAL,
             'httpProxy': myProxy,
             'sslProxy': myProxy,
             'noProxy': ''})

             options = Options()
             options.proxy = proxy
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
            time.sleep(100)
    elif prox == "2":
        try:
             print(f"{Fore.LIGHTCYAN_EX} generating proxy........")
             pro = FreeProxy(rand=True).get()
             print(f"{Fore.BLUE} got proxy : {pro}")
             myProxy = pro
             proxy = Proxy({
             'proxyType': ProxyType.MANUAL,
             'httpProxy': myProxy,
             'sslProxy': myProxy,
             'noProxy': ''})

             options = Options()
             options.proxy = proxy
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
            time.sleep(100)




if __name__ == "__main__":
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
    toki = input(" >> ")
    login(token=toki)
