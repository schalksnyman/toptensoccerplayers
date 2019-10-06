from bs4 import BeautifulSoup
import requests
import lxml

base_url = "https://naijaquest.com/best-football-players-in-the-world"

# Send get HTTP request
page = requests.get(base_url)
print(type(page))
print(page.status_code)

# Verify we had a successful get request webpage call
if page.status_code == requests.codes.ok:

  # Get the whole webpage in beautiful soup format
  bs = BeautifulSoup(page.text, 'lxml')

  # Find the list of players
  list_of_all_players = bs.find('div', class_='entry-content').find_all('ul')
  top_ten_players = list_of_all_players[:10]
  #print(top_ten_players)

  # Hold the scraped data
  data = {
    'Rank': [],
    'Country': [],
    'Player': [],
    'Team': []
  }

player = top_ten_players[0]
rank = player.find('strong').text.split('.')[0]
country = player.find('strong').text.split('–')[-1].strip()

print(country)