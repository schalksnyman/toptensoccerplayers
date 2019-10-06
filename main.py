from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = "https://naijaquest.com/best-football-players-in-the-world"

# Send get HTTP request
page = requests.get(base_url)
# print(type(page))
# print(page.status_code)

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
    'Country': [],
    'Name': [],
    'Team': []
  }

  # Scrape all ten players in the top ten list
  for player in top_ten_players:
    tidy_player_text_list = player.find('strong').text.replace('-','').replace('–','').replace('—','').split()
    # print(tidy_player_text_list)
    # rank = tidy_player_text_list[0].split('.')[0]
    # if rank:
    #   data['Rank'].append(rank)
    # else:
    #   data['Rank'].append('none')
    # print(rank)
    country = tidy_player_text_list[-1]
    # Fix bad data
    if country == "Englan":
      country = "England"
    if country:
      data['Country'].append(country)
    else:
      data['Country'].append('none')
    # print(country)
    if tidy_player_text_list[2].lower() == "van" and tidy_player_text_list[3].lower() == "der":
      name = tidy_player_text_list[1] + " " + tidy_player_text_list[2] + " " + tidy_player_text_list[3] + " " + tidy_player_text_list[4]
    elif tidy_player_text_list[2].lower() == "van" and tidy_player_text_list[3].lower() != "der":
      name = tidy_player_text_list[1] + " " + tidy_player_text_list[2] + " " + tidy_player_text_list[3]
    else:
      name = tidy_player_text_list[1] + " " + tidy_player_text_list[2]
    if name:
      data['Name'].append(name)
    else:
      data['Name'].append('none')
    # print(name)
    team = tidy_player_text_list[3]
    if tidy_player_text_list[3] not in name and tidy_player_text_list[3] not in country:
      team = tidy_player_text_list[3]
      if tidy_player_text_list[4] not in name and tidy_player_text_list[4] not in country:
        team = team + " " + tidy_player_text_list[4]
        if tidy_player_text_list[5] not in name and tidy_player_text_list[5] not in country:
          team = team + " " + tidy_player_text_list[5]
    else:
      team = tidy_player_text_list[4]
      if tidy_player_text_list[5] not in name and tidy_player_text_list[5] not in country:
        team = team + " " + tidy_player_text_list[5]
    if team:
      data['Team'].append(team)
    else:
      data['Team'].append('none')
    # print(team)

  table = pd.DataFrame(data, columns=['Country', 'Name', 'Team'])
  table.index = table.index + 1
  print(table)
  table.to_csv('players_of_the_year.csv', sep=',', index=False, encoding='utf-8')