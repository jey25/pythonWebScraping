import requests
import os

que = True

while que:
    sites_name = input(
        "Please write a URL or URLs you want to check. (Separated by comma)")

    sites = sites_name.split(',')
    for site in sites:
        site = site.strip().lower()

        if not ("http://" in site or "https://" in site):
            site = "http://" + site

        try:
            res = requests.get(site)

            if res.status_code == 200:
                print(site + " is UP!")
            else:
                print(site + " is Down!")
        except:
            print(f"{site} is not exist")

    while True:
        answer = input("GoGo? (y/n)")
        if not (answer == "y" or answer == "n"):
            print("Bad answer.")
        elif answer == "y":
            def clear(): return os.system('clear')
            clear()
            break
        else:
            que = False
            break
