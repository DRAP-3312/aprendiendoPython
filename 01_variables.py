my_variable = 'Mi variable'
age = 22
novato = True
money = 1.0
colores_fav = ['Verde', 'Negro', 'Azul', 'Blanco']
print({
    'var': my_variable.upper(),
    'age': age,
    'money': money,
    'colores': colores_fav
})

# Variables en una sola linea
name, edad, estado = 'paco', 80, 'aburrido'
# Algunas funciones del sistema
print(len(my_variable))


# inputs
mi_nombre = input('Whats your name? : ')
mi_edad = input('How old are you? : ')

print({ 'name': mi_nombre, 'edad': mi_edad})

def reverse_words(s):
    lista = s.split()
    lista.reverse()
    return ' '.join(lista)

print(reverse_words('hola guapo'))