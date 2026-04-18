from algorit import quicksort

# Cobertura de sentencias
def pruebas_cobertura_sentencias():
    print("Pruebas de Cobertura de Sentencias")
    
    # Caso base (lista vacía)
    assert quicksort([]) == []
    
    # Caso base (un elemento)
    assert quicksort([5]) == [5]
    
    # Caso general
    assert quicksort([20, 10, 8, 5, 6, 10, 2]) == [2, 5, 6, 8, 10, 10, 20]
    
    # Elementos repetidos
    assert quicksort([3, 3, 3]) == [3, 3, 3]
    
    # Lista ya ordenada
    assert quicksort([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    print("Cobertura de sentencias completada\n")

# Cobertura de decisiones
def pruebas_cobertura_decisiones():
    print("Pruebas de Cobertura de Decisiones")
    
    # Decisión TRUE (entra al if len(arr) <= 1)
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    
    # Decisión FALSE (pasa al resto del código)
    assert quicksort([3, 1, 2]) == [1, 2, 3]
    
    print("Cobertura de decisiones completada\n")

if __name__ == "__main__":
    pruebas_cobertura_sentencias()
    pruebas_cobertura_decisiones()
    print("Todas las pruebas pasaron correctamente")