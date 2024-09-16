def to_alternating_case(string):
    frase = list(str(string).split(' '))
    result = []
    for palabra in frase: 
        changes = ''
        for letra in palabra:
            if str(letra).islower():
                changes += letra.upper()
            else: 
                changes += letra.lower()
        result.append(changes)

    return ' '.join(result)

def formaCortar(string):
    return str(string).swapcase()


print(formaCortar('hoLa munDo'))
print(to_alternating_case('hoLa munDo'))