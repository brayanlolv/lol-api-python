
from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.EdgeOptions()  
options.add_argument('--ignore-certificate-errors')#
#options.add_argument('--incognito')#
# options.add_argument('--headless')#  
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])#exclui rum erro

def isMono(players):
    result = []
    driver = webdriver.Edge(options=options)
    
    for player in players:
        
        try:
            # driver = webdriver.Edge(options=options)
            urlLOG = "https://www.leagueofgraphs.com/pt/summoner/br/{}-br1".format(player["summonerName"])
            driver.get(urlLOG)
            time.sleep(0.7)# temq ver se nao vai dar pau
            soup = BeautifulSoup(driver.page_source, 'lxml')
            # olhar se nao pode ser mais rapido deixa lo aberto até o final
            soup = soup.find("body")
            teste = soup.find_all("div",class_="content active",attrs={ "data-tab-id":"championsData-soloqueue"},limit=2 )
            tr = teste[1].find_all("tr",limit=2)

            # total_losses = float(soup.find("span",class_="lossesNumber").string)
            # total_wins = float(soup.find("span",class_="winsNumber").string)
            total_losses = player["losses"]
            total_wins = player["wins"]
            number_champ_games = float(tr[1].find("div",class_="progressBarTxt").string)
            otp = number_champ_games >= (total_losses + total_wins ) /2
            most_played_champ = tr[1].find("div",class_="name").string
            most_played_champ = most_played_champ.lower()
            most_played_champ = most_played_champ.replace(" ","")
            most_played_champ = most_played_champ.replace("'","")
            # driver.close()

            if(not otp):
                continue
          
            player_overall = {
            "name":player["summonerName"],
            "champ":most_played_champ,
            "champ_games":number_champ_games,
            "total_wins":total_wins,
            "total_losses":total_losses,
            "total_games": (total_wins+total_losses),
            "pdl":player["leaguePoints"]
            }
            
          
            
            print(player_overall)
            result.append(player_overall)

        except:
            continue
    
    driver.close()

    return result
    











