def generador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Ejemplo de uso
if __name__ == "__main__":
    fibonacci = generador_fibonacci()
    for _ in range(10):
        print(next(fibonacci))