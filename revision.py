# Máximo, mínimo y longitud de un array sin usar librerías

def maximo_array(arr):
    if not arr:
        return None
    max_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num
    return max_value


def minimo_array(arr):
    if not arr:
        return None
    min_value = arr[0]
    for num in arr[1:]:
        if num < min_value:
            min_value = num
    return min_value


def longitud_array(arr):
    count = 0
    for _ in arr:
        count += 1
    return count


if __name__ == "__main__":
    datos = [1, 2, 100, 4, 5]
    print("El máximo del array es:", maximo_array(datos))
    print("El mínimo del array es:", minimo_array(datos))
    print("La longitud del array es:", longitud_array(datos))
