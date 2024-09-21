from flask import Blueprint, jsonify, request
from models.veiculo import Veiculo
from database import db

veiculo_bp = Blueprint('veiculo', __name__)

# ROTAS BASICAS DELETAR - ATUALIZAR - LISTAR - ADICIONAR

# Listar todos os veiculos cadastrados no banco de dados
@veiculo_bp.route('/ListarVeiculos', methods=['GET'])
def get_veiculos():
    veiculos = Veiculo.query.all()
    resultado = [{'id': v.id, 'nome_veiculo': v.nome_veiculo, 'placa': v.placa,'modelo': v.modelo, 'status': v.status} for v in veiculos]
    return jsonify(resultado)

# Recuprar um veiculo especifico atraves do id
@veiculo_bp.route('/BuscarVeiculo/<int:id>', methods=['GET'])
def get_veiculo(id):
    veiculo = Veiculo.query.get(id)
    if veiculo:
        resultado = [{'id': veiculo.id, 'nome_veiculo': veiculo.nome_veiculo, 'placa': veiculo.placa,'modelo': veiculo.modelo, 'status': v.status}]
        return jsonify(resultado)
    else:
        return jsonify('Veiculo não encontrado')

# Deletar um veiculo
@veiculo_bp.route("/DeletarVeiculo/<id>", methods=["DELETE"])
def delete_veiculo(id):
    veiculo = Veiculo.query.get(id)
    db.session.delete(veiculo)
    db.session.commit()
    return jsonify('Veiculo deletado com Sucesso')

# Atualizar um veiculo
@veiculo_bp.route('/AtualizarVeiculo', methods=['PUT'])
def update_veiculo(id):
    veiculo = Veiculo.query.get(id)
    if veiculo:
        data = request.json
        veiculo.nome_veiculo = data.get('nome_veiculo', veiculo.nome_veiculo)
        veiculo.placa = data.get('placa', veiculo.placa)
        veiculo.modelo = data.get('modelo', veiculo.modelo)

        db.session.commit()
        return jsonify({'message': 'Veículo atualizado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Veículo não encontrado'}), 404

# Adicionar um veiculo
@veiculo_bp.route('/AdicionarVeiculo', methods=['POST'])
def add_veiculo():
    data = request.json
    novo_veiculo = Veiculo(nome_veiculo=data['nome_veiculo'], placa=data['placa'], modelo=data['modelo'], status=data[status])
    db.session.add(novo_veiculo)
    db.session.commit()
    return jsonify({'message': 'Veículo adicionado com sucesso!'})
