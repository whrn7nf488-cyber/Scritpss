# MI CALCULADORA EN PYTHON

print("=== CALCULADORA BÁSICA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("\n¿Qué quieres hacer? (1-4): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == "1":
    print(f"Resultado: {num1 + num2}")
elif opcion == "2":
    print(f"Resultado: {num1 - num2}")
elif opcion == "3":
    print(f"Resultado: {num1 * num2}")
elif opcion == "4":
    if num2 == 0:
        print("¡ERROR! No se puede dividir por cero")
    else:
        print(f"Resultado: {num1 / num2}")
else:
    print("Opción inválida")

print("\n¡Gracias por usar la calculadora! ✨")
