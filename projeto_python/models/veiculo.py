from database import db

class Veiculo(db.Model):
    __tablename__ = 'veiculos_cadastrados'
    id = db.Column(db.Integer, primary_key=True)
    nome_veiculo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
