def area(a,b):
#     a = 5
#     b = 4
    A = a*b
    return A

def area_triangolo(b,h):
    A = b*h/2
    return A

def stampa_area(area):
    print(f"Area: {area}")

A1 = area(6,44)
print(A1)

At = area_triangolo(5,2)
print(At)

stampa_area(A1)