import modulos as xs

from camelcase import CamelCase

c = CamelCase()
s = 'this is a sentence that needs CamelCasing!'

camelcase= c.hump(s)

print (camelcase)