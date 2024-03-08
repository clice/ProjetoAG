# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    # Construtor de inicialização dos atributos da Região
    def __init__(self, tipo):
        self.indice = 0          # Determina o índice da Região (vértice)
        self.num_adjacentes = 0  # Inicializa a região sem vértices adjacantes
        self.tipo = tipo         # Determina o tipo de Região
        self.criaturas = None    # Lista de criaturas na Região
        self.perigos = None      # Lista de perigos na Região
        self.armas = None        # Lista de armas na Região
        self.itens = None        # Lista de itens de cura na Região


