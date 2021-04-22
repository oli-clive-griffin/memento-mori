from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

if __name__ == '__main__':
    print("Looking")
    url = "https://deaths.dompost.co.nz/obituaries/dominion-post-nz/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for li in soup.findAll('ul', {'class': "recentObitsList"}):
        name = li.text.replace("(Death Notice)", "")
        name = name.replace(", ", ",")
        print(name)

