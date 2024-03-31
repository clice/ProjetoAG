# Função para mover Explorador de Região
def mover_explorador(explorador, ilha):
    while True:
        resposta = input("Deseja avançar para uma região aleatória (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            break

        explorador.atualizar_regiao(ilha)  # Atualizar a região do Explorador
        explorador.mostrar_regiao()  # Mostrar localização atual
        break


# Função
