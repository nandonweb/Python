import pandas as pd
from json import loads
import requests
from flask import Flask

# Perfis para teste / plataformas diferentes
# Nando = Nando%239723462 / acti
# Mark = ImpMark%231470 / battle
# Xbox = mrkuttfaeva / xbl
# Play = death_from_ab007 / psn

gamertag = "Nando%239723462"
plataform = "acti"

#url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/"+str(gamertag)"/"+str(plataform)"

url = f'https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/{gamertag}/{plataform}'

headers = {
	"X-RapidAPI-Key": "b312896511msh558e357260d169fp12e5a5jsn2d5a36be5710",
	"X-RapidAPI-Host": "call-of-duty-modern-warfare.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

meujson = loads(response.text)
playerinfo = loads(response.text)

meujson = meujson['matches']
playerinfo = playerinfo['matches']

# Ultima Partida
meujson = meujson[int('0')]
playerinfo = playerinfo[int('0')]
playerinfo = playerinfo['playerStats']

# Paramentros
matchid = meujson['matchID']
modo = meujson['mode']

kills = playerinfo['kills']
kd_ratio = playerinfo['kdRatio']
headshots = playerinfo['headshots']
deaths = playerinfo['deaths']
assists = playerinfo['assists']
dano = playerinfo['damageDone']
danorece = playerinfo['damageTaken']
tempo = playerinfo['timePlayed']
posicaotime = playerinfo['teamPlacement']


df = pd.DataFrame({'Ultima Partida': ['Match ID', 'Modo', 'Matou' , 'KDR', 'Headshots', 'Morreu', 'Assistencias', 'Dano Feito', 'Dano Recebido', 'Tempo da Partida', 'Posição do Time'],
'Informacoes': [matchid, modo, kills, kd_ratio, headshots, deaths, assists, dano, danorece, tempo, posicaotime]})

df.loc[df['Informacoes'] == 'br_rebirth_playlist_wz340/fortkeep_res_quad'] = 'Squad'
df.loc[df['Informacoes'] == 'br_rebirth_playlist_wz340/fortkeep_res_trios'] = 'Trios'
df.loc[df['Informacoes'] == 'br_rebirth_playlist_wz340/fortkeep_res_duos'] = 'Duplas'
df.loc[df['Informacoes'] == 'br_rebirth_playlist_wz340/fortkeep_res_solo'] = 'Solo'


app = Flask(__name__)

@app.route('/')
def tabela():
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)