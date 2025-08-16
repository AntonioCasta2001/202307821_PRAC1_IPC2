from Libro_Fisico import Libro_Fisico
from libro_digital import Libro_Digital
def acerca_de(libro):
    print(libro.informacion())
biblioteca = []

if __name__ == "__main__":
    libro_fisico = None
    libro_digital = None
    while True:
        print('---------------Menu Principal---------------')
        print('|1. Agregar Libro Fisico                   |')
        print('|2. Agregar Libro Digital                  |')
        print('!3. Mostrar Libros Disponibles             |')
        print('|4. Prestar Libro                          |')
        print('|5. Devolver Libro                         |')
        print('|6. Buscar Libro Digital                   |')
        print('|7. Buscar Libro Fisico                    |')
        print('|8. Salir                                  |')
        print('--------------------------------------------')
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            titulo = input("Ingrese un titulo: ")
            autor = input("Ingrese un autor: ")
            no_ejemplar = input("Ingrese el numero de ejemplar: ")
            libro_fisico = Libro_Fisico(titulo, autor, no_ejemplar)
            biblioteca.append(libro_fisico)
        elif opcion == 2:
            titulo = input("Ingrese un titulo: ")
            autor = input("Ingrese un autor: ")
            tamaño_archivo=input("Ingrese el tamaño del archivo en MB: ")
            libro_digital = Libro_Digital(titulo, autor, tamaño_archivo)
            biblioteca.append(libro_digital)
        elif opcion == 3:
            i=0
            for libro in biblioteca:
                print("#",i+1)
                libro.informacion()
                i+=1
        elif opcion == 4:
            codigo = input("Ingrese el código del libro a prestar: ")
            encontrado = False
            for material in biblioteca:
                while material.codigo == codigo:
                    material.prestar_libro()
                    encontrado = True
                    break
            if encontrado==False:
                print("Error: Libro no encontrado.")
        elif opcion == 5:
            codigo = input("Ingrese el codigo del libro a devolver: ")
            encontrado = False
            for libro in biblioteca:
                if libro.codigo == codigo:
                    libro.devolver_libro()
                    encontrado=True
                    break
            while encontrado == False:
                print("El libro no pertenece ala biblioteca")
                break
        elif opcion == 6:
            codigo = input("Ingrese el codigo del libro a buscar: ")
            for libro in biblioteca:
                if libro.codigo == codigo:
                    print(f"El libro {titulo} | autor: {autor} | tamaño: {tamaño_archivo}")
                    break
                else:
                    print("no se encuentra disponible")
        elif opcion == 7:
            codigo = input("Ingrese el codigo del libro a buscar: ")
            for libro in biblioteca:
                if libro.codigo == codigo:
                    print(f"El libro {titulo} | autor: {autor} | numero de ejemplar: {no_ejemplar}")
                    break
                else:
                    print("no se encuentra disponible")
        elif opcion == 8:
            print("saliendo del programa...")
            break
        else:
            print("Error: Elija una de las opciones disponibles")
#referencia: https://stackoverflow.com/questions/61205931/how-do-i-generate-a-random-alphanumeric-string-in-python
