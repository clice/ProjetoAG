import random

from helpers.checagem import *
from colorama import Fore, Style, init


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
        
        adjacentes = list(ilha.encontrar_regioes_adjacentes(explorador.regiao.tipo))   # Regiões adjacentes da Região atual
        explorador.atualizar_regiao(ilha.encontrar_regiao(random.choice(adjacentes)))  # Atualizar a região

        print(Fore.MAGENTA + f"Localização atual: {explorador.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores

        # Checar o que tem na Região atualizada
        checar_regiao(explorador)  