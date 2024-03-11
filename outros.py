import random
from criatura import Criatura

# # Gerar Ilha do jogo aleatoriamente
# ilha = Ilha()
# ilha.gerar_ilha_aleatoria()
# ilha.desenhar_ilha()


# OUTROS MÉTODOS

# Método para sortear uma Criatura
def sortear_criatura():
    # Dicionário das Criaturas na Ilha
    criaturas = (
        {
            "tipo": "Crocodilo Gigante",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Tem 8 metros de comprimento, possui pele dura, "
                         "bastante força e mordida poderosa"
        },
        {
            "tipo": "Formiga Quimera",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Podem desossar um boi em poucos minutos "
                         "apesar de frágeis individualmente"
        },
        {
            "tipo": "Onça Pintada",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Consegue se camuflar quase que perfeitamente, "
                         "e possui o tamanho de um touro, com garras "
                         "e dentes poderosos"
        }
    )

    return random.choice(criaturas)


# Método para sortear uma Arma
def sortear_arma():
    # Dicionário das Armas na Ilha
    armas = (
        {
            "tipo": "Faca",
            "pontos_ataque": 5
        },
        {
            "tipo": "Espada",
            "pontos_ataque": 10
        },
        {
            "tipo": "Pistola",
            "pontos_ataque": 15
        }
    )
    
    return random.choice(armas)


# Método para sortear uma Planta Venenosa
def sortear_planta_venenosa():
    # Dicionário das Plantas Venenosas
    plantas_venenosas = (
        {
            "tipo": "",
            "pontos": 5
        },
        {
            "tipo": "",
            "pontos": 10
        },
        {
            "tipo": "Visgo do Diabo",
            "pontos": 15
        }
    )

    return random.choice(plantas_venenosas)


# Método para sortear uma Planta Medicinal
def sortear_planta_medicional():
    # Dicionário das Plantas Medicinais
    plantas_medicinais = (
        {
            "tipo": "",
            "pontos": 5
        },
        {
            "tipo": "",
            "pontos": 10
        },
        {
            "tipo": "",
            "pontos": 15
        }
    )

    return random.choice(plantas_medicinais)


criatura = sortear_criatura()
criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'], criatura['descricao'], 0)
resposta = input(f"Deseja lutar com {criatura.tipo} (S/N)? ")
print(resposta)
