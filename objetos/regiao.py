from colorama import Fore, Style


# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo):
        self.indice = indice     # Determina o índice da Região (vértice)
        self.tipo = tipo         # Determina o tipo de Região
        self.perc_tesouro = 0    # Determina o percentual do Tesouro que há na Região
        self.criaturas = []      # Lista de criaturas na Região
        self.qtd_criaturas = 0   # Quantidade de Criaturas na Região
        self.itens = []          # Lista de itens de cura na Região

    # String representando as informações sobre a Região
    def __str__(self):
        print(f"Índice: {self.indice}")
        print(f"Tipo: {self.tipo}")
        print(f"Criaturas: {self.criaturas}")
        print(f"Quantidade de criaturas: {self.qtd_criaturas}")
        print(f"Itens: {self.itens}")

    # MÉTODOS PARA AS INFORMAÇÕES DA REGIÃO

    # Método para checar qual a Região atual
    def checar_regiao(self):
        if self.tipo == 'Tesouro':
            print(Fore.CYAN + f"Você chegou ao Tesouro!")

            # Restaurar cores
            print(Style.RESET_ALL)
        else:
            print("Continue procurando...\n")

    # MÉTODOS PARA AS CRIATURAS DA REGIÃO

    # Método para adicionar criaturas na Região
    def adicionar_criatura(self, criatura):
        self.criaturas.append(criatura)
        self.qtd_criaturas += 1

    # Método para retornar se há mais de uma Criatura na Região
    def ha_criaturas(self):
        return self.qtd_criaturas > 1
