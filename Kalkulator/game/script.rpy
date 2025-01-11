image bg = "menu-matematika.png"
image ploca ="ploca.png"
image mate = "mate.png"
image tika = "tika.png"
define mate = Character("Mate")
define tika = Character("Tika")

label start:

    scene bg

    show mate at left
    show tika at right

    "Kalkulator matematičkih zadataka  - podržani složeni izrazi osnovnih matematičkih operacija sa zagradama, apsolutnim vrijednostima, potencijama, logaritmima, trigonometrijskim funkcijama."

    scene ploca
    show mate at left
    show tika at right

    menu:
        "Unesi matematički zadatak:":
            jump matematika
        "Pomoć:":
            jump pomoć

    return

label matematika:

    python:
        from math import *

        i = renpy.input("Matematički zadatak: ", allow="0123456789.,-+*/()absincopthlge")

        r = float(eval(i))

    $ charlist = [mate, tika]
    $ char = renpy.random.choice(charlist)
    $ renpy.say(char, "[i] = [r]")

    jump start

label pomoć:

    "Apsolutna vijednost broja unosi se kao abs(broj). Primjer za -10: abs(-10)."
    "Potencija se unosi korištenjem **. Primjer za ´3 na 7´: 3**7."
    "Kut u stupnjevima se unosi kao kut*pi/180. Primjer za kut od 90°: sin(90*pi/180)."
    "Logaritam broja se unosi u obliku log(broj,baza). Primjer za logaritam od 8 u bazi 2: log(8,2)."
    "Ako se unese samo log(broj), onda se računa logaritam u bazi e. Primjer: log(e)."

    jump start
