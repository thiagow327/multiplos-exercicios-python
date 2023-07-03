import pytest
from app import atualizar_veiculo, consulta_detalhes_de_um_veiculo
from datetime import datetime

def test_atualizar_veiculo():
    # Caso de teste 1: Verificar se a função atualiza os dados corretamente para um veículo existente
    veiculo_alterado = {
        "veiculo": "Carro",
        "marca": "Tesla",
        "ano": 2023,
        "cor": "Branco",
        "descricao": "Carro elétrico",
        "vendido": False,
        "updated": datetime.now(),
    }
    atualizar_veiculo(1, veiculo_alterado)
    result = consulta_detalhes_de_um_veiculo(1)
    assert result["ano"] == 2023
    assert result["cor"] == "Branco"

    # Caso de teste 2: Verificar se a função retorna None ao tentar atualizar um veículo inexistente
    veiculo_alterado = {
        "veiculo": "Carro",
        "marca": "Tesla",
        "ano": 2023,
        "cor": "Branco",
        "descricao": "Carro elétrico",
        "vendido": False,
        "updated": datetime.now(),
    }
    result = atualizar_veiculo(100, veiculo_alterado)
    assert result is None