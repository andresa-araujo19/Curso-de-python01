lista = []

while True:
    nome = input('Diga seu nome: ')
    if '.' not in nome:
        lista.append(nome)
    else:
        break

print(f'Lista de nome: {lista}.')