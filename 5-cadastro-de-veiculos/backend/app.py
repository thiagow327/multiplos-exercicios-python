from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

veiculos = [
    {
        "id": 1,
        "veiculo": "Carro",
        "marca": "Tesla",
        "ano": 2022,
        "cor": "Prata",
        "descricao": "Carro elétrico",
        "vendido": False,
        "created": datetime.now(),
        "updated": datetime.now(),
    },
    {
        "id": 2,
        "veiculo": "Caminhonete",
        "marca": "Ford",
        "ano": 2002,
        "cor": "Azul",
        "descricao": "SUV",
        "vendido": True,
        "created": datetime.now(),
        "updated": datetime.now(),
    },
]

marcas = [
    "Toyota",
    "Volkswagen",
    "Ford",
    "Chevrolet",
    "Honda",
    "Nissan",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Hyundai",
    "Kia",
    "Volvo",
    "Tesla",
    "Ferrari",
    "Lamborghini",
    "Porsche",
    "Maserati",
    "Subaru",
    "Jeep",
    "Land Rover",
]


@app.route("/")
def index():
    return render_template("/frontend/index.html")


# Retorna todos os veículos
@app.route("/veiculos", methods=["GET"])
def consulta_veiculos():
    return jsonify(veiculos)


# Retorna todos os veículos de acordo com os parâmetros passados (marca, ano e cor)
@app.route("/veiculos/filtrar", methods=["GET"])
def filtrar_veiculos():
    marca = request.args.get("marca")
    ano = request.args.get("ano")
    cor = request.args.get("cor")

    veiculos_filtrados = veiculos

    if marca:
        veiculos_filtrados = [
            veiculo for veiculo in veiculos_filtrados if veiculo.get("marca") == marca
        ]
    if ano:
        veiculos_filtrados = [
            veiculo for veiculo in veiculos_filtrados if veiculo.get("ano") == int(ano)
        ]
    if cor:
        veiculos_filtrados = [
            veiculo for veiculo in veiculos_filtrados if veiculo.get("cor") == cor
        ]
    return jsonify(veiculos_filtrados)


# Retorna os detalhes do veículo
@app.route("/veiculos/<int:id>", methods=["GET"])
def consulta_detalhes_de_um_veiculo(id):
    veiculo = next((veiculo for veiculo in veiculos if veiculo.get("id") == id), None)
    if veiculo:
        return jsonify(veiculo)
    else:
        return jsonify({"message": "Veiculo nao encontrado"})


# Adiciona um novo veículo
@app.route("/veiculos", methods=["POST"])
def cadastrar_veiculo():
    novo_veiculo = request.get_json()
    marca = novo_veiculo.get("marca")
    if marca not in marcas:
        return jsonify({"error": "Marca de veículo inválida"}), 400
    novo_veiculo["created"] = datetime.now()
    novo_veiculo["updated"] = datetime.now()
    veiculos.append(novo_veiculo)
    return jsonify(novo_veiculo)


# Atualiza os dados de um veículo
@app.route("/veiculos/<int:id>", methods=["PUT"])
def atualizar_veiculo(id):
    veiculo_alterado = request.get_json()
    for indice, veiculo in enumerate(veiculos):
        if veiculo.get("id") == id:
            veiculo_alterado["updated"] = datetime.now()
            veiculos[indice].update(veiculo_alterado)
            return jsonify(veiculos[indice])
    return jsonify({"message": "Veiculo nao encontrado"})


# Atualiza apenas o campo vendido
@app.route("/veiculos/vendido/<int:id>", methods=["PUT"])
def atualizar_campo_vendido_veiculo(id):
    veiculo_alterado = request.get_json()
    for indice, veiculo in enumerate(veiculos):
        if veiculo.get("id") == id:
            if len(veiculo_alterado) != 1 or "vendido" not in veiculo_alterado:
                return (
                    jsonify({"error": "Somente o campo 'vendido' pode ser alterado"}),
                    400,
                )
            veiculo["vendido"] = veiculo_alterado["vendido"]
            veiculo["updated"] = datetime.now()
            return jsonify(veiculos[indice])
    return jsonify({"message": "Veiculo nao encontrado"})


# Apaga o veículo
@app.route("/veiculos/<int:id>", methods=["DELETE"])
def excluir_veiculo(id):
    for indice, veiculo in enumerate(veiculos):
        if veiculo.get("id") == id:
            del veiculos[indice]
            return jsonify(veiculos)
    return jsonify({"message": "Veiculo nao encontrado"})


if __name__ == "__main__":
    app.run(port=8080, host="localhost", debug=True)

# app.run(port=8080, host="localhost", debug=True)
