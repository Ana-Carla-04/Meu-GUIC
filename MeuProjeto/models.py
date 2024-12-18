from MeuProjeto import banco_dados





class Usuario(banco_dados.Model):
    __tablename__ = 'USUARIO'

    Matricula = banco_dados.Column(banco_dados.String(14), primary_key=True, nullable=False, autoincrement=False)
    Nome = banco_dados.Column(banco_dados.String(50), nullable=False )
    Tipo = banco_dados.Column(banco_dados.Enum('Aluno', 'Servidor'), nullable=False)
    Senha = banco_dados.Column(banco_dados.String(50), nullable=False)



class Setores(banco_dados.Model):
    __tablename__ = 'SETORES'
    

    ID_setor = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_setor = banco_dados.Column(banco_dados.String(255))
    Responsavel_setor = banco_dados.Column(banco_dados.String(255))
    Descricao_setor = banco_dados.Column(banco_dados.String(3000))
    Contato_email = banco_dados.Column(banco_dados.String(255))
    Contato_numero = banco_dados.Column(banco_dados.Integer)
    Imagens_setor = banco_dados.Column(banco_dados.LargeBinary)


class Eventos(banco_dados.Model):
    __tablename__ = 'EVENTOS'


    ID_evento = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_evento = banco_dados.Column(banco_dados.String(255))
    Data_evento = banco_dados.Column(banco_dados.Date)
    Descricao_evento = banco_dados.Column(banco_dados.String(3000))
    Responsaveis_evento = banco_dados.Column(banco_dados.String(255))
    local = banco_dados.Column(banco_dados.String(255))
    Imagens_evento = banco_dados.Column(banco_dados.LargeBinary)


class MaterialApoio(banco_dados.Model):
    __tablename__ = 'MATERIAL_APOIO'


    ID_arquivo = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_arquivo = banco_dados.Column(banco_dados.String(255))
    Quantidade_download = banco_dados.Column(banco_dados.Integer)
    Data_download = banco_dados.Column(banco_dados.Date)
    Arquivo_pdf = banco_dados.Column(banco_dados.LargeBinary)
    Usuario_mat_download = banco_dados.Column(banco_dados.String(14), banco_dados.ForeignKey('USUARIO.Matricula'))


class Avaliacao(banco_dados.Model):
    __tablename__ = 'AVALIACAO'


    ID_feedback = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Sugestao = banco_dados.Column(banco_dados.String(1000))
    Estrelas = banco_dados.Column(banco_dados.Integer, unique=True)
    Data_feedback = banco_dados.Column(banco_dados.Date)
    Usuario_mat_avaliacao = banco_dados.Column(banco_dados.String(14), banco_dados.ForeignKey('USUARIO.Matricula'))



