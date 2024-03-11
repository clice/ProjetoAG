import random
from criatura import Criatura

# # Gerar Ilha do jogo aleatoriamente
# ilha = Ilha()
# ilha.gerar_ilha_aleatoria()
# ilha.desenhar_ilha()


# OUTROS MÉTODOS

# Método para sortear uma Criatura
def sortear_criatura():
    # Lista das Criaturas na Ilha
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
    # Lista das Armas na Ilha
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
    # Lista das Plantas Venenosas
    plantas_venenosas = (
        {
            "tipo": "Planta Venenosa 1",
            "pontos": 5
        },
        {
            "tipo": "Planta Venenosa 2",
            "pontos": 10
        },
        {
            "tipo": "Visgo do Diabo",
            "pontos": 15
        }
    )

    return random.choice(plantas_venenosas)


# Método para sortear uma Planta Medicinal
def sortear_planta_medicinal():
    # Lista das Plantas Medicinais
    plantas_medicinais = (
        {
            "tipo": "Planta Medicinal 1",
            "pontos": 5
        },
        {
            "tipo": "Planta Medicinal 2",
            "pontos": 10
        },
        {
            "tipo": "Planta Medicinal 3",
            "pontos": 15
        }
    )

    return random.choice(plantas_medicinais)


# Método para sortear os perigos na Região
def sortear_perigos(self):
    # Lista dos Perigos da Ilha
    perigos = (
        'Passagens escorregadias à beira do abismo',
        'Animais selvagens perigosos ou venenosos',
        'Poço de areia movediça e de piche',
        'Plantas venenosas com frutos chamativos e aparentemente suculentos'
    )

    return random.choice(perigos)

# Métofo para sortear um
def sortear_regiao():
    regioes = ('Praia', 'Montanha', 'Lago', 'Paredão de Rocha', 'Riacho', 'Floresta')


criatura = sortear_criatura()
criatura = Criatura(criatura['tipo'], criatura['pontos_vida'], criatura['pontos_ataque'], criatura['descricao'], 0)
resposta = input(f"Deseja lutar com {criatura.tipo} (S/N)? ")
print(resposta)
