# dato= input('ingrese dato: ')

# lista = ['Hola' 'mundo','chanchito','feliz','dragones']

# if lista.count(dato) > 0:
#     print('El dato existe:',dato)
# else:
#     print('El dato no existe :(', dato)

primero = input('ingrese el primer numero: ')
try: 
    primero= int(primero)
except:
    primero = 'letra'
if primero=='letra': 
    print ('El valor Ingresado no e sun numero')
    exit()

segundo =  input('ingresa el segundo numero: ')
try:
    segundo=int(segundo)
except:
    segundo='letra'
    
if segundo=='letra': 
    print ('El valor Ingresado no e sun numero')
    exit()

simbolo=input('Ingrese operacion: ')

if simbolo=='+':
    print('Suma:', primero+segundo)
elif simbolo=='-':
    print('Resta: ',primero-segundo)
elif simbolo=='*':
    print('Multiplicacion: ',primero*segundo)
elif simbolo=='/':
    print('Division: ',primero/segundo)
else:
    print('vuleve a internarlo, ingresa un simbolo valido + - * /')