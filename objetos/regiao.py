# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo):
        self.indice = indice     # Determina o índice da Região (vértice)
        self.tipo = tipo         # Determina o tipo de Região
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

    # MÉTODO PARA AS CRIATURAS DA REGIÃO

    # Método para adicionar criaturas na Região
    def adicionar_criatura(self, criatura):
        self.criaturas.append(criatura)
        self.qtd_criaturas += 1

    # Método para retornar se há mais de uma Criatura na Região
    def ha_criaturas(self):
        return self.qtd_criaturas > 1
