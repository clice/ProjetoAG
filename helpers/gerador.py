from helpers.sorteios import *
from objetos.ilha import Ilha
from objetos.item import Item
from objetos.regiao import Regiao
from objetos.criatura import Criatura
from objetos.explorador import Explorador


# Função para gerar a ilha
def gerar_ilha():
    # Inicializar a ILha
    ilha = Ilha()
    ilha.adicionar_mapa()
        
    # Laço para rodar e gerar a quantidade de elementos na Ilha
    # Os sorteios ilha.regioes[1:-1] ignoram o primeiro e último itens da lista
    for _ in range(ilha.qtd_itens):
        # Gerar Criatura numa Região da Ilha
        regiao = random.choice(ilha.regioes[1:-1])
        criatura = sortear_criatura()  # Sortear Criatura para adicionar a Região
        criatura = Criatura(
            criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
            criatura['pontos_ataque'], criatura['descricao'], regiao.tipo
        )  # Objeto Criatura
        regiao.adicionar_criatura(criatura)  # Adiciona a Criatura a Região

        # Gerar Perigo numa Região da Ilha
        perigo = sortear_perigo()  # Sortear Perigo para adicionar a Região
        gerar_item(random.choice(ilha.regioes[1:-1]), perigo)

        # Gerar Planta Medicinal numa Região da Ilha
        planta_medicinal = sortear_planta_medicinal()  # Sortear Planta Medicianal para adicionar a Região
        gerar_item(random.choice(ilha.regioes[1:-1]), planta_medicinal)

        # Gerar Arma numa Região da Ilha
        arma = sortear_arma()  # Sortear Arma para adicionar a Região
        gerar_item(random.choice(ilha.regioes[1:-1]), arma)

    return ilha


# Função para gerar um Item na Região
def gerar_item(regiao, item):
    regiao.adicionar_item(
        Item(
            item['nome'], item['tipo'], item['pontos'],
            item['qtd_uso'], regiao.tipo
        )
    )  # Adiciona o Item na Região


# Função para gerar o Explorador
def gerar_explorador(qtd_movimentos):
    print("Informações iniciais:")
    regiao = Regiao(0, 'Praia', 0)
    explorador = Explorador(regiao, qtd_movimentos)  # Inicializar o Explorador
    explorador.__str__()  # Imprimir informações do Explorador
    return explorador


# Função para checar o que tem na Região
def checar_regiao(explorador):
    if explorador.regiao.tipo == 'Tesouro':
        explorador.regiao.encontrar_tesouro(explorador)
