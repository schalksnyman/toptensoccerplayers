from bs4 import BeautifulSoup
import requests
import lxml

base_url = "https://www.ranker.com/list/best-current-soccer-players/ranker-sports"

# Send get HTTP request
page = requests.get(base_url)
print(type(page))
print(page.status_code)

# Verify we had a successful get request webpage call
if page.status_code == requests.codes.ok:

  # Get the whole webpage in beautiful soup format
  bs = BeautifulSoup(page.text, 'lxml')


