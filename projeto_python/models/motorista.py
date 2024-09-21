from database import db

class Motorista(db.Model):
    __tablename__ = 'motoristas_cadastados'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    #para inteiros nao definir um tamanho
