from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
suma_n1 = 0
suma_n2 = 0 
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
  #Se suma todas las notas 1 es decir d[4]
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0],d[4],d[5]) #Creamos el objeto 
    suma_n1 = suma_n1 + p.obtener_nota1() #Acumulamos n1
    suma_n2 = suma_n2 + p.obtener_nota2() #Acumulamos n2
    #suma_n1 = suma_n1 + p.obtener_nota1()  #Esta linea permite sumar la nota uno pero con el uso de objeto y su metodo obtener
    if (p.obtener_nota1() < 15 or p.obtener_nota2() < 15):  #Comparamos si las notas son menores a 15
    	print(p.obtener_nombre())  #Imprimimos los nombres con notas menores a 15



promedio_n1 = suma_n1/len(lista) #Sacamos el priomedio de n1 
promedio_n2 = suma_n2/len(lista) #Sacamos el promedio de n2 
print (promedio_n1) #Imprimos
print (promedio_n2) #Imprimimos