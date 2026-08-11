#Escribir un programa que verifique si una cadena o número se lee igual hacia adelante que hacia atrás
def is_palindrome(s):
    # Convertir a cadena y eliminar espacios y convertir a minúsculas
    s = str(s).replace(" ", "").lower()
    return s == s[::-1]

# Prueba el código corregido con varias cadenas y números, incluidos los casos límite.

if __name__ == "__main__":
    test_cases = [
        "A man a plan a canal Panama",
        "racecar",
        "hello",
        12321,
        12345
    ]

    for case in test_cases:
        result = is_palindrome(case)
        print(f"Is '{case}' a palindrome? {result}")