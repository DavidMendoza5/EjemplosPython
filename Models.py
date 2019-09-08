

def matriz():
    matrix = []
    rows = int(input("Ingresa el número de filas: "))
    columns = int(input("Insert the number of columns that you want: "))

    for c in range(rows):
        matrix.append([0]*columns)

        for i in range(rows):
            for j in range(columns):
                matrix[i][j] = int(input("a [%d][%d]= "%(i,j)))
    print(matrix)