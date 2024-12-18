from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)



# Criar engine para se conectar ao MySQL
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost')
 # Conectar ao banco e criar o banco de dados, se necessário
with engine.connect() as conn:
        conn.execute(sqlalchemy.text("CREATE DATABASE IF NOT EXISTS MeuGUIC"))




# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/MeuGUIC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações do SQLAlchemy

# Inicialize o SQLAlchemy
banco_dados = SQLAlchemy(app)


# Importando os modelos após a inicialização do banco de dados
from MeuProjeto import models
from MeuProjeto import routes
from MeuProjeto import *




with app.app_context():
    banco_dados.create_all()  # Cria todas as tabelas definidas nos modelos
    print("Banco de dados e tabelas criados com sucesso!")
