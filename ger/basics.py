# Kommentar
print("Hallo, Welt!")  # Ausgabe

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
