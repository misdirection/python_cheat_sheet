# Grundlegende Syntax

# Konsolen-Eingabe und Ausgabe
print("Hallo, Welt!")  # Ausgabe
input("Wie heißt du? ")  # Eingabe

# Variablen
name = "Alice"
alter = 25
pi = 3.14159

# Datentypen
ganzzahl = 10  # int
kommazahl = 3.14  # float
text = "Hallo"  # str
wahrheitswert = True  # bool

# Listen
früchte = ["Apfel", "Banane", "Kirsche"]
print(früchte[0])  # Zugriff auf das erste Element

# Tupel (unveränderliche Listen)
farben = ("rot", "grün", "blau")

# Dictionaries
person = {"name": "Bob", "alter": 30}
print(person["name"])  # Zugriff auf den Wert zum Schlüssel "name"


## Kontrollstrukturen
# Bedingte Anweisungen
if alter > 18:
    print("Erwachsener")
elif alter > 12:
    print("Jugendlicher")
else:
    print("Kind")

# Schleifen
# for-Schleife
for frucht in früchte:
    print(frucht)

# while-Schleife
zähler = 0
while zähler < 5:
    print(zähler)
    zähler += 1


## Funktionen
# Definition einer Funktion
def begrüße(name):
    print(f"Hallo, {name}!")


# Aufruf der Funktion
begrüße("Alice")


# Funktion mit Rückgabewert
def addiere(a, b):
    return a + b


summe = addiere(3, 5)
print(summe)


# Klassen
# Definition einer Klasse
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def bellen(self):
        print(f"{self.name} sagt: Wuff!")


# Erstellen eines Objekts
mein_hund = Hund("Bello", 5)
mein_hund.bellen()  # Aufruf einer Methode


##Wichtige Module
# Importieren eines Moduls
import math

# Verwendung von Funktionen aus dem Modul
print(math.sqrt(16))  # Ausgabe: 4.0

import random

# Zufällige Zahl zwischen 1 und 10
zufallszahl = random.randint(1, 10)
print(zufallszahl)


# Dateien
# Datei öffnen und lesen
with open("datei.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)

# Datei öffnen und schreiben
with open("ausgabe.txt", "w") as datei:
    datei.write("Dies ist eine Zeile Text.\n")


# Fehlerbehandlung
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(f"Das Quadrat der Zahl ist {zahl ** 2}")
except ValueError:
    print("Das war keine gültige Zahl!")
