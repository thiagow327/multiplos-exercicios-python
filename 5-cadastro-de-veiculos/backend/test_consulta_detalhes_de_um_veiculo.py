import pytest
from app import consulta_detalhes_de_um_veiculo

def test_consulta_detalhes_de_um_veiculo():
    # Caso de teste 1: Verificar se a função retorna os detalhes corretos para um veículo existente
    result = consulta_detalhes_de_um_veiculo(1)
    assert isinstance(result, dict)
    assert result["id"] == 1
    assert result["veiculo"] == "Carro"
    assert result["marca"] == "Tesla"
    assert result["ano"] == 2022
    assert result["cor"] == "Prata"

    # Caso de teste 2: Verificar se a função retorna None para um veículo inexistente
    result = consulta_detalhes_de_um_veiculo(100)
    assert result is None