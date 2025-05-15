import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchermy.orm import declarative_base, sessionmaker
from tinydb import TinyDB
from datetime import datetime
import time

db = TinyDB('db.json')

def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    responde = requests.get(url)
    return responde.json()
    
def transformar(dados_json):
    valor = dados_json["data"]["amount"]
    cripto = dados_json["data"]["base"]
    moedas = dados_json["data"]["currency"]
    dados_tratados = {
        "valor": valor,
        "cripto": cripto,
        "moedas": moedas,
        "timestamp": datetime.now().isoformat()
        }   
    return dados_tratados

def load(dados_tratados):
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print("Dados inseridos no banco de dados.")

if __name__ == "__main__":
    dados_json = extrair()
    dados_tratados = transformar(dados_json)
    load(dados_tratados)

while True:
    dados_json = extrair()
    dados_tratados = transformar(dados_json)
    load(dados_tratados)
    print("Aguarde 15 segundos para a próxima execução.")
    time.sleep(15)