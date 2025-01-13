from flask import Flask, render_template,request, session, redirect, flash, jsonify
import requests
import json
from datetime import datetime 

from MeuProjeto import app, banco_dados
from MeuProjeto.models import *



app.secret_key = 'napoleao'

# URL da API SUAP
SUAP_TOKEN_URL = 'https://suap.ifrn.edu.br/api/v2/autenticacao/token/'
SUAP_INFO_URL = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'


# @app.route('/')
# def login():
#     return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def suap_login():
#     matricula = request.form['matricula']
#     senha = request.form['senha']

#     print("print 1")

#     # Autenticação no SUAP via API
#     payload = json.dumps({'username': matricula, 'password': senha})
#     headers = {'Content-Type': 'application/json'}

#     print("print 2")

#     # Enviando a requisição de autenticação
#     response = requests.post(SUAP_TOKEN_URL, data=payload, headers=headers)
#     data = response.json()

#     print("print 3")

#     # Se o token de acesso for retornado
#     if response.status_code == 200 and 'access' in data:
#         token_acesso = data['access']
        
#         # Armazenando o token na sessão
#         session['token_acesso'] = token_acesso

#         # Fazendo uma nova requisição para obter os dados do usuário
#         headers = {'Authorization': f'Bearer {token_acesso}'}
#         user_response = requests.get(SUAP_INFO_URL, headers=headers)
#         user_data = user_response.json()
#         print("print 4")

#         if user_response.status_code == 200:
#             nome_usuario = user_data['nome_usual']
#             matricula_usuario = user_data['matricula']
#             tipo_vinculo = user_data['tipo_vinculo']
            
#             # Armazenando as informações do usuário na sessão
#             session['nome_usuario'] = nome_usuario
#             session['matricula_usuario'] = matricula_usuario
#             session['tipo_vinculo'] = tipo_vinculo

#             print("print 5")

#             # Verifica se o usuário já existe no banco de dados
#             usuario = Usuario.query.filter_by(Matricula=matricula_usuario).first()
#             print(tipo_vinculo)
#             if not usuario:
#                 # Se o usuário não existir, cria um novo registro no banco
                
#                 novo_usuario = Usuario(
#                     Matricula=matricula_usuario,
#                     Nome=nome_usuario,
#                     Tipo=tipo_vinculo,
#                     Senha=senha  # Aqui você pode criptografar a senha, se necessário
#                 )
#                 banco_dados.session.add(novo_usuario)
#                 banco_dados.session.commit()
#                 print("print 6")


            
#             # Verifica se é um aluno, servidor ou prestador de serviço
#             if tipo_vinculo in ["Prestador de Serviço", "Aluno", "Servidor"]:
#                 print("deu certo")
#                 flash(f'Olá, {nome_usuario}! Seja bem-vindo ao sistema.', 'success')
#                 return redirect('/homepage')
                
#             else:
#                 flash('Você não tem permissão para acessar o sistema.', 'error')
#                 print("deu errado")
#                 return redirect('/')
#         else:
#             flash('Erro ao buscar informações do usuário.', 'error')
#             return redirect('/')
#     else:
#         # Credenciais inválidas
#         flash('Matrícula ou senha incorretas.', 'error')
#         return redirect('/')

@app.route('/homepage')
def homepage():
    # Página protegida, acessível somente para usuários autorizados
    if 'token_acesso' not in session:
        flash('Você precisa fazer login primeiro.', 'error')
        return redirect('/')
    return render_template('homepage.html')

# Rota para processar a avaliação (POST)
@app.route('/avaliacao', methods=['POST'])
def avaliacao():
    sugestao = request.form.get('avaliacao')  # Obtém o valor do campo de texto
    estrelas = request.form.get('estrelas')  # Obtém o valor das estrelas (selecionado pelo usuário)

    # Cria uma nova avaliação
    nova_avaliacao = Avaliacao(
        Sugestao=sugestao,
        Estrelas=int(estrelas),
        Data_feedback=datetime.now()  # A data atual é atribuída
    )

    # Adiciona a avaliação no banco de dados e faz o commit
    banco_dados.session.add(nova_avaliacao)
    banco_dados.session.commit()

    return "Avaliação enviada com sucesso!"  # Você pode redirecionar para uma nova página ou exibir uma mensagem de sucesso



@app.route('/eventos')
def eventos():
    return render_template ('eventos.html')

@app.route('/setores')
def setores():
    return render_template ('setores.html')

@app.route('/material')
def material():
    return render_template ('material.html')


# setores


# setores

@app.route('/auditorio')
def auditorio():
    return render_template ('/setores_templates/auditorio.html')

@app.route('/almoxarifado')
def almoxarifado():
    return render_template ('/setores_templates/almoxarifado.html')

@app.route('/biblioteca')
def biblioteca():
    return render_template ('/setores_templates/biblioteca.html')

@app.route('/coapac')
def coapac():
    return render_template ('/setores_templates/coapac.html')

@app.route('/CED')
def CED():
    return render_template ('/setores_templates/CED.html')

@app.route('/CE')
def CE():
    return render_template ('/setores_templates/CE.html')

@app.route('/Cood_pesquisa')
def CE():
    return render_template ('/setores_templates/coord_pesquisa.html')

@app.route('/ETEP')
def ETEP():
    return render_template ('/setores_templates/ETEP.html')

@app.route('/GREMIO')
def ETEP():
    return render_template ('/setores_templates/gremio.html')

@app.route('/miniauditorio')
def miniauditorio():
    return render_template ('/setores_templates/miniauditorio.html')

@app.route('/licenciatura_quimica')
def miniauditorio():
    return render_template ('/setores_templates/licenc_quim.html')

@app.route('/NAPNE')
def NAPNE():
    return render_template ('/setores_templates/NAPNE.html')

@app.route('/NEABI')
def NEABI():
    return render_template ('/setores_templates/NEABI.html')

@app.route('/NULIC')
def NULIC():
    return render_template ('/setores_templates/NULIC.html')

@app.route('/psicologia')
def psicologia():
    return render_template ('/setores_templates/psicologia.html')

@app.route('/secretaria_academica')
def servico_social():
    return render_template ('/setores_templates/secret_academica.html')

@app.route('/setor_saude')
def setor_saude():
    return render_template ('/setores_templates/setor_saude.html')

@app.route('/TI')
def TI():
    return render_template ('/setores_templates/TI.html')




# eventos

@app.route('/eventos/ENQUICAP')
def ENQUICAP():
    return render_template ('/eventos_templates/enquicap.html')

@app.route('/eventos/EXPOAP')
def EXPOAP():
    return render_template ('/eventos_templates/expoap.html')

@app.route('/eventos/EXPOTEC')
def EXPOTEC():
    return render_template ('/eventos_templates/expotec.html')

@app.route('/eventos/FEISA')
def FEISA():
    return render_template ('/eventos_templates/feisa.html')

@app.route('/eventos/Informática')
def Informatica():
    return render_template ('/eventos_templates/semana_info.html')

@app.route('/eventos/Intercalouros')
def Intercalouros():
    return render_template ('/eventos_templates/Intercalouros.html')

@app.route('/eventos/linguagens')
def linguagens():
    return render_template ('/eventos_templates/semana_lingua.html')

@app.route('/eventos/SECITEX')
def SECITEX():
    return render_template ('/eventos_templates/secitex.html')

@app.route('/eventos/SEMADEC')
def SEMADEC():
    return render_template ('/eventos_templates/semadec.html')

@app.route('/eventos/START')
def START():
    return render_template ('/eventos_templates/start.html')

@app.route('/eventos/Consciencia_Negra')
def Consciencia_Negra():
    return render_template ('/eventos_templates/consciencia_negra.html')

if __name__ == '__main__':
    app.run(debug=True)