"""
    creación de clases
"""
#Creamos la clase persona 
class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, n1, n2): #Creamos el constructor de la clase 
        """
        """ 
        #Inicializamos los atributos del constructor 
        self.nombre = n   
        self.edad = int(ed)  #Utilizamos int para convertir la cadena ingresada a un valor entero
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1) #Utilizamos int para convertir la cadena ingresada a un valor entero
        self.nota2 = int(n2) #Utilizamos int para convertir la cadena ingresada a un valor entero

    def agregar_nombre(self, n):   #Creamos el set del atributo nombre 

        self.nombre = n

    def obtener_nombre(self): #Creamos el get del atributo nombre que no resive parametros porque devuelve

        return self.nombre

    def agregar_edad(self, n): #Creamos el set del atributo edad 

        self.edad = int(n)

    def obtener_edad(self): #Creamos el get del atributo edad que no resive parametros porque devuelve
 
        return self.edad
    
    def agregar_codigo(self, n):  #Creamos el set del atributo codigo
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self): #Creamos el get del atributo codigo que no resive parametros porque devuelve
        """
        """
        return self.codigo
    
    def agregar_apellido(self, n):  #Creamos el set del atributo apellido 
    	self.apellido = n

    def obtener_apellido(self): #Creamos el get del atributo apllido  que no resive parametros porque devuelve

        return self.apellido

    def agregar_nota1(self, n):  #Creamos el set del atributo nota1
    	self.nota1 = int(n)

    def obtener_nota1(self): #Creamos el get del atributo nota1 que no resive parametros porque devuelve
    	return self.nota1

    def agregar_nota2(self, n):  #Creamos el set del atributo nota2
    	self.nota2 = int(n)

    def obtener_nota2(self): #Creamos el get del atributo nota2  que no resive parametros porque devuelve
    	return self.nota2
    
    def __str__(self): #Creamos el metodo str que es similiar al toString en java 

        return "%s - %s - %d - %d - %d -%d" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(),self.obtener_nota1(),self.obtener_nota2())
#Retornanos una cadena que presenta los atributos de la clase
#Creamos la clase OperacionesPersona que hará los metodos necesarios (calculos, etc)

class OperacionesPersona(object):  #Creamos la clase 

    #Creamos el constructor que recibirá la lista
    def __init__(self, listado):

        self.listado_personas = listado    #Inicializamos la lista_personas que será globan en la clase

    def obtener_promedion1(self):  #Creamos el metodo para obtener el promedio 1
        suma_n1 = 0 #INicializamos la variable 
        for n in self.listado_personas: #Creamos un for que recorra toda la lsita 
           suma_n1 = suma_n1 + n.obtener_nota1() #Acumulamos el valor de la suma total en el ciclo for ya que iterara todas

        promedio = (suma_n1/len(self.listado_personas)) #Calculamos el promedio con la longitud de la lista que es el numero de iteraciones
        return promedio #devolvemos promedio 

    def obtener_promedion2(self): #Creamos el metodo obtener promedio 2
        suma_n2 = 0 #Inicializamos la varaible 
        for n in self.listado_personas: #For que recorrera toda la lista 
           suma_n2 = suma_n2 + n.obtener_nota2() #Acumulamos los valores de n2
           
        promedio2 = (suma_n2/len(self.listado_personas)) #Calculamos el promedio con la longitud de la lista que es el numero de iteraciones devolvemos promedio 
        return promedio2

    def obtener_listado_n1(self): #creamos el metodo que presentara personas con n1 menores a 15
        cadena = " " #Inicializamos la cadena
        for n in self.listado_personas: #Recorremos toda la lista 
            if (n.obtener_nota1() < 15): #Obtenemos n1 y la compramos en la condicion <15 
                cadena = "%s %s %s"%(cadena, n.obtener_nombre(), n.obtener_apellido()) #En caso de ser afirmativa hacemos la cadena
        return cadena #retornamos la cadena

    def obtener_listado_n2(self): #creamos el metodo presentara personas con n2 menores a 15
        cadena = " " #Inicializamos la cadena 
        for n in self.listado_personas:
            if (n.obtener_nota2() < 15):  #Comparamos cada iteracion n2 < 15 
                cadena = "%s %s %s"%(cadena, n.obtener_nombre(), n.obtener_apellido()) #En caso de ser afirmativo hacemos la cadena y la retornamos
        return cadena

    def obtener_listado_personas(self, b ,c): #Creamos el metodo que presentara personas que empiecen con R y J recibe 2 parametros
        cadena = " " #Inicializamos la cadena 
        lista = [] #Creamos una lista vacia 
        for n in self.listado_personas:  #creamos el for para recorrer el listado
            if(b == n.obtener_nombre()[0] or c == n.obtener_nombre()[0]): #IF que comprara el primer caracter del metodo obtener_nombre() con los parametros recibidos
                lista = cadena = "%s -%s - %s"%(cadena,n.obtener_nombre(),n.obtener_apellido()) #De ser afirmativo concatenamos la cadena y la enviamos a lista
        return lista #Devolvemos lista
    def __str__(self): #Metodo STR de la clase similar a toString java
        cadena = " " #Inizialiamos la variable 
        for n in self.listado_personas: #Creamos el for para recorrer la lista
            cadena = "%s - %s - %s\n"%(cadena, n.obtener_nombre(),n.obtener_apellido()) #Creamos la cadena con el valor de los metodos
             
        return cadena #Devolvemos valor de cadena