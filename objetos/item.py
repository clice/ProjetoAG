from colorama import Fore, Back, Style


# Declaração do objeto Arma
class Item:
    # Construtor de inicialização dos atributos da Arma
    def __init__(self, nome, tipo, pontos, qtd_uso, regiao):
        self.nome = nome        # Nome do Item
        self.tipo = tipo        # Tipo do Item
        self.pontos = pontos    # Pontos do Item
        self.qtd_uso = qtd_uso  # Quantidade de uso do Item
        self.regiao = regiao    # Região (vértice) do Item no mapa (grafo)

    # String representando as informações sobre a Arma
    def __str__(self):
        print(Back.YELLOW + Fore.BLACK + f"     Nome: {self.nome} " + Style.RESET_ALL)
        print(Back.YELLOW + Fore.BLACK + f"     Pontos: {self.pontos} " + Style.RESET_ALL)
        print(Back.YELLOW + Fore.BLACK + f"     Usos: {self.qtd_uso} " + Style.RESET_ALL)
        
    # MÉTODO PARA A QUANTIDADE DE USO DO ITEM

    # Método para remover a quantidade de uso do Item
    def remover_qtd_uso(self):
        self.qtd_uso -= 1
