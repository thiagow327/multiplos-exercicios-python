// Função para consultar todos os veículos
function consultarVeiculos() {
    fetch("http://localhost:8080/veiculos")
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("consultaResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na consulta: ", error));
}

// Função para filtrar veículos
function filtrarVeiculos() {
    const marca = document.getElementById("marca").value;
    const ano = document.getElementById("ano").value;
    const cor = document.getElementById("cor").value;

    const params = new URLSearchParams({
        marca: marca,
        ano: ano,
        cor: cor,
    });

    fetch(`http://localhost:8080/veiculos/filtrar?${params}`)
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("filtragemResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na filtragem: ", error));
}

// Função para consultar os detalhes de um veículo
function consultarDetalhesVeiculo() {
    const id = document.getElementById("idDetalhes").value;

    fetch(`http://localhost:8080/veiculos/${id}`)
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("detalhesResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na consulta de detalhes: ", error));
}

// Função para cadastrar um novo veículo
function cadastrarVeiculo() {
    const veiculo = document.getElementById("veiculo").value;
    const marca = document.getElementById("novaMarca").value;
    const ano = document.getElementById("novoAno").value;
    const cor = document.getElementById("novaCor").value;
    const descricao = document.getElementById("descricao").value;

    fetch("http://localhost:8080/veiculos")
        .then((response) => response.json())
        .then((veiculosCadastrados) => {
            const proximoId = obterProximoId(veiculosCadastrados);

            const novoVeiculo = {
                id: proximoId,
                veiculo: veiculo,
                marca: marca,
                ano: parseInt(ano),
                cor: cor,
                descricao: descricao,
                vendido: false,
            };

            fetch("http://localhost:8080/veiculos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(novoVeiculo),
            })
                .then((response) => response.json())
                .then((data) => {
                    const resultado = document.getElementById("cadastroResultado");
                    resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
                })
                .catch((error) => console.error("Erro no cadastro: ", error));
        })
        .catch((error) => console.error("Erro ao obter veículos cadastrados: ", error));
}

// Função para atualizar um veículo
function atualizarVeiculo() {
    const id = document.getElementById("idAtualizacao").value;
    const marca = document.getElementById("marcaAtualizacao").value;
    const veiculo = document.getElementById("veiculoAtualizacao").value;
    const ano = document.getElementById("anoAtualizacao").value;
    const cor = document.getElementById("corAtualizacao").value;
    const descricao = document.getElementById("descricaoAtualizacao").value; // Adicionado para capturar o valor da descrição

    const veiculoAtualizado = {
        marca: marca,
        veiculo: veiculo,
        ano: ano,
        cor: cor,
        descricao: descricao // Incluído o campo descrição no objeto veiculoAtualizado
    };

    fetch(`http://localhost:8080/veiculos/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(veiculoAtualizado),
    })
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("atualizacaoResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na atualização: ", error));
}

function atualizarCampoVendido() {
    const id = document.getElementById("idVendido").value;
    const vendido = document.getElementById("vendido").value === "True";

    const veiculoAtualizado = {
        vendido: vendido,
    };

    fetch(`http://localhost:8080/veiculos/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(veiculoAtualizado),
    })
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("campoVendidoResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na atualização do campo 'vendido': ", error));
}

// Função para excluir um veículo
function excluirVeiculo() {
    const id = document.getElementById("idExclusao").value;

    fetch(`http://localhost:8080/veiculos/${id}`, {
        method: "DELETE",
    })
        .then((response) => response.json())
        .then((data) => {
            const resultado = document.getElementById("exclusaoResultado");
            resultado.innerHTML = "<pre class='json-response'>" + JSON.stringify(data, null, 2) + "</pre>";
        })
        .catch((error) => console.error("Erro na exclusão: ", error));
}

// Função para limpar os resultados
function limparResultados() {
    document.getElementById("consultaResultado").innerHTML = "";
    document.getElementById("filtragemResultado").innerHTML = "";
    document.getElementById("cadastroResultado").innerHTML = "";
    document.getElementById("atualizacaoResultado").innerHTML = "";
    document.getElementById("exclusaoResultado").innerHTML = "";
}

// Função para obter o próximo ID sequencial com base nos veículos cadastrados
function obterProximoId(veiculosCadastrados) {
    let maxId = 0;
    veiculosCadastrados.forEach((veiculo) => {
        if (veiculo.id > maxId) {
            maxId = veiculo.id;
        }
    });
    return maxId + 1;
}

// Vinculando eventos aos botões
document.getElementById("consultarBtn").addEventListener("click", consultarVeiculos);
document.getElementById("filtrarBtn").addEventListener("click", filtrarVeiculos);
document.getElementById("cadastrarBtn").addEventListener("click", cadastrarVeiculo);
document.getElementById("atualizarBtn").addEventListener("click", atualizarVeiculo);
document.getElementById("excluirBtn").addEventListener("click", excluirVeiculo);
document.getElementById("limparBtn").addEventListener("click", limparResultados);
