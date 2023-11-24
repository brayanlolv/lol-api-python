import requests
import json


chave_riot =  "RGAPI-e2542b42-9e49-41f0-b4a0-4dea9665562a"
#get_chall_url = "https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I"
get_chall_url = "https://br1.api.riotgames.com/lol/league/v4/leagues/9468e29a-a085-3ab8-8d19-d25cc8630618"

get_grandmaster_url = "https://br1.api.riotgames.com/lol/league/v4/leagues/3a2adce0-034f-3252-adf2-a1c5529bd748"

get_masters_url = "https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"


def create_challengers_json():
    chall_arch = open("data/overall/challengers.json","w",encoding="utf-8")
    result = requests.get(get_chall_url,headers={ "X-Riot-Token":chave_riot})    
    chall_arch.write(result.text)
    
def create_grandmasters_json():
    chall_arch = open("data/overall/grandmasters.json","w",encoding="utf-8")
    result = requests.get(get_grandmaster_url,headers={ "X-Riot-Token":chave_riot})    
    chall_arch.write(result.text)
    
def create_masters_json():
    chall_arch = open("data/overall/masters.json","w",encoding="utf-8")
    result = requests.get(get_masters_url,headers={ "X-Riot-Token":chave_riot})    
    chall_arch.write(result.text)