class Eleicao:
    def __init__(self, total_eleitores, votos_validos, votos_brancos, votos_nulos):
        self.total_eleitores = total_eleitores
        self.votos_validos = votos_validos
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos

    def percentual_validos(self):
        return (self.votos_validos / self.total_eleitores) * 100

    def percentual_brancos(self):
        return (self.votos_brancos / self.total_eleitores) * 100

    def percentual_nulos(self):
        return (self.votos_nulos / self.total_eleitores) * 100


# Dados fornecidos
eleicao = Eleicao(1000, 800, 150, 50)

# Calculando os percentuais
percentual_validos = eleicao.percentual_validos()
percentual_brancos = eleicao.percentual_brancos()
percentual_nulos = eleicao.percentual_nulos()

# Impressão dos resultados
print(f"Cálculo de percentuais:")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
