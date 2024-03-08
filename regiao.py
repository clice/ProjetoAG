# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo, criaturas=None, perigos=None, armas=None, itens=None):
        self.indice = indice                                         # Determina o índice da Região (vértice)
        self.num_adjacentes = 0                                      # Inicializa a região sem vértices adjacantes
        self.tipo = tipo                                             # Determina o tipo de Região
        self.criaturas = criaturas if criaturas is not None else []  # Lista de criaturas na Região
        self.perigos = perigos if perigos is not None else []        # Lista de perigos (plantas venenosas) na Região
        self.armas = armas if armas is not None else []              # Lista de armas na Região
        self.itens = itens if itens is not None else []              # Lista de itens de cura na Região


