def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, digite um valor válido')
            continue
        except (KeyboardInterrupt):
            print('Digite um valor antes')
            return 0
        else:
            return n

def leiastr(msg):
    while True:
        try:
            n = str(input(msg)).lower()
        except (ValueError, TypeError):
            print('Digite um elemento válido')
            continue
        except (KeyboardInterrupt):
            print('Digite um elemento válido')
            return 0
        else:
            return n


def menu(list):
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1


def itenscomuns(lista1, lista2):
    counter = 0
    for x in lista1:
        for y in lista2:
            if x == y:
                counter += 1

    return counter


def compare_element(attackelement, barrier):
    counter = 0
    for x in barrier:
        if x == "sun":
            counter += attackelement[0]
        if x == "moon":
            counter += attackelement[1]
        if x == "fire":
            counter += attackelement[2]
        if x == "water":
            counter += attackelement[3]
        if x == "wood":
            counter += attackelement[4]
        if x == "metal":
            counter += attackelement[5]
        if x == "earth":
            counter += attackelement[6]
        if x == "star":
            counter += attackelement[7]

    return counter

