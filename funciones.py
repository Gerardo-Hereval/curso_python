from re import I


def miFuncion():
    print('Mi primera funcion')

#miFuncion()

def imprimeDato(*nombre):
    print('El nombre completo es: ',nombre)

#imprimeDato('carlos','heredia')

def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

#nombreCompleto(nombre='Carlos', apellido='Heredia')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

#nombreCompleto2(nombre='Carlos', apellido='Heredia')

def mifuncion2(argumento='Santi'):
    print (argumento)

# mifuncion2('batman')
# mifuncion2()


def conca(lista):
    i=''
    for el in lista:
        i=i + el + ' '
    return i
#nombres = conca(['Carlos', 'Heredia'])
#print (nombres)

def recursion(i):
    if (i<1):
        return i
    print(i)
    recursion(i-1)

recursion(6)