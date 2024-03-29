help("False")

# import this


# import webbrowser
# import requests

# print("Let's find an old website.")
# site = "lolcats.com"
# era = "20151022"
# # url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
# url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
# response = requests.get(url)
# data = response.json()
# try:
#     old_site = data["archived_snapshots"]["closest"]["url"]
#     print("Found this copy: ", old_site)
#     print("It should appear in your browser now.")
#     webbrowser.open(old_site)
#     print(url, type(url))
# except:
#     print("Sorry, no luck finding", site)

# import webbrowser
# import json
# from urllib.request import urlopen

# print("Let's find an old website.")
# # site = input("Type a website URL: ")
# site = "lolcats.com"
# # era = input("Type a year, month, and day, like 20150613: ")
# era = "20151022"
# # url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
# url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
# response = urlopen(url)
# contents = response.read()
# text = contents.decode("utf-8")
# data = json.loads(text)
# try:
#     old_site = data["archived_snapshots"]["closest"]["url"]
#     print("Found this copy: ", old_site)
#     print("It should appear in your browser now.")
#     webbrowser.open(old_site)
#     print(url, type(url))
# except:
#     print("Sorry, no luck finding", site)
#     print(url)


# quotes = {
#     "Moe": "A wise guy, huh?",
#     "Larry": "Ow!",
#     "Curly": "Nyuk!",
# }
# stooge = "Curly"
# print(stooge, "says: ", quotes[stooge])

# spells = [
#     "Riddikulus!",
#     "Wingardium Leviosa!",
#     "Avada Kedavra!",
#     "Expecto Patronum!",
#     "Nox!",
#     "Lumos!",
# ]
# for value in spells:
#     print(value)

# for coutdown in 5, 4, 3, 2, 1, "hey!":
#     print(coutdown)
