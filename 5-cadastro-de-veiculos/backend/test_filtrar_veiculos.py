import pytest
from app import filtrar_veiculos


def test_filtrar_veiculos():
    # Caso de teste 1: Verificar se a função retorna uma lista de veículos filtrados corretamente
    result = filtrar_veiculos(marca="Tesla", ano=2022, cor="Prata")
    assert isinstance(result, list)

    # Caso de teste 2: Verificar se a lista de veículos filtrados contém apenas veículos que atendem aos critérios
    result = filtrar_veiculos(marca="Tesla", ano=2022, cor="Prata")
    assert all(
        veiculo["marca"] == "Tesla"
        and veiculo["ano"] == 2022
        and veiculo["cor"] == "Prata"
        for veiculo in result
    )

    # Caso de teste 3: Verificar se a função retorna uma lista vazia quando nenhum veículo atende aos critérios
    result = filtrar_veiculos(marca="Toyota", ano=2022, cor="Azul")
    assert len(result) == 0
