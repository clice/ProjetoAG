import networkx as nx
import matplotlib.pyplot as plt

from helpers.sorteio import *
from objetos.regiao import Regiao


# Declaração do objeto Ilha (Grafo)
class Ilha:
    # Construtor de inicialização dos atributos da Ilha
    def __init__(self):
        self.mapa = nx.Graph()                          # Inicializa um grafo vazio (Mapa da Ilha)
        self.regioes = []                               # Lista de Regiões do grafo gerado
        self.qtd_regioes = random.randint(5, 10)  # Número de Regiões na Ilha (vértices no grafo)
        self.qtd_arestas = 0                            # Quantidade de arestas para a movimentação total permitida
        self.checkpoints = []                           # Lista de Regiões que são checkpoints

    # MÉTODOS PARA GERAR E MANIPULAR O GRAFO DA ILHA

    # Método para gerar uma Ilha com valores aleatórios de Regiões (vértices)
    def gerar_mapa(self):
        regioes_usadas = []  # Lista de Regiões para não repetir no mapa

        # Adiciona Regiões a Ilha (vértices ao grafo)
        for i in range(self.qtd_regioes):
            if i == 0:
                # Caso seja o primeito vértice, será sempre a Praia
                self.adicionar_regiao(i, 'Praia', 0)  # Adiciona a Região ao grafo Mapa
            elif i == self.qtd_regioes - 1:
                # Caso seja o último vértice, será sempre o Tesouro
                self.adicionar_regiao(i, 'Tesouro', 100)  # Adiciona a Região ao grafo Mapa
            else:
                # Outros casos entre 1 e qtd_regioes - 1
                regiao_aleatoria = sortear_regiao(regioes_usadas)  # Sortear a Região da ILha
                regioes_usadas.append(regiao_aleatoria)            # Adiciona a lista de regiões já utilizadas
                self.adicionar_regiao(i, regiao_aleatoria, 0)      # Adiciona a Região ao grafo Mapa

        # Adicionar os Checkpoints
        self.adicionar_checkpoints(regioes_usadas)

        # Atualizar a lista de regiões usadas com todas as regiões na ordem
        regioes_usadas.insert(0, 'Praia')
        regioes_usadas.append('Tesouro')

        # Garante que o grafo gerado é conectado adicionando arestas entre os vértices em sequência (0 -> 1 -> ...)
        for i in range(self.qtd_regioes - 1):
            self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

            if i == 0:
                # Primeiro vértice `Praia` conecta com o seguinte
                self.mapa.add_edge('Praia', regioes_usadas[i + 1])  # Adiciona aresta
            elif i == self.qtd_regioes - 2:
                # Penúltimo vértice conecta com o último `Tesouro`
                self.mapa.add_edge(regioes_usadas[i], 'Tesouro')  # Adiciona aresta
            else:
                # Vértices entre `Praia` e o `Tesouro`
                self.mapa.add_edge(regioes_usadas[i], regioes_usadas[i + 1])  # Adiciona aresta

        # Adiciona mais arestas aleatórias para tornar o grafo mais conectado
        for regiao in regioes_usadas:
            adjacente = random.choice(regioes_usadas)  # Escolhendo uma Região aleatória

            # Se a Região adjacente for diferente da Região atual,
            # adicionar como Região adjacente a atual
            # assim evitando arestas para o mesmo vértice
            if adjacente != regiao:
                # Conferindo se já existe uma aresta entre os vértices para evitar duplicidade
                if not self.mapa.has_edge(regiao, adjacente):
                    self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

                    if adjacente == 0:
                        self.mapa.add_edge(regiao, 'Praia')
                    elif adjacente == self.qtd_regioes - 1:
                        self.mapa.add_edge(regiao, 'Tesouro')
                    else:
                        self.mapa.add_edge(regiao, adjacente)

    # Método para desenhar a Ilha e método para plotar a movimentação
    def desenhar_mapa(self, regiao_atual):  # Alterar nome para ficar mais facil de entender
        # plt.ion()                          # Ativar modo interativo
        node_size = 5000                   # Definir tamanho dos vértices para imprimir
        pos = nx.spring_layout(self.mapa)  # Posição das Regiões (vértices)

        # Desenhar o grafo com: Regiões padrão cor "sky blue", arestas em preto e fonte negrito
        nx.draw(self.mapa, pos, with_labels=True, node_color='skyblue', edge_color='black', font_weight='bold',
                node_size=node_size)

        # Destacar a Região atual que o Explorador está com a cor "red"
        nx.draw_networkx_nodes(self.mapa, pos, nodelist=[regiao_atual], node_color='red', node_size=node_size)

        # Destacar a Região Checkpoint com a cor "yellow"
        for regiao in self.checkpoints:
            nx.draw_networkx_nodes(self.mapa, pos, nodelist=[regiao], node_color='yellow', node_size=node_size)

        # plt.pause(1)  # Pausa de 1 segundo para permitir plotar a exibição
        # plt.clf()     # Limpar a exibição anterior
        # plt.ioff()    # Desativar o modo interativo

        # Salvar imagem do mapa
        # plt.savefig('mapa.png')

        # Exibir grafo
        plt.show()

    # MÉTODOS PARA AS REGIÕES DO GRAFO

    # Método para adicionar uma Região ao grafo
    def adicionar_regiao(self, indice, tipo, perc_tesouro):
        self.mapa.add_node(tipo)                                 # Adiciona vértice ao grafo
        self.regioes.append(Regiao(indice, tipo, perc_tesouro))  # Adiciona o objeto Região as regiões da Ilha

    # Método para buscar a região e a retornar
    def encontrar_regiao(self, tipo_regiao):
        # Laço para percorrer todas as regiões da Ilha
        for regiao in self.regioes:
            if regiao.tipo == tipo_regiao:
                return regiao

    # Método para retornar as regiões adjacentes do grafo Ilha
    def encontrar_regioes_adjacantes(self, regiao):
        return list(self.mapa.neighbors(regiao))

    # MÉTODOS PARA OS CHECKPOINTS

    # Método para adicionar os checkpoints
    def adicionar_checkpoints(self, regioes):
        qtd_elementos = sortear_qtd_elementos(self.qtd_regioes)

        if qtd_elementos < 3:
            # Sortear uma quantidade de elementos com base na lista de regiões
            self.checkpoints = random.sample(regioes, qtd_elementos)
        else:
            # Sortear uma quantidade de elementos com base na lista de regiões
            self.checkpoints = random.sample(regioes, 3)

    # Método para remover um checkpoint depois de usado
    def remover_checkpoint(self, checkpoint):
        self.checkpoints.remove(checkpoint)
