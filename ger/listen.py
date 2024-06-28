# Listen
fruechte = ["Apfel", "Banane", "Kirsche"]
print(fruechte[0])  # Zugriff auf das erste Element


# Liste hinzufuegen
fruechte.append("Orange")  # Hinzufuegen am Ende
print(fruechte)  # Ausgabe: ['Apfel', 'Banane', 'Kirsche', 'Orange']

# Element an einer bestimmten Position einfuegen
fruechte.insert(1, "Mango")
print(fruechte)  # Ausgabe: ['Apfel', 'Mango', 'Banane', 'Kirsche', 'Orange']

# Element entfernen
fruechte.remove("Banane")
print(fruechte)  # Ausgabe: ['Apfel', 'Mango', 'Kirsche', 'Orange']

# Element an einer bestimmten Position entfernen
entferntes_element = fruechte.pop(2)
print(entferntes_element)  # Ausgabe: 'Kirsche'
print(fruechte)  # Ausgabe: ['Apfel', 'Mango', 'Orange']

# Letztes Element entfernen
letztes_element = fruechte.pop()
print(letztes_element)  # Ausgabe: 'Orange'
print(fruechte)  # Ausgabe: ['Apfel', 'Mango']

# Liste umkehren
fruechte.reverse()
print(fruechte)  # Ausgabe: ['Mango', 'Apfel']

# Liste kopieren
fruechte_kopie = fruechte.copy()
print(fruechte_kopie)  # Ausgabe: ['Mango', 'Apfel']

# Liste leeren
fruechte.clear()
print(fruechte)  # Ausgabe: []

# Anzahl der Vorkommen eines Elements zaehlen
fruechte = ["Apfel", "Banane", "Kirsche", "Apfel"]
anzahl_apfel = fruechte.count("Apfel")
print(anzahl_apfel)  # Ausgabe: 2

# Index eines Elements finden
index_banane = fruechte.index("Banane")
print(index_banane)  # Ausgabe: 1

# Liste erweitern
fruechte.extend(["Orange", "Mango"])
print(fruechte)  # Ausgabe: ['Apfel', 'Banane', 'Kirsche', 'Apfel', 'Orange', 'Mango']
