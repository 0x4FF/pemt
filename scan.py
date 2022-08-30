import requests, os, socket, colorama, urllib3; from colorama import Fore; from bs4 import BeautifulSoup



def domain_search():
    query = input(">$ Enter domain: ")
    
    if query == "q":
        main()
        
    with open('domains.txt', 'r+') as file:
        content = file.read()
        
    domains = content.splitlines()
    found = []
    
    for domains in domains:
        domain_url = f"https://{domains}.{query}"
        try:
            requests.get(domain_url)
        except requests.ConnectionError:
            pass
        else:
            print(f"{Fore.GREEN}Domain Found: {domain_url}")
            found.append(domain_url)

            
def directory_bruteforce():
    query = input(">$ Enter link: ")
    
    if query == "q":
        main()
        
    with open('directorys.txt', 'r+') as file:
        content = file.read()
        
    directorys = content.splitlines()
    found = []
    
    for directorys in directorys:
        directory_url = f"{query}{directorys}"
        response = requests.get(str(directory_url))
        if (response.status_code == 200):
            print(f"{Fore.GREEN}Found: {directory_url}")
            found.append(directory_url)
        elif (response.status_code == 404):
            print(f"{Fore.RED}Invalid: {directory_url}")

            
def port_scan():
    h = input(">$ Enter IP: ")
    
    if h == "q":
        main()
        
    try:
        for port in range (1, 65536):
            s = socket.socket()
            result = s.connect_ex((h, port))
            if result == 0:
                print(f"{Fore.GREEN}{h}: {port} is open")
            else:
                print(f"{Fore.RED}{h}: {port} is closed")
    except socket.error:
        print(f"couldnt connect to {h}")

        
def get_html():
    http = urllib3.PoolManager()
    url = input(">$ Enter link: ")
    
    if url == "q":
        main()
        
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)
    with open('site.html', 'w+') as file:
        file.write(str(soup))

        
def main():
    choice = input("[1] Subdomain Scan   [2] Directory Bruteforce   [3] Port Scanner    [4] Get HTML Code   [q] Exit & Back: ")
    if choice == "1":
        os.system("cls")
        domain_search()
        
    elif choice == "2":
        os.system("cls")
        directory_bruteforce()
        
    elif choice == "3":
        os.system("cls")
        port_scan()
        
    elif choice == "q":
        exit()
    else:
        print("Not an option..")

        
main()
