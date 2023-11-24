import json
from funcs.getLOF import isMono

def get_all_mono(json_players,json_result):
    
        print("all mono")
        all_challengers = open(json_players,"r",encoding="utf-8")
        all_challengers = all_challengers.read() 
        all_challengers_obj = json.loads(all_challengers) # troquei o mono chall
             
        result = isMono(all_challengers_obj["entries"])
    
        print("result")
        print(result)
        chall_arch_j = open(json_result,"w",encoding="utf-8")
        chall_arch_j.write(json.dumps(result))
        chall_arch_j.close()