#multiplicar dos numeros sin usar el simbolo de multiplicacion

a=4
b=8

resultado=0

for x in range(a):
    resultado+=b
# print(resultado)

#ingresa nombre y apellido e imprimelo al reves

nombre='Carlos'
apellido='Heredia'

conca=nombre+ ' ' + apellido

# print (conca[::-1])

#escribir una funcion que encuentre el elemento menor de una lista

lista=[1,2,3,4,123,-2,-23]

menor='init'

for x in lista:
    if menor == 'init':
        menor=x
    else:
        menor = x if x < menor else menor
# print ('menor: ', menor)


#escribir una funcion que devuelva el volumen de una esfera por su radio
#4/3*pi*r^3
#** elevar a una potencia
def calVolumen(r):
    return 4/3 * 3.14 * r ** 3
resultado=calVolumen(6)
# print(resultado)

#Escribir una funcion que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad>18

class Usuario:
    def __init__(self,edad):
        self.edad=edad

usuario=Usuario(15)
usuario2=Usuario(19)

resultado1= esMayor(usuario)
resultado2=esMayor(usuario2)

# print (resultado1,resultado2)

#escribir una funcion que indique si un numero es apr o impar

def esPar(n):
    return n%2==0

esPar(10)

resultado=esPar(11)
# print(resultado)

#escribir una funcion que indique cuantas vocales tiene una palabra
palabra='Baloo'
vocales= 0
for x in palabra:
    y=x.lower() #funcion para que pase a minuscula la letra
    vocales += 1 if y=='a' or y=='e' or y=='i' or y=='o' or y=='u' else 0
# print (vocales)

#escriba una aplicacion que reciba una cantidad infinita de numeros hasta decir basta
#luego que devuelva la suma de los numeros ingresados

# lista=[]
# print ('Ingrese numeros y para salir escriba "basta"')
# while True:
#     valor = input('Ingrese valor: ')
#     if valor =='basta':
#         break
#     else: 
#         try: 
#             valor=int(valor)
#             lista.append(valor)
#         except:
#             print ('Dato invalido')
#             exit()
# resultado=0
# for x in lista:
#     resultado+= x

#print (resultado)

#funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregaNombre(nombre,apellido):
    c= open('nombre_completo.txt','a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombre('santi','Heredia')