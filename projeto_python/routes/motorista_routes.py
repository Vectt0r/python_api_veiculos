from flask import Blueprint, jsonify, request
from models.motorista import Motorista
from database import db

motorista_bp = Blueprint('motoristas_cadastados', __name__)

@motorista_bp.route('/motoristas', methods=['GET'])
def get_motoristas():
    motoristas = Motorista.query.all()
    resultado = [{'id': m.id, 'nome': m.nome, 'idade': m.idade} for m in motoristas]
    return jsonify(resultado)

@motorista_bp.route('/motoristas', methods=['POST'])
def add_motorista():
    data = request.json
    novo_motorista = Motorista(nome=data['nome'], idade=data['idade'])
    db.session.add(novo_motorista)
    db.session.commit()
    return jsonify({'message': 'Motorista adicionado com sucesso!'})
