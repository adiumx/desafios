#Escribir un programa que elimine los elementos duplicados de un array, asegurando que solo queden elementos únicos.
def remove_duplicates(arr):
    return list(set(arr))

# Ejemplo de uso
if __name__ == "__main__":
    array = [1, 2, 2, 3, 4, 4, 5]
    unique_array = remove_duplicates(array)
    print("Array original:", array)
    print("Array sin duplicados:", unique_array)

#Prueba con varios arrays (incluidos los casos límite).

    test_arrays = [
        [1, 2, 2, 3, 4, 4, 5],
        [1, 1, 1, 1],
        [],
        [5, 5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 2, 1],
        ['a', 'b', 'a', 'c', 'b'],
        [True, False, True],
        [None, None, None],
    ]

    for i, test_array in enumerate(test_arrays):
        unique_array = remove_duplicates(test_array)
        print(f"Test {i + 1}: Original: {test_array} -> Sin duplicados: {unique_array}")