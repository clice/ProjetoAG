import random

from colorama import Fore, Style
from helpers.sorteios import sortear_criatura


# Declaração do objeto Criatura
class Criatura:
    # Construtor de inicialização dos atributos da Criatura
    def __init__(self, nome, tipo, pontos_vida, pontos_ataque, descricao, regiao):
        self.nome = nome                    # Nome da Criatura
        self.tipo = tipo                    # Tipo da Criatura
        self.pontos_vida = pontos_vida      # Pontos de vida da Criatura
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Criatura
        self.descricao = descricao          # Descrição da Criatura
        self.regiao = regiao                # Região (vértice) da Criatura no mapa (grafo)

    # String representado as informações sobre a Criatura
    def __str__(self):
        print(f"Criatura: {self.nome}")
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Descrição: {self.descricao}")
        print(f"Região: {self.regiao.tipo}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

    # Método para retornar se a Criatura está viva (pontos_vida > 0)
    def esta_viva(self):
        return self.pontos_vida > 0
    
    # Método para reviver a Criatura depois de morrer durante a luta
    def reviver(self, ilha):
        regiao = random.choice(ilha.regioes[1:-1])
        criatura = sortear_criatura()  # Sortear Criatura para adicionar a Região
        criatura = Criatura(
            criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
            criatura['pontos_ataque'], criatura['descricao'], regiao
        )  # Objeto Criatura
        self.adicionar_criatura(criatura)    
    
    # MÉTODO PARA A REGIÃO DA CRIATURA

    # Método para mostrar a localização atual
    def mostrar_regiao(self):
        print(Fore.MAGENTA + f"Localização atual: {self.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores
