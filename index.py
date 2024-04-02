crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ", ".join(crypto_list)
print(crypto_string)


# name = "Из строки можно извлечь подстроку"
# new_str = name.split(" ")
# print(new_str)

# print(len(""))
# print(name[5:])
# print(name[5:-3])
# print(name[5:20])
# print(name[-5:-2])
# print(name[::])
# print(name[::])
# print(name[-1::-1])
# print(name[::-1])
# print(name[-50::])
# print(name[:100:])
# print(name[6:5])
# print(name, id(name))
# name_new = name.replace('H', "P")
# print(name_new, id(name_new))
# name_two = "P" + name[1:]
# print(name_two, id(name_two))


# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters[0])
# print(letters[1])
# letters[9] = 20
# print(letters[200])
# print(letters[-1])
# start = "Na " * 4 + "\n\t"
# middle = "Hey " * 3 + "\n\t\t"
# end = "Goodbye."
# print(start + start + middle + end)

# a = "Duck."
# b = a
# c = "Grey Duck!"
# print(a + b + c)
# print(a, b, c)

# palindrome = ("+++"
#               "---"
#               "___")
# palindrome = "+++""---""___"
# palindrome = "+++" + "---" + "___"
# palindrome = r'''Boys and girls, come out to play.
#     The moon doth shine as bright as day.'''
# print(palindrome)

# poem = '''There was a Young Lady of Norway,
#     Who casually sat in a doorway;
#         When the door squeezed her flat,
#             She exclaimed, "What of that?"
#                 This courageous Young Lady of Norway.'''

# print(poem)

# secret = 7
# guess = 5
# if guess < secret:
#     print("too low")
# elif guess > secret:
#     print(" too hight")
# else:
#     print("just right")


# tweet_limit = 20
# tweet_string = "Blah" * 50
# # diff = tweet_limit - len(tweet_string)
# if diff := tweet_limit - len(tweet_string) >= 0:
#     print("Afifting tweet")

# else:
#     print("Went over by", abs(diff))
#     print(len(tweet_string))
#     print(tweet_limit - len(tweet_string))

# tweet_limit = 280
# tweet_string = "Blah" * 50
# diff = tweet_limit - len(tweet_string)
# if diff >= 0:
#     print("Afifting tweet")
# else:
#     print("Went over by", abs(diff))

# vowels = "aeiu"
# vowels_set = {"a","e","i","o","u"}
# vowels_set = ("a","e","i","o","u")
# vowels_dict = {"a":"apple",
#                "e":"elephant",
#                "i":"impala",
#                "o":"ocelot",
#                "u":"unicorn"}
# letter = "o"
# if letter in vowels_dict:
#     print(letter,"is a vowel")
# else:
#     print("NO Text")

# letter = 'o'
# if letter == 'a' or letter == 'e' \
#     or letter == 'i' \
#     or letter == 'o' \
#     or letter == 'u':
#     print(letter, 'is a vowel')
# else:
#     print(letter,"is not a vowel")

# some_list = None
# if some_list:
#     print("True")
# else:
#     print("False")

# False

# False
# None
# 0
# 0.0
# ''
# [] список
# () кортеж
# {} словарь
# set() пустое множество

# furry = False
# large = True
# if furry:
#     if large:
#         print("It's a yeti.")
#     else:
#         print("It's a cat!")
# else:
#     if large:
#         print("it's a whale!")
#     else:
#         print("it's a human. Or hairless cat.")


# sum = 1 + \
#       2 + \
#       3 + \
#       4
# print(sum)


# print("No comment: quotes make the # harmless.")

# 60 с/мин * 60 мин/ч * 24 ч/день
# seconds_per_day = 86400 #adadad

# help("False")

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
