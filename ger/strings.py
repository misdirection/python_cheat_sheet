# String erstellen
text = "Hallo, Welt!"

# Länge eines Strings
print(len(text))  # Ausgabe: 12

# Großbuchstaben
print(text.upper())  # Ausgabe: "HALLO, WELT!"

# Kleinbuchstaben
print(text.lower())  # Ausgabe: "hallo, welt!"

# Entfernen von Leerzeichen am Anfang und Ende
text_mit_leerzeichen = "  Hallo, Welt!  "
print(text_mit_leerzeichen.strip())  # Ausgabe: "Hallo, Welt!"

# Ersetzen eines Substrings
print(text.replace("Welt", "Python"))  # Ausgabe: "Hallo, Python!"

# Aufteilen eines Strings in eine Liste
print(text.split(","))  # Ausgabe: ['Hallo', ' Welt!']

# Überprüfen, ob ein Substring vorhanden ist
print("Welt" in text)  # Ausgabe: True

# Zeichen an einer bestimmten Position
print(text[7])  # Ausgabe: "W"

# Teilstring (Slicing)
print(text[7:12])  # Ausgabe: "Welt!"


# format() Funktion
name = "Alice"
alter = 25

# Einfache Platzhalter
begrüßung = "Hallo, {}!".format(name)
print(begrüßung)  # Ausgabe: "Hallo, Alice!"

# Mehrere Platzhalter
info = "Name: {}, Alter: {}".format(name, alter)
print(info)  # Ausgabe: "Name: Alice, Alter: 25"

# Benannte Platzhalter
info_benannt = "Name: {n}, Alter: {a}".format(n=name, a=alter)
print(info_benannt)  # Ausgabe: "Name: Alice, Alter: 25"

# Formatierung von Zahlen
pi = 3.14159
print("Pi ist ungefähr {:.2f}".format(pi))  # Ausgabe: "Pi ist ungefähr 3.14"

# Platzhalter mit Index
text = "Der {0} hat {1} und der {2} hat {3}".format(
    "Hund", "gebellt", "Vogel", "gesungen"
)
print(text)  # Ausgabe: "Der Hund hat gebellt und der Vogel hat gesungen"
