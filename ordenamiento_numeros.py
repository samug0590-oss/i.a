
# Reto 1: Programa a una persona
# Ordenar tres números de menor a mayor

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a <= b and b <= c:
    print(a, b, c)

elif a <= c and c <= b:
    print(a, c, b)

elif b <= a and a <= c:
    print(b, a, c)

elif b <= c and c <= a:
    print(b, c, a)

elif c <= a and a <= b:
    print(c, a, b)

else:
    print(c, b, a)
