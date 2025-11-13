### 🔹 **Esercizio 1: Conta fino a 10**
'''Scrivi un programma che utilizzi un ciclo `while` per stampare i numeri da 1 a 10.

💡 **Suggerimento**: Usa una variabile che parte da 1 e aumenta di 1 in ogni iterazione.
'''

n = 1
while n <= 10:
    print(n)
    n += 1


### 🔹 **Esercizio 2: Somma dei numeri**
Scrivi un programma che chieda all’utente di inserire numeri interi. Il programma deve continuare a sommare i numeri inseriti finché l’utente non inserisce `0`. Alla fine, il programma deve stampare la somma totale.

#**Suggerimento**: Usa una variabile per memorizzare la somma.


somma = 0
num = int(input("Inserisci un numero (0 per terminare): "))

while num != 0:
    somma += num
    num = int(input("Inserisci un numero (0 per terminare): "))

print("La somma totale è:", somma)


### 🔹 **Esercizio 3: Indovina il numero**
# Scrivi un programma che sceglie un numero segreto (per esempio `7`) e chiede all’utente di indovinarlo. Il programma deve continuare a chiedere finché l’utente non indovina.

# **Suggerimento**: Confronta il numero inserito con quello segreto.

numero_segreto = 7
tentativo = int(input("Indovina il numero segreto: "))

while tentativo != numero_segreto:
    print("Sbagliato! Riprova.")
    tentativo = int(input("Indovina il numero segreto: "))

print("Bravo! Hai indovinato.")

### 🔹 **Esercizio 4: Tabellina con while**
Chiedi all’utente un numero e stampa la sua tabellina fino a 10 usando un ciclo `while`.

💡 **Suggerimento**: Usa una variabile contatore per moltiplicare.

```python
n = int(input("Inserisci un numero per vedere la tabellina: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
```

---

### 🔹 **Esercizio 5: Conto alla rovescia**
Scrivi un programma che chiede un numero all’utente e stampa il conto alla rovescia fino a 0.

💡 **Suggerimento**: La variabile deve diminuire ad ogni ciclo.

```python
n = int(input("Inserisci un numero per il conto alla rovescia: "))

while n >= 0:
    print(n)
    n -= 1

print("Boom! 🎇")
```

---

Questi esercizi aiuteranno gli studenti a comprendere il funzionamento del ciclo `while`. Vuoi che li trasformi in una scheda stampabile? 😊
