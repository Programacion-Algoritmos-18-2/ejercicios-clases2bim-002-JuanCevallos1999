from paquete_archivos.miarchivo import MiArchivo  #Importamos las clases que utilizaremos 
from paquete_modelo.mimodelo import Persona 		
from paquete_modelo.mimodelo import OperacionesPersona
m = MiArchivo() #Creamos un objeto de la clase archivo 

lista = m.obtener_informacion() #Creamos una lista con la informacion del archivo mediante el metodo obtener_informacion
lista = [l.split("|") for l in lista] #Usamos split para separar las listas y crear una especia de arreglo por cada linea

# print(lista)

lista = lista[1:] #Empezamos la lista en 1 
lista_personas = [] #Creamos una lista vacia 
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista: #Recorremos la lista 
    p = Persona(d[1], d[2], d[3], d[0],d[4],d[5]) #Creamos el objeto con los parametros de la lista 
    lista_personas.append(p) #Agregamos a nuestra lista vacia el objeto que creamos 
    #print(p)

operaciones = OperacionesPersona(lista_personas) #Enviamos la lista cargada a la clase 
print(operaciones.obtener_promedion1()) #Llamamos el metodo obtener_promedio1 y lo imprimimos
print("")
print(operaciones.obtener_promedion2()) #Llamamos el metodo obtener_promedio2 y lo imprimimos 
print("")
print(operaciones.obtener_listado_n1()) #Llamamos el metodo obtener_listadon1 y lo imprimimos
print("")
print(operaciones.obtener_listado_n2()) #Llamamos el metodo obtener_listado_n2  y lo imprimimos
print("")
print(operaciones.obtener_listado_personas('R','J')) #Llamamos el metodo y enviamos parametros e imprimimos 