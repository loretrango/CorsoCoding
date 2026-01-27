# problema di geometria pag.80 e.63 (questo è un commento)
# tutto in cm

r1 = 5
r2 = 10
pi = 3.14

A1 = r1**2 * pi
A2 = r2**2 * pi

print("A1:", A1)
print("A2:", A2)


## Problema parallelepipedo, calcolare la superficie totale e il volume

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

print("-----")
## Problema acquario a forma di parallelepipedo, misure in cm, a=45 x b=41 x h=105
# prezzo vetro 40euro/m2, calcolare il costo del vetro necessario per costruire l'acquario
# il vetro si trova su tutte le superfici compresa la base e il coperchio
print("Acquario")

# dati
print("Dati:")
a = 45
h = 41
b = 105
costo_vetro_per_m2 = 40  # euro
print("Costo vetro per m2 (euro):", costo_vetro_per_m2)
print("Dimensioni acquario (cm):", a, "x", b, "x", h)

# svolgimento
print("Svolgimento:")
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

At_m2 = At / 10000  # convertire cm2 in m2
costo_totale_vetro = At_m2 * costo_vetro_per_m2
print("Costo totale vetro (euro):", costo_totale_vetro)
# fine problema acquario

########
# Parallelepipedo a=18, b=32, h=33
# Calcoloare volume, area totale, area laterale, area base
print("-----")
print("Parallelepipedo")
a = 18
b = 32
h = 33
Ab = a*b
P = 2*a + 2*b
Al = P*h
At = 2*Ab + Al
V = Ab*h
print("Area base:", Ab, "cm2")
print("Area laterale:", Al, "cm2")
print("Area totale:", At, "cm2")
print("Volume:", V)
# volume in litri
print("Un litro equivale a 1dm3 ovvero 1000 cm3")
V_litri = V / 1000  # convertire cm3 in litri
print("Volume (litri):", V_litri)   
# fine problema parallelepipedo
