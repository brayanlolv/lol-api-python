from flask import Flask,jsonify,request
from funcs.get_players import create_challengers_json , create_grandmasters_json, create_masters_json
from funcs.get_mono import get_all_mono
from funcs.getLOF import isMono
from funcs.req_functions import find_by_champion, find_by_rank, load_monos
import time
import threading
from threading import Timer



#por o elo e a taxa de vitoria com o mono nos objetos


app = Flask("servidor")


@app.route("/")
def home():
    return "Ola"



@app.route("/get_by_elo")
def get_by_elo():
    rank = request.args.get("rank",default="*",type=str)
    rank = rank.lower() 
    if(rank == "master"):
        return jsonify(find_by_rank(3))
    
    elif(rank == "grandmaster"):
        return jsonify(find_by_rank(2))

    else:       
        return jsonify(find_by_rank(1))


#http://localhost:4000/getchamp?champion=lux&ranks=2
@app.route("/get_by_champ") #polivel
def getChamp():
    selected_ranks = request.args.get("ranks",default=1,type=int)
    just  = request.args.get(0,default=None,type=int)
    champ_name = request.args.get("champion",default="nada_selecionado",type=str)
    champ_name = champ_name.lower()
    
    if(champ_name == "nada_selecionado"):
        return jsonify({"error":"nenhum campeao foi selecionado"})

    result = load_monos(selected_ranks,champ_name)    
    
    if(just == 1):#so challenger
        return jsonify(result[0])
    
    if(just == 2):#so gm
        return jsonify(result[1])
    
    if(just == 3):#so master
        return jsonify(result[2])
    
    return jsonify(result)



def atualizar_informacoes():              
    # create_challengers_json() #colocar um if para so atualizar o json se o codigo for 200
    # create_grandmasters_json()
    # create_masters_json()

    get_all_mono("data/overall/challengers.json","data/mono/monochall.json") 
    get_all_mono("data/overall/grandmasters.json","data/mono/mono_grandmaster.json")
    # get_all_mono("data/overall/masters.json","data/mono/mono_master.json")

def manage_thread():
    rodar = True
    
    while rodar :
        
        thread_filho = threading.Thread(target=atualizar_informacoes)
        thread_filho.start()
        thread_filho.join()
        time.sleep(1*60*60*12)
        # threading.Timer(3,atualizar_informacoes).start()
        
        
    

thread_pai = threading.Thread(target=manage_thread)
thread_pai.start()




app.run(port=4000,host="localhost",
    #debug=True
        debug=False
        )

print("ola")
