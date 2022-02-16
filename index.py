#Acá van los comentarios
#if 3>5:
#print('Esto no se va a imprimir')
#if 5>3:
#        print('5 es mayor que 3')


x=5
y='Chanchito feliz'

#print(x,y)

email= 'carlos.valenzh@gmail.com'
#print(email)

a, b, c = 'Lala','lele','lili'

#print(a,b,c)

valor1=valor2=valor3= 'chanchito feliz'

#print(valor1,valor2,valor3)

inicio='Hola '
final= 'Mundo'

#print (inicio + final)

palabra='Hola mundo'
palabra1="Hola mundo"
num_entero= 20
num_decimales=20.2
num_complejo=1j

#print(palabra,palabra1,num_entero,num_decimales,num_complejo)

lista=['Hola','Mundo','Chanchito feliz']
lista1 =lista.copy()
lista.append('digimon')
lista.append('pokemon')
#lista.clear()
#print(lista,len(lista))
largo_lista=len(lista)
largo_lista1=len(lista1)
#print(largo_lista,largo_lista1)
#print(lista[0])

#lista.pop() #elimina ultimo registro
#lista.remove('Hola') #elimina valor especifico
lista.reverse()
lista.sort()
tupla=('Hola','Mundo','Somos','Tupla')
listaDeTupla= list(tupla)
listaDeTupla.append('jeje')
#print(listaDeTupla)

rango=range(6)
#print(rango)

#creacion de diccionarios

diccionario={
    "nombre":"Baloo",
    "raza":"perro",
    "edad":5
}

#print(diccionario)
#print (diccionario ['nombre']) #para adquirir solo un valor
#print (diccionario.get('nombre')) #para tener el valor de un diccionario
#nombre=diccionario.get('nombre') #para asignar un valor del diccionario a una variable
#print(nombre)

diccionario ['ronroneo']='sí'

#print(diccionario)

gatitos = {
    "fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "mamba":
    {
        "nombre": "mamba",
        "edad":3
    }
}

#print (gatitos)

perritos = dict(nombre="baloo") #para crear diccionario es otra opcion