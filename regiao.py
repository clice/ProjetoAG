# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo):
        self.indice = indice     # Determina o índice da Região (vértice)
        self.qtd_adjacentes = 0  # Quantidade de vértices adjacantes a Região
        self.adjacentes = None   # Lista de vértices adjacentes a Região
        self.tipo = tipo         # Determina o tipo de Região
        self.criaturas = None    # Lista de criaturas na Região
        self.qtd_criaturas = 0   # Quantidade de Criaturas na Região
        # self.perigos = None      # Lista de perigos na Região
        # self.armas = None        # Lista de armas na Região
        self.itens = None        # Lista de itens de cura na Região

    # MÉTODO PARA OS VÉRTICES ADJACENTES DA REGIÃO

    # Método para adicionar um vértice adjacente a Região
    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
        self.qtd_adjacentes += 1

    # Método para retornar os vértices adjacentes a Região
    def get_adjacentes(self):
        return self.adjacentes.keys()

    # MÉTODO PARA AS CRIATURAS DA REGIÃO

    # Método para adicionar criaturas na Região
    def adicionar_criaturas(self, criatura):
        self.criaturas.append(criatura)
        self.qtd_criaturas += 1

    # Método para retornar se há mais de uma Criatura na Região
    def ha_criaturas(self):
        return self.qtd_criaturas > 1
