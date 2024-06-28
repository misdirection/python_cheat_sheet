import turtle

# Fenster einrichten
fenster = turtle.Screen()  # Erstellt ein Grafikfenster
fenster.bgcolor("white")  # Setzt die Hintergrundfarbe des Fensters
fenster.title("Turtle Grafik")  # Setzt den Titel des Fensters

# Turtle einrichten
zeichner = turtle.Turtle()  # Erstellt eine neue Turtle
zeichner.shape("turtle")  # Setzt die Form der Turtle
zeichner.color("blue")  # Setzt die Farbe der Turtle
zeichner.speed(5)  # Setzt die Geschwindigkeit der Turtle (1-10, 0 ist am schnellsten)

# Bewegungsfunktionen
zeichner.forward(100)  # Bewegt die Turtle 100 Einheiten vorwärts
zeichner.backward(50)  # Bewegt die Turtle 50 Einheiten rückwärts
zeichner.right(90)  # Dreht die Turtle 90 Grad nach rechts
zeichner.left(90)  # Dreht die Turtle 90 Grad nach links
zeichner.goto(0, 0)  # Bewegt die Turtle zu den Koordinaten (0, 0)
zeichner.setpos(50, 50)  # Bewegt die Turtle zu den Koordinaten (50, 50)
zeichner.setheading(45)  # Setzt die Richtung der Turtle auf 45 Grad
zeichner.home()  # Bewegt die Turtle zurück zum Ursprung (0, 0)
zeichner.circle(50)  # Zeichnet einen Kreis mit Radius 50

# Stiftfunktionen
zeichner.penup()  # Hebt den Stift an, Turtle bewegt sich ohne zu zeichnen
zeichner.pendown()  # Senkt den Stift ab, Turtle zeichnet beim Bewegen
zeichner.pensize(3)  # Setzt die Dicke des Stifts auf 3
zeichner.pencolor("red")  # Setzt die Stiftfarbe auf Rot
zeichner.fillcolor("yellow")  # Setzt die Füllfarbe auf Gelb

# Beginnt einen Füllbereich
zeichner.begin_fill()
zeichner.circle(50)  # Zeichnet einen Kreis, der gefüllt wird
zeichner.end_fill()  # Beendet den Füllbereich

# Bildschirmfunktionen
fenster.bgcolor("lightblue")  # Setzt die Hintergrundfarbe des Fensters auf Hellblau
fenster.title("Mein Turtle Fenster")  # Setzt den Titel des Fensters
fenster.setup(width=800, height=600)  # Setzt die Größe des Fensters auf 800x600 Pixel
fenster.clear()  # Löscht den Bildschirm
fenster.bye()  # Schließt das Turtle-Grafikfenster

# Zeichenfunktionen
zeichner.dot(20, "green")  # Zeichnet einen Punkt mit Durchmesser 20 und Farbe Grün
zeichner.write("Hallo, Welt!", move=False, align="center", font=("Arial", 16, "normal"))
# Schreibt Text "Hallo, Welt!" an der aktuellen Position der Turtle
