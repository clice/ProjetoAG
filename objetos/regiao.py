import random

from colorama import Fore, Style


# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao:
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo, tesouro):
        self.indice = indice    # Determina o índice da Região (vértice)
        self.tipo = tipo        # Determina o tipo de Região
        self.tesouro = tesouro  # Determina o percentual do Tesouro que há na Região
        self.criaturas = []     # Lista de Criaturas na Região
        self.itens = []         # Lista de Itens na Região

    # String representando as informações sobre a Região
    def __str__(self):
        print(f"Índice: {self.indice}")
        print(f"Tipo: {self.tipo}")

    # MÉTODOS PARA A QUANTIDADE PERCENTUAL DO TESOURO NA REGIÃO

    # Método para remover o percentual do tesouro da Região
    def remover_tesouro(self, tesouro):
        self.tesouro -= tesouro

    # MÉTODOS PARA AS CRIATURAS NA REGIÃO

    # Métoro para adicionar Criatura na Região
    def adicionar_criatura(self, criatura):
        self.criaturas.append(criatura)

    # Método para remover Criatura da Região
    def remover_criatura(self, criatura):
        self.criaturas.remove(criatura)

    # Método para retornar se há Criaturas na Região
    def ha_criaturas(self):
        return bool(self.criaturas)

    # MÉTODOS PARA OS ITENS NA REGIÃO

    # Método para adicionar Item na Região
    def adicionar_item(self, item):
        self.itens.append(item)

    # Método para remover Item da Região
    def remover_item(self, item):
        self.itens.remove(item)

    # MÉTODOS PARA CHECAR AS INFORMAÇÕES DA REGIÃO

    # Método para quando o Explorador encontrar o tesouro
    def encontrar_tesouro(self, explorador):
        print(Fore.CYAN + f"VOCÊ CHEGOU AO TESOURO!")
        print(Style.RESET_ALL)  # Restaurar cores

        resposta = input(f"Deseja resgatar o tesouro (S/Outro)? ")

        if resposta.upper() != "S":
            print("Não quer")
            # if explorador.ha_armas():
        else:
            explorador.adicionar_tesouro()  # Adicionar o percentual do tesouro ao Explorador
            self.tesouro = explorador.tesouro  # Atualizar o percentual do tesouro restanda na Região
