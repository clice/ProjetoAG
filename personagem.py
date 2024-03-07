import random

# Declaração do objeto Personagem
class Personagem:
    # Construtor de inicialização dos atributos do Personagem
    def __init__ (self, pontos_vida=100, pontos_ataque=20, per_tesouro=0, itens=None):
        self.pontos_vida = pontos_vida                     # Pontos de vida do Personagem
        self.pontos_ataque = pontos_ataque                 # Pontos de ataque do Personagem
        self.per_tesouro = per_tesouro                     # Porcentagem do tesouro carregado pelo personagem
        self.itens = itens if itens is not None else []    # Lista de itens carregados pelo Personagem

    # String representando as informações sobre o Personagem
    def __str__(self):
        return (f"Explorador: "
                f"Pontos de vida = {self.pontos_vida}, "
                f"Pontos de ataque = {self.pontos_ataque}, "
                f"Porcentagem do tesouro = {self.per_tesouro},"
                f"Itens = {self.itens}")

