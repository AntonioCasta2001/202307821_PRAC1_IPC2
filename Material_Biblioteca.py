from abc import ABC, abstractmethod
import random
import string

class MaterialBiblioteca(ABC):
    def __init__(self,titulo,autor):
        self.__titulo = titulo
        self.__autor = autor
        self.prestado = False
        self.codigo = self.generar_codigo()
    def generar_codigo(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    def prestar_libro(self):
        if self.prestado == False:
            self.prestado = True
            print(f"{self.__titulo} acaba de ser prestado")
        else:
            print(f"el libro {self.__titulo} se encuentra prestado")
    def devolver_libro(self):
        if self.prestado == True:
            self.prestado = False
            print(f"Libro '{self.__titulo}' ha sido devuelto de manera exitosa")
        else:
            print(f"El Libro '{self.__titulo}' no se encuentra en estado de prestamo")
    def gettitulo(self):
        return self.__titulo
    def settitulo(self,titulo):
        self.__titulo = titulo

    def getautor(self):
        return self.__autor
    def setautor(self,autor):
        self.__autor = autor
    @abstractmethod
    def informacion(self):
        print(f"Título: {self.gettitulo()}")
        print(f"Autor: {self.getautor()}")
        print(f"Código: {self.codigo}")