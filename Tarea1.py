

#def crear_matriz(tamanio_matriz):

class matriz:
    def __init__(self, tamanio_matriz):
        self.tamanio_matriz = tamanio_matriz

    def suma_filas(self, tamanio_matriz):
        int(self.tamanio_matriz)
        nummero = self.tamanio_matriz*self.tamanio_matriz
        suma_numeros = (nummero*(nummero + 1))/2
        suma_filas_columnas = suma_numeros/self.tamanio_matriz
        print("La suma de cada fila, columna y diagonal debe ser:", str(suma_filas_columnas))
