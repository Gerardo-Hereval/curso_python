# c = open('baloo.txt','w')

# c.write('\nagregaremos una nueva linea a nuestro archivo')

# c.close()

import os

if os.path.exists('baloo.txt'):
    os.remove('baloo.txt')
else:
    print('El archivo no existe')


os.rmdir('miCarpeta')