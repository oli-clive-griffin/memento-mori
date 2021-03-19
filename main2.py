# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  url = "https://cinema.thescreeningroom.co.nz/movie/cousins-2021"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  rough = soup.findAll('div', {'class': "movie-details"})
  startprinting = None
  stopprinting = None
  for i in range(len(rough)):
    child = rough[i]
    if child.contents == "<p><i></i></p>":
      startprinting = True
    
    if child.text == "Tweet":
      stopprinting = None

    if startprinting and not stopprinting:
      print(child, "\n")

    print(child, "\n \n")
    # print("startprinting:", startprinting)
    # print("stopprinting:", stopprinting)

  print "________"
  
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
