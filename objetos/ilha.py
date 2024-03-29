import networkx as nx
import matplotlib.pyplot as plt

from helpers.sorteio import *
from objetos.regiao import Regiao


# Declaração do objeto Ilha (Grafo)
class Ilha:
    # Construtor de inicialização dos atributos da Ilha
    def __init__(self):
        self.ilha = nx.Graph()                          # Inicializa um grafo vazio
        self.regioes = []                               # Lista de Regiões do grafo gerado 
        self.qtd_regioes = random.randint(5, 10)        # Número de Regiões na Ilha (vértices no grafo)
        self.qtd_arestas = 0                            #
        self.checkpoints = []                           # Lista de Regiões que são checkpoints
        self.criaturas = []                             # Lista de Criaturas na Ilha
        self.perigos = []                               # Lista de Perigos na Ilha
        self.armas = []                                 # Lista de Armas na Ilha

    # MÉTODOS PARA OS CHECKPOINTS

    # Método para adicionar os checkpoints
    def adicionar_checkpoints(self, regioes_usadas):
        if self.sortear_qtd_elementos() < 3:
            self.checkpoints = random.sample(regioes_usadas, self.sortear_qtd_elementos())
        else:
            # Definindo o máximo de Checkpoints igual a 3
            self.checkpoints = random.sample(regioes_usadas, 3)

    # Método para remover um checkpoint depois de usado
    def remover_checkpoint(self, checkpoint):
        self.checkpoints.remove(checkpoint)

    # MÉTODOS PARA GERAR E MANIPULAR O GRAFO DA ILHA
        
    # Método para gerar uma Ilha com valores aleatórios de Regiões (vértices)
    def gerar_ilha(self):
        regioes_usadas = []  # Lista de Regiões para não repetir no mapa

        # Adiciona Regiões a Ilha (vértices ao grafo)
        for i in range(self.qtd_regioes):
            if i == 0:
                # Caso seja o primeito vértice, será sempre a Praia
                nova_regiao = Regiao(i, 'Praia')  # Criando o objeto Região
                self.ilha.add_node('Praia')            # Adiciona vértice ao grafo
                self.regioes.append(nova_regiao)       # Adiciona o objeto Região as regiões da Ilha
            elif i == self.qtd_regioes - 1:
                # Caso seja o último vértice, será sempre o Tesouro
                nova_regiao = Regiao(i, 'Tesouro')  # Criando o objeto Região
                self.ilha.add_node('Tesouro')            # Adiciona vértice ao grafo
                self.regioes.append(nova_regiao)         # Adiciona o objeto Região as regiões da Ilha
            else:
                # Outros casos entre 1 e qtd_arestas - 1
                regiao_aleatoria = sortear_regiao(regioes_usadas)  # Sortear a Região da ILha
                nova_regiao = Regiao(i, regiao_aleatoria)          # Criando o objeto Região
                regioes_usadas.append(regiao_aleatoria)            # Adiciona a lista de regiões já utilizadas
                self.ilha.add_node(regiao_aleatoria)               # Adiciona vértice ao grafo
                self.regioes.append(nova_regiao)                   # Adiciona o objeto Região as regiões da Ilha

        # Adicionar os Checkpoints
        self.adicionar_checkpoints(regioes_usadas)

        # Atualizar a lista de regiões usadas com todas as regiões na ordem
        regioes_usadas.insert(0, 'Praia')
        regioes_usadas.append('Tesouro')

        print(regioes_usadas)
        print(self.qtd_regioes)

        # Garante que o grafo gerado é conectado adicionando arestas entre os vértices em sequência (0 -> 1 -> ...)
        for i in range(self.qtd_regioes - 1):
            self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

            if i == 0:
                # Primeiro vértice `Praia` conecta com o seguinte
                self.ilha.add_edge('Praia', regioes_usadas[i + 1])  # Adiciona aresta
            elif i == self.qtd_regioes - 2:
                # Penúltimo vértice conecta com o último `Tesouro`
                self.ilha.add_edge(regioes_usadas[i], 'Tesouro')  # Adiciona aresta
            else:
                # Vértices entre `Praia` e o `Tesouro`
                self.ilha.add_edge(regioes_usadas[i], regioes_usadas[i + 1])  # Adiciona aresta

        # Adiciona mais arestas aleatórias para tornar o grafo mais conectado
        for regiao in regioes_usadas:
            adjacente = random.choice(regioes_usadas)  # Escolhendo uma Região aleatória

            # Se a Região adjacente for diferente da Região atual,
            # adicionar como Região adjacente a atual
            # assim evitando arestas para o mesmo vértice
            if adjacente != regiao:
                # Conferindo se já existe uma aresta entre os vértices para evitar duplicidade
                if not self.ilha.has_edge(regiao, adjacente):
                    self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

                    if adjacente == 0:
                        self.ilha.add_edge(regiao, 'Praia')
                    elif adjacente == self.qtd_regioes - 1:
                        self.ilha.add_edge(regiao, 'Tesouro')
                    else:
                        self.ilha.add_edge(regiao, adjacente)

    # Método para desenhar a Ilha e método para plotar a movimentação 
    def desenhar_ilha(self, regiao_atual):  # Alterar nome para ficar mais facil de entender
        node_size = 5000  # Definir tamanho dos vértices para imprimir

        # Posição das Regiões (vértices)
        pos = nx.spring_layout(self.ilha)

        # Desenhar o grafo com: Regiões padrão cor "sky blue", arestas em preto e fonte negrito
        nx.draw(self.ilha, pos, with_labels=True, node_color='skyblue', edge_color='black', font_weight='bold',
                node_size=node_size)

        # Destacar a Região atual que o Explorador está com a cor "red"
        nx.draw_networkx_nodes(self.ilha, pos, nodelist=[regiao_atual], node_color='red', node_size=node_size)

        # Destacar a Região Checkpoint com a cor "yellow"
        for regiao in self.checkpoints:
            nx.draw_networkx_nodes(self.ilha, pos, nodelist=[regiao], node_color='yellow', node_size=node_size)

        # Salvar imagem do mapa
        # plt.savefig('mapa.png')

        # Exibir grafo
        plt.show()

    # OUTROS MÉTODOS

    # Método para gerar a quantidade de elementos
    def sortear_qtd_elementos(self):
        return round(self.qtd_regioes * (random.randint(20, 30) / 100))
        
    # # Método para gerar os adjacentes nas regiões
    # def add_adjacentes(self):
    #     for i in range(self.qtd_regioes):
    #         grau=self.ilha.degree(self.regioes[i])
    #         for j in range(grau):
    #             Regiao[i].adicionar_adjacente(list(Ilha.neighbors(j)))
    #
    # def retornar_regiao(self, indice):
    #     return(self.regioes[indice])

    # #Método para verificar os vertices disponiveis para movimentação
    # def caminhos_disponiveis(self,regiao_atual):
    #     for regiao_atual in range(self.regioes):
