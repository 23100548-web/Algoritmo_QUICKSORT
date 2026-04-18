def quicksort(arr):
    """
    Ordena una lista de elementos utilizando el algoritmo recursivo Quicksort.
    """
    # Caso base
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote y crear sublistas
    pivote = arr[len(arr) // 2]
    
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Llamadas recursivas
    return quicksort(menores) + iguales + quicksort(mayores)

if __name__ == "__main__":
    array = [20, 10, 8, 5, 6, 10, 2]
    ordenado = quicksort(array)

    print("Array original:", array)
    print("Array ordenado:", ordenado)