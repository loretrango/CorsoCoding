print("ciao")

def cilindro(r,h):
    pi = 3.14
    Ab = r**2 * pi
    C = 2*pi*r
    
    print("Raggio: ", r)
    
    print("Altezza: ", h)
    print("Circonferenza: ", C)
    print("Area base: ", Ab)

    V = Ab * h
    print("Volume: ", round(V,2))
    Al = C*h
    print("Area laterale: ", Al)
    At = 2*Ab + Al
    print("Area totale: ", At)
    
    print()
    

cilindro(3,7)
cilindro(44,2)
cilindro(1,10)