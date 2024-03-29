from colorama import init
from helpers.sorteio import *
from objetos.ilha import Ilha
from objetos.item import Item
from objetos.criatura import Criatura
from objetos.explorador import Explorador


# Função para inicializar o jogo
def inicializar_jogo():
    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    while True:
        # Gerar elementos na Ilha
        ilha = gerar_elementos()

        print("Você chegou a ilha!\n")
        print("Essas são as informações iniciais:")

        explorador = Explorador()      # Inicializar o Explorador
        explorador.__str__()           # Imprimir informações do Explorador
        explorador.movimentacao(ilha)  # Realizar a movimentação do Explorador

        # for criatura in ilha.criaturas:
        #     criatura.__str__()
        #     explorador.lutar_criatura(criatura)

        # criatura1 = sortear_criatura()
        # criatura1 = Criatura(criatura1['tipo'], criatura1['pontos_vida'], criatura1['pontos_ataque'],
        #                     criatura1['descricao'], 0)
        #
        # criatura2 = sortear_criatura()
        # criatura2 = Criatura(criatura2['tipo'], criatura2['pontos_vida'], criatura2['pontos_ataque'],
        #                     criatura2['descricao'], 0)
        #
        # criatura1.lutar_criatura(criatura2)

        break


# Método para gerar os elementos da ilha
def gerar_elementos():
    # Inicializar o grafo da Ilha
    ilha = Ilha(random.randint(5, 10))
    ilha.gerar_ilha()
    ilha.desenhar_ilha('Praia')

    regioes = ilha.regioes[1:-1]  # Remover primeiro e último elementos da lista de Regiões

    for i in range(sortear_qtd_elementos(ilha.qtd_regioes)):
        regiao = random.choice(regioes)         # Sortear uma das Regiões da Ilha

        # Sortear Criatura para adicionar a Região
        criatura = sortear_criatura()
        criatura = Criatura(
            criatura['nome'], criatura['pontos_vida'], criatura['pontos_ataque'],
            criatura['descricao'], regiao.tipo
        )
        regiao.criaturas.append(criatura)  # Adiciona a Criatura a Região

        # Sortear Perigo para adicionar a Região
        perigo = sortear_perigo()
        perigo = Item(perigo['nome'], perigo['tipo'], perigo['pontos'], 1, regiao.tipo)
        regiao.itens.append(perigo)  # Adiciona o Perigo a Região

        # Sortear Planta Medicianal para adicionar a Região
        planta_medicinal = sortear_planta_medicinal()
        planta_medicinal = Item(
            planta_medicinal['nome'], planta_medicinal['tipo'],
            planta_medicinal['pontos'], 1, regiao.tipo
        )
        regiao.itens.append(planta_medicinal)  # Adiciona a Planta Medicinal a Região

        # Sortear Arma para adicionar a Região
        arma = sortear_arma()
        arma = Item(arma['nome'], arma['tipo'], arma['pontos'], 3, regiao.tipo)
        regiao.itens.append(arma)  # Adiciona a Arma a Região

    return ilha


# Iniciar o jogo
if __name__ == "__main__":
    # Inicializar colorama
    init()

    # Inicializar o jogo
    inicializar_jogo()
