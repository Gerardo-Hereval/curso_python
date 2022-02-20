import mysql.connector

mi_db=mysql.connector.connect(
    host='localhost',
    user='gerardo.heredia',
    password='Here182615',
    database='prueba'
)

cursor= mi_db.cursor()

#cursor.execute ('select * from Usuario') # para hacer una consulta

#cursor.execute('show create table Usuario') #para ver la estructura de las columnas de la tabla

#resultado= cursor.fetchall() #fetchall devolvera todas los resultados que se encontraron en la consulta
#y se los mandara a resultado, si queremos solo un resultado, daremos fetchone

#print (resultado)


#---------------------------
# para realizar un insert
#sql= 'insert into Usuario (email, username) values( %s, %s )' #los %s seran los valores agregados en values de abajo
#values=('pablo.segura@gmail.com','pablo.segura') #aqui se ingresaran los valores que se mandaran con insert
#cursor.execute(sql,values) #aqui se agregaran ambas partes para correr el codigo
#mi_db.commit()

#---------------------------
#para realizar un update
# sql= 'update Usuario set email= %s where id=%s'
# values= ('pablo.segura.abi@gmail.com',4)
# cursor.execute(sql,values)
# mi_db.commit()

#----------------------------

#para limitar los resultados
#cursor.execute ('select * from Usuario limit 1')
#resultado= cursor.fetchall()
#print (resultado)