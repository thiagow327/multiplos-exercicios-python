import pytest
from app import cadastrar_veiculo, consulta_veiculos 
from datetime import datetime


def test_cadastrar_veiculo():
    # Caso de teste 1: Verificar se a função adiciona um novo veículo à lista de veículos
    novo_veiculo = {
        "id": 3,
        "veiculo": "Moto",
        "marca": "Honda",
        "ano": 2021,
        "cor": "Vermelha",
        "descricao": "Motocicleta",
        "vendido": False,
        "created": datetime.now(),
        "updated": datetime.now(),
    }
    cadastrar_veiculo(novo_veiculo)
    result = consulta_veiculos()
    assert len(result) == 3

    # Caso de teste 2: Verificar se o novo veículo adicionado está presente na lista de veículos
    result = consulta_veiculos()
    assert any(veiculo["id"] == 3 for veiculo in result)

    # Caso de teste 3: Verificar se a função retorna um erro ao tentar adicionar um veículo com marca inválida
    novo_veiculo_invalido = {
        "id": 4,
        "veiculo": "Carro",
        "marca": "Fiat",
        "ano": 2021,
        "cor": "Branco",
        "descricao": "Carro popular",
        "vendido": False,
        "created": datetime.now(),
        "updated": datetime.now(),
    }
    with pytest.raises(ValueError):
        cadastrar_veiculo(novo_veiculo_invalido)
