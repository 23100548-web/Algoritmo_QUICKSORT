def quicksort(arr):
    # caso de base
    if len(arr) <= 1:
        return arr
    
    # elegir pivote 
    pivote = arr[len(arr) // 2]
    
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # llamada recursivas
    return quicksort(menores) + iguales + quicksort(mayores)

# sentencias

def pruebas_cobertura_sentencias():
    print("Pruebas de Cobertura de Sentencias")
    
    # Caso base (lista vacía)
    assert quicksort([]) == []
    
    # Caso base (un elemento)
    assert quicksort([5]) == [5]
    
    # Caso general
    assert quicksort([20,10,8,5,6,10,2]) == [2,5,6,8,10,10,20]
    
    # Elementos repetidos
    assert quicksort([3, 3, 3]) == [3, 3, 3]
    
    # Lista ordenada
    assert quicksort([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    print(" Cobertura de sentencias completada\n")



# desiciones

def pruebas_cobertura_decisiones():
    print("Pruebas de Cobertura de Decisiones")
    
    # Decisión TRUE
    assert quicksort([]) == []
    
    # Decisión TRUE
    assert quicksort([1]) == [1]
    
    # Decisión FALSE
    assert quicksort([3, 1, 2]) == [1, 2, 3]
    
    print("Cobertura de decisiones completada\n")


if __name__ == "__main__":
    pruebas_cobertura_sentencias()
    pruebas_cobertura_decisiones()
    print(" Todas las pruebas pasaron correctamente")