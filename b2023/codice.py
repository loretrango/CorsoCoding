# problema di geometria pag.80 e.63 (questo è un commento)
# tutto in cm

r1 = 5
r2 = 10
pi = 3.14

A1 = r1**2 * pi
A2 = r2**2 * pi

print("A1:", A1)
print("A2:", A2)


## Problema cilindro. Calcolare il volume e la superficie totale di un cilindro
## dati raggio della base e altezza

a = 5
b = 3
h = 10

Ab = a*b
print("Area base:", Ab)

P = 2*a + 2*b
print("Perimetro base:", P)

Al = P*h
print("Area laterale:", Al)
At = 2*Ab + Al
print("Area totale:", At)

V = Ab*h
print("Volume:", V)
# fine problema cilindro

