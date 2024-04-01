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
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Pontos: {self.pontos}")
        print(f"Usos: {self.qtd_uso}")
        print(f"Região: {self.regiao.tipo}")
        
    # MÉTODO PARA A QUANTIDADE DE USO DO ITEM

    # Método para remover a quantidade de uso do Item
    def remover_qtd_uso(self):
        self.qtd_uso -= 1
