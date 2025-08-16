from Material_Biblioteca import MaterialBiblioteca

class Libro_Fisico(MaterialBiblioteca):
    def __init__(self, titulo, autor,no_ejemplar):
        super().__init__(titulo, autor)
        self.__no_ejemplar=no_ejemplar
        self.dias_prestamos=7

    def getejemplar(self):
        return self.__no_ejemplar
        
    def setejemplar(self,no_ejemplar):
        self.__no_ejemplar=no_ejemplar

    def informacion(self):
        super().informacion()
        print(f"Número de ejemplar: {self.__no_ejemplar}")
        print(f"Días máximos de préstamo: {self.dias_prestamos}")
        

