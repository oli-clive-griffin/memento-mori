# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://deaths.dompost.co.nz/obituaries/dominion-post-nz/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for li in soup.findAll('ul', {'class': "recentObitsList"}):
        name = li.text.replace("(Death Notice)", "")
        name = name.replace(", ", ",")
        print(name)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
