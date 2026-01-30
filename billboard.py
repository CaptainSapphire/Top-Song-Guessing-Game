import requests
from bs4 import BeautifulSoup
import os
import time 

base_url = "https://www.billboard.com/charts/hot-100/"

print("Do you know what's trending today?")

# collect the data from the page (the top song)
res = requests.get(base_url)
soup = BeautifulSoup(res.text, "html.parser")

# class name might change over time, so inspect the page if it breaks

# This targets the container for the #1 spot specifically
chart_items = soup.find_all("li", class_="lrv-u-width-100p")
number1 = chart_items[0].find("h3", id="title-of-a-story").get_text(strip=True)

# getting the name of the creator of the number 1 song
# the class naming of the artist is chud so I am using span and c-label to get it
artist = chart_items[0].find("span", class_="c-label").get_text(strip=True)

# for loop of guesses of the top song
for i in range(5): # 5 guesses is fair
    guess = input("What's the current #1 song on the Billboard Hot 100? ")
    if guess.lower() == number1.lower():
        print(f"Correct! {number1} by {artist} is currently #1!")
        break
    else:
        print("Incorrect. Try again!")

if (guess.lower() != number1.lower()):
    print(f"The correct answer is {number1} by {artist}. You'll get it next time!")

time.sleep(2)
os.system('cls')
print("Thanks for playing!")
