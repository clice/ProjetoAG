# Declaração do objeto Arma
class Arma:
    # Construtor de inicialização dos atributos da Arma
    def __init__(self, tipo, pontos_ataque, regiao):
        self.tipo = tipo                    # Nome do tipo da Arma
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Arma
        self.qtd_uso = 3                    # Quantidade de uso restante da Arma
        self.regiao = regiao                # Região (vértice) da Arma no mapa (grafo)

    # String representando as informações sobre a Arma
    def __str__(self):
        print(f"Planta: {self.tipo}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Usos restantes: {self.qtd_uso}")
        print(f"Regiao: {self.regiao}\n")

    # Método para remover a quantidade de uso da Arma
    def remover_qtd_uso(self):
        self.qtd_uso -= 1
