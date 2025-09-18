import random

import time


# Função substitui letras por símbolos/números para deixar a senha mais forte
def transformar_caractere(letra):
    substituicoes = {
        "a": "3", "A": "3",
        "b": "1", "B": "1",
        "c": "0", "C": "0",
        "d": "5", "D": "5",
        "e": "4", "E": "4",
        "f": "8", "F": "8",
        "g": "9", "G": "9",
        "h": "6", "H": "6",
        "i": "2", "I": "2",
        "j": "7", "J": "7",
        "k": "@", "K": "@",
        "l": "#", "L": "#",
        "m": "$", "M": "$",
        "n": "%", "N": "%",
        "o": ("&"), "O": ("&"),
        "p": "*", "P": "*",
        "q": "-", "Q": "-",
        "r": "+", "R": "+",
        "s": "!", "S": "!",
        "t": "^", "T": "^",
        "u": "~", "U": "~",
        "v": "`", "V": "`",
        "w": "=", "W": "=",
        "x": "<", "X": "<",
        "y": ">", "Y": ">",
        "z": "/", "Z": "/"
    }
    return substituicoes.get(letra, letra)

# Função que gera a senha forte com base no texto do usuário
def gerar_senha(base):
    random.seed(time.time())  # Inicializa o gerador de números aleatórios com o tempo atual
    
    nova_senha = ""  # Variável que vai guardar a senha final
    for letra in base:  # Percorre cada letra digitada
        nova_senha += transformar_caractere(letra)  # Substitui e adiciona na nova senha
    
    nova_senha += str(int(time.time()))[-2:] # Adiciona os dois últimos dígitos do timestamp atual

    #Embaralhando a ordem dos caracteres
    senha_lits = list(nova_senha)
    random.shuffle(senha_lits)
    senha = ''.join(senha_lits)

    # Adicionando caracteres extras para aumentar a segurança
    extra = "!@#$%*123456789"
    senha += random.choice(extra)
    senha += str(random.randint(10, 99))

    # Alternando entre maiúsculas e minúsculas
    senha = "".join(char.upper() if random.choice([True, False]) else char.lower()
            for char in senha)
    
    return nova_senha

# Programa principal
base = input("Digite a base da sua senha: ")
senha_forte = gerar_senha(base)
print("Sua nova senha é:", senha_forte)
