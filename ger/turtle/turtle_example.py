import turtle

# Fenster einrichten
fenster = turtle.Screen()
fenster.bgcolor("white")
fenster.title("Turtle Grafik Beispiel")

# Turtle einrichten
zeichner = turtle.Turtle()
zeichner.shape("turtle")
zeichner.color("blue")
zeichner.speed(5)


# Funktion, um eine Spirale zu zeichnen
def zeichne_spirale():
    abstand = 10  # Abstand zwischen den Spiralwindungen
    winkel = 30  # Winkel für die Drehung
    for _ in range(36):  # 36 * 10 Grad = 360 Grad (eine komplette Umdrehung)
        zeichner.forward(abstand)
        zeichner.right(winkel)
        abstand += 2  # Abstand wird bei jeder Iteration vergrößert


# Funktion aufrufen
zeichne_spirale()

# Warten auf Benutzereingabe, um das Fenster zu schließen
turtle.done()
