# Declaração do objeto Criatura
class Criatura:
    # Construtor
    def __init__(self, tipo, pontos_vida, pontos_ataque, posicao):
        self.tipo = tipo  # Nome do tipo da Criatura
        self.pontos_vida = pontos_vida  # Pontos de vida da Criatura
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Criatura
        self.posicao = posicao  # Posição da Criatura no mapa (grafo)

    # String representado as informações sobre a Criatura
    def __str__(self):
        print(f"Criatura\n"
              f"Pontos de vida: {self.pontos_vida}\n"
              f"Pontos de ataque: {self.pontos_ataque}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida = self.pontos_vida - pontos

        # Se os pontos de vida da Criatura chegarem a zero
        if self.pontos_vida <= 0:
            print(f"{self.tipo} morreu!\n")
