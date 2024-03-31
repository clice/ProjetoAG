from colorama import Fore, Style, init
from helpers.sorteio import *
from objetos.ilha import Ilha
from objetos.item import Item
from objetos.criatura import Criatura
from objetos.explorador import Explorador


# Função para inicializar o jogo
def inicializar_jogo():
    # Inicializar o jogo
    print("Bem-vindo(a) Explorador(a)! Você está chegando a ilha. Lembre-se que lá há muitos perigos.")
    print("O tesouro pirata que foi escondido na ilha já atraiu muitos, porém nenhum retornou.")
    print("Espero que você consiga retornar ao menos com alguma parte do tesouro.")
    print("Boa sorte!\n")

    while True:
        # Gerar elementos na Ilha
        ilha = gerar_elementos()

        print("Você está chegando a ilha!\n")

        print("Essas são as informações iniciais:")
        explorador = Explorador()  # Inicializar o Explorador
        explorador.__str__()  # Imprimir informações do Explorador
        ilha.desenhar_mapa(explorador.regiao.tipo)  # Mostrar mapa da Ilha

        mover_explorador(explorador, ilha)  # Realizar a movimentação do Explorador
        break


# Método para gerar os elementos da ilha
def gerar_elementos():
    # Inicializar o grafo da Ilha
    ilha = Ilha()
    ilha.gerar_mapa()

    qtd_elementos = sortear_qtd_elementos(ilha.qtd_regioes)  # Quantidade de elementos para adicionar as Regiões

    # Laço para rodar e gerar a quantidade de elementos na Ilha
    # Os sorteios ilha.regioes[1:-1] ignoram o primeiro e último itens da lista
    for _ in range(qtd_elementos):
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


# Função para realizar a movimentação do Explorador de uma Região a outra da Ilha
def mover_explorador(explorador, ilha):
    print(Fore.MAGENTA + f"Localização atual: {explorador.regiao.tipo}.")
    print(Style.RESET_ALL)  # Restaurar cores

    while True:
        resposta = input("Deseja avançar para um lugar aleatório (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            break
        
        # Mudar a região do Explorador
        mudar_regiao(explorador, ilha)

        print(Fore.MAGENTA + f"Localização atual: {explorador.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores

        # Checar o que tem na Região atualizada
        explorador.regiao.checar_regiao(explorador)


# Função para mudar a região da Criatura ou do Explorador
def mudar_regiao(personagem, ilha):
    adjacentes = list(ilha.encontrar_regioes_adjacentes(personagem.regiao.tipo))  # Regiões adjacentes da Região atual
    tipo_regiao = random.choice(adjacentes)           # Escolher aleatoriamente uma Região
    nova_regiao = ilha.encontrar_regiao(tipo_regiao)  # Informações da Região escolhida
    personagem.atualizar_regiao(nova_regiao)          # Atualizar a região


# Função para iniciar o jogo
if __name__ == "__main__":
    init()              # Inicializar colorama
    inicializar_jogo()  # Inicializar jogo
