from colorama import Fore, Style, init



# Função para checar o que tem na Região
# def checar_regiao(explorador):
#     if explorador.regiao.tipo == 'Tesouro':
#         print(Fore.CYAN + f"Você chegou ao Tesouro!")
#         print(Style.RESET_ALL)  # Restaurar cores
#     else:
#         if explorador.regiao.itens:
#             for item in explorador.regiao.itens:
#                 if item.tipo == 'criatura':
#                     print(f"{item.nome} encontrado(a)! CUIDADO!")
#                     explorador.lutar_criatura(item)
#
#                 if item.tipo == 'perigo':
#                     print(f"{item.nome} encontrado(a)! CUIDADO!")
#                     explorador.remover_pontos_vida(item.pontos)  # Remover pontos do Explorador
#                     print(f"Você agora tem {explorador.pontos_vida} pontos de vida!")
#
#                 if item.tipo == 'planta_medicinal':
#                     print(f"{item.nome} encontrado(a)!")
#
#                     while True:
#                         resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
#                         print()
#
#                         # Verificar resposta do Explorador
#                         if resposta.upper() == "S":
#                             break
#
#                     explorador.adicionar_item(item)  # Adicionar o elemento a lista
#                     print(Fore.GREEN + f"Você guardou {item.nome} na mochila!")
#                     print(Style.RESET_ALL)  # Restaurar cores
#
#                 if item.tipo == 'arma':
#                     print(f"{item.nome} encontrado(a)!.")
#
#                     while True:
#                         resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
#                         print()
#
#                         # Verificar resposta do Explorador
#                         if resposta.upper() == "S":
#                             break
#
#                     explorador.adicionar_item(item)  # Adicionar o elemento a lista
#                     print(Fore.GREEN + f"Você guardou {item.nome} na mochila!")
#                     print(Style.RESET_ALL)  # Restaurar cores
#
#         print("Nada na região. Continue procurando...\n")
