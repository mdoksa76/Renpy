# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg Jesenovec = "Jesenovec.jpg"
image bg room = "matrix.jpg"

define MD76 = Character("MD76")
define Daniel = Character("Daniel")
image Daniel = "daniel.png"
define Gabriel = Character("Gabriel")
image Gabriel = "gabriel.png"
define Monika = Character("Monika")
image Monika = "monika.png"

# The game starts here.

label start:

    scene bg room

    MD76 "Dobar dan!"

    menu:
        "Računanje +, -, *, /, ^":
            jump matematika
        "Matematički izraz":
            jump mathematica
        "LOGARITAM log_baza(broj)":
            jump logaritam
        "Characters":
            jump characters
        "Audio":
            jump audio
        "Video":
            jump video
        "Animacija #1":
            jump animacija

label matematika:

    MD76 "Znam računati. Provjeri!"

    python:
        import math

        x=renpy.input("x = ", allow="0123456789.-")
        op=renpy.input("operacija = ", allow="+-*/^")
        y=renpy.input("y = ", allow="0123456789.-")

        x=float(x)
        y=float(y)

        if op == "+":
            reza=x+y
        elif op =="-":
            reza=x-y
        elif op == "*":
            reza=x*y
        elif op == "/":
            reza=x/y
        elif op == "^":
            reza=x**y

    MD76 "[x][op][y]=[reza]"

    jump start

label mathematica:

    python:
        from math import *

        i = renpy.input("Matematički zadatak: ", allow="0123456789.,-+*/()absincopthlge")

        r = float(eval(i))

    MD76 "[i] = [r]"

    jump start

label logaritam:

    python:
        import math

        baza=renpy.input("baza = ", allow="0123456789.-")
        broj=renpy.input("broj = ", allow="0123456789.-")

        x=float(baza)
        y=float(broj)

        reza=math.log(y,x)

    MD76 "log_[x]([y]) = [reza]"

    jump start

label characters:

    show Gabriel at left
    Gabriel "Gabriel Dokša, 24.4.2008."

    show Daniel at right
    Daniel "Daniel Dokša, 5.11.2009."

    show Monika at center
    Monika "Monika Dokša, 14.6.2013."

    MD76 "Pozdrav bando!"

    show Gabriel at ididesno

    MD76 "Gdje ćeš Dugi?"

    show Monika at ididesno
    MD76 ""
    hide Monika with fade
    MD76 ""
    hide Daniel with pixellate
    MD76 ""
    MD76 "Gdje ste zbrisali, učiti treba?!"
    MD76 ""

    jump start

label audio:

    play sound "kamera.mp3"

    jump start

label video:

    $ renpy.movie_cutscene("movies/Tani-By-Mikulic-1982.webm")

    jump start

label animacija:

    scene bg Jesenovec
    show ptica at ididesno

    MD76 "Pozdrav!"

    jump start

# This ends the game.

return
