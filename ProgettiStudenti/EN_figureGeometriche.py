## Calcolo Area e Perimetro di figure geometriche

def AreaCerchio():
    print("AREA CERCHIO:")
    r= (float(input("inserisci il raggio: ")))
    A= (r**2)*3.14
    Area= (str(input("inserisci la formula dell'area: ")))
    if Area == "(r**2)" or Area == "r**2*3.14":
        print("La risposta è corretta.")
    else:
        print("La risposta è errata. Quella corretta è r**2*3.14")
        
    print("Area=", A)

    
#AreaCerchio()

def CirconferenzaCerchio():
    print("CIRCONFERENZA:")
    r= (float(input("inserisci il raggio: ")))
    C= (r*2)*3.14
    Circonferenza= (str(input("inserisci la formula della circonferenza: ")))
    if Circonferenza == "(r*2)*3.14" or Circonferenza == "r*2*3.14":
        print("La risposta è corretta.")
    else:
        print("La risposta è errata. Quella corretta è r*2*3.14")
        
    print("Circonferenza=", C)
    
#CirconferenzaCerchio()

def AreaTriangolo():
    print("AREA TRIANGOLO: ")
    b= (float(input("inserisci la base: ")))
    h= (float(input("inserisci l'altezza: ")))
    A= (b*h)/2
    Area= (str(input("inserisci la formula: ")))
    if Area == "(b*h)/2" or Area == "b*h/2":
        print("La risposta è corretta")
    else:
        print("La risposta è errata. Quella corretta è b*h/2")
    print("Area=", A)

#AreaTriangolo()

def PerimetroTriangolo():

    print("PERIMETRO TRIANGOLO: ")
    l= (float(input("inserisci il lato: ")))
    l= (float(input("inserisci il lato: ")))
    l= (float(input("inserisci il lato: ")))
    A= l+l+l
    print("Perimetro: ", A)
    
#PerimetroTriangolo()

def menu():
        nome= (str(input("come ti chiami? ")))
        print("Ciao",nome,"!","Di cosa hai bisogno?")
        while True:
            print("1. Stampa Area Cerchio")
            print("2. Stampa Circonferenza")
            print("3. Stampa Area Triangolo")
            print("4. Stampa Perimetro Triangolo")
            print("5. Esci dal programma")
            scelta = int(input("Scegli un'opzione: "))
            if scelta == 1:
                AreaCerchio()
            elif scelta == 2:
                CirconferenzaCerchio()
            elif scelta == 3:
                AreaTriangolo()
            elif scelta == 4:
                PerimetroTriangolo()
            elif scelta == 5:
                uscita= str(input("Sei sicuro di voler uscire? Si/No "))
                if uscita == "si" or "Si" or "SI":
                    print("Grazie per aver usato il programma, arrivederci.")
                    break
            else:
                print("Opzione non valida. Riprova")
                
menu()