import codecs #Importamos codecs
import sys

class MiArchivo: #Creamos la clase MiArchvio
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r") #Leemos el archivo que poseemos 

    def obtener_informacion(self): #metodo para retornar el archivo leido 
        return self.archivo.readlines()

    def cerrar_archivo(self): #Metodo para cerrar el archivo
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """  
        self.archivo = codecs.open("data/demo2.csv", "a") #Utilizamos esta linea de codigo para escribir en esa direccion

    def agregar_informacion(self, p): #Utilizamos el metodo para escribir el nuevo archivo con los parametros establecidos
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self): #Cerramos el archivo
        self.archivo.close()
