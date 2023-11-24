import json
from operator import itemgetter

def find_by_champion(array,champ_name):
    result = []
    for player in array:
        if(player["champ"]==champ_name):
            result.append(player)
    
    
    return result
    

def load_monos(ranks,name):
    result = []
    challengers_mono = open("data/mono/monochall.json")
    challengers_mono = challengers_mono.read()
    challengers_mono_obj = json.loads(challengers_mono)
    # challengers_mono.close()
        
    result.append(find_by_champion(challengers_mono_obj,name))

    if(ranks > 1):
        grandmasters_mono = open("data/mono/mono_grandmaster.json")
        grandmasters_mono = grandmasters_mono.read()
        grandmasters_mono_obj = json.loads(grandmasters_mono)
        # grandmasters_mono.close()
    
        result.append(find_by_champion(grandmasters_mono_obj,name))
    
    if(ranks > 2):
        masters_mono = open("data/mono/mono_master.json")
        masters_mono = masters_mono.read()
        masters_mono_obj = json.loads(masters_mono)
        # masters_mono.close()  
        
        result.append(find_by_champion( masters_mono_obj,name))
    
    return result



def find_by_rank(number):

    if(number == 3):
        file = open("data/mono/mono_master.json","r")
        
    if(number == 2):
        file = open("data/mono/mono_grandmaster.json","r")
        
    if(number == 1):
        file = open("data/mono/monochall.json","r")
        
    file = file.read()
    file = json.loads(file)
    return sorted(file,key=itemgetter("pdl"))
    