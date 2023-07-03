import pytest
from app import atualizar_campo_vendido_veiculo


def test_atualizar_campo_vendido_veiculo():
    # Caso de teste 1: Verificar se a função atualiza corretamente o campo "vendido" de um veículo existente
    veiculo_alterado = {
        "vendido": True,
    }
    result = atualizar_campo_vendido_veiculo(1, veiculo_alterado)
    assert result["vendido"] == True

    # Caso de teste 2: Verificar se a função retorna None ao tentar atualizar o campo "vendido" de um veículo inexistente
    veiculo_alterado = {
        "vendido": True,
    }
    result = atualizar_campo_vendido_veiculo(100, veiculo_alterado)
    assert result is None
