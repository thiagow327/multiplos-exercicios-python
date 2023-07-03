import pytest
from app import consulta_veiculos


def test_consulta_veiculos():
    # Caso de teste 1: Verificar se a função retorna uma lista de veículos
    result = consulta_veiculos()
    assert isinstance(result, list)

    # Caso de teste 2: Verificar se a lista de veículos não está vazia
    result = consulta_veiculos()
    assert len(result) > 0

    # Caso de teste 3: Verificar se a lista de veículos contém os atributos esperados
    result = consulta_veiculos()
    assert all(
        "id" in veiculo
        and "veiculo" in veiculo
        and "marca" in veiculo
        and "ano" in veiculo
        and "cor" in veiculo
        and "descricao" in veiculo
        and "vendido" in veiculo
        and "created" in veiculo
        and "updated" in veiculo
        for veiculo in result
    )
