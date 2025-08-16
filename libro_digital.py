from Material_Biblioteca import MaterialBiblioteca

class Libro_Digital(MaterialBiblioteca):
    def __init__(self, titulo, autor,tamaño_archivo):
        super().__init__(titulo, autor)
        self.__tamaño_archivo=tamaño_archivo
        self._prestamo = 3

    def gettamaño(self):
        return self.__tamaño_archivo
        
    def settamaño(self,tamaño_archivo):
        self.__tamaño_archivo=tamaño_archivo
    def informacion(self):
        super().informacion()
        print(f"Tamaño del libro: {self.gettamaño()} MB")
        print(f"Dias maximo de prestamo: {self._prestamo}")
        
