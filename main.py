import os
import requests
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bitcoin.db')

# Corrigir URL do PostgreSQL para o Render
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = 'crypto_prices'
    id = Column(Integer, primary_key=True)
    valor = Column(String)
    cripto = Column(String)
    moedas = Column(String)
    timestamp = Column(DateTime)

def extrair():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        return None

def transformar(dados_json):
    if not dados_json:
        return None
    try:
        return {
            "valor": dados_json["data"]["amount"],
            "cripto": dados_json["data"]["base"],
            "moedas": dados_json["data"]["currency"],
            "timestamp": datetime.now()
        }
    except KeyError as e:
        print(f"Erro ao processar dados: {e}")
        return None

def salvar_dados_sqlalchemy(dados_tratados):
    if not dados_tratados:
        return
    try:
        session = Session()
        crypto_price = CryptoPrice(
            valor=dados_tratados["valor"],
            cripto=dados_tratados["cripto"],
            moedas=dados_tratados["moedas"],
            timestamp=dados_tratados["timestamp"]
        )
        session.add(crypto_price)
        session.commit()
        print("Dados inseridos no banco de dados SQLAlchemy.")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
        session.rollback()
    finally:
        session.close()

@app.route('/')
def index():
    dados_json = extrair()
    dados_tratados = transformar(dados_json)
    if dados_tratados:
        salvar_dados_sqlalchemy(dados_tratados)
        return render_template('index.html', 
                             price=dados_tratados["valor"],
                             cripto=dados_tratados["cripto"],
                             moeda=dados_tratados["moedas"],
                             timestamp=dados_tratados["timestamp"].strftime("%d/%m/%Y %H:%M:%S"))
    return "Erro ao carregar dados", 500

@app.route('/get_price')
def get_price():
    dados_json = extrair()
    dados_tratados = transformar(dados_json)
    if dados_tratados:
        salvar_dados_sqlalchemy(dados_tratados)
        return jsonify(dados_tratados)
    return jsonify({"error": "Falha ao obter preço"}), 500

# Criar tabelas no banco de dados
def init_db():
    try:
        Base.metadata.create_all(engine)
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

# Inicializar banco de dados quando o aplicativo iniciar
init_db()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)