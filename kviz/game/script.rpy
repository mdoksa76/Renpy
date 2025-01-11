init python:
    import random

    class Pitanje:
        def __init__(self, tekst, odgovori, tocan_odgovor):
            self.tekst = tekst
            self.odgovori = odgovori
            self.tocan_odgovor = tocan_odgovor

    pitanja = [
        Pitanje("Koji je glavni grad Hrvatske?", ["Zagreb", "Split", "Rijeka", "Osijek"], "a"),
        Pitanje("Koja je najduža rijeka u Hrvatskoj?", ["Kupa", "Sava", "Dunav", "Mura"], "b"),
        Pitanje("Tko je napisao 'Tko pjeva zlo ne misli'?", ["August Šenoa", "Ivo Brešan", "Vjekoslav Majer", "Zdenko Runjić"], "c"),
        Pitanje("Koja je valuta u Japanu?", ["Funta", "Euro", "Dolar", "Jen"], "d"),
        Pitanje("Koliko planeta ima u Sunčevom sustavu?", ["8", "9", "7", "10"], "a"),
        Pitanje("Koja je najviša planina na svijetu?", ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"], "b"),
        Pitanje("Koji hrvatski nogometni klub je najtrofejniji u Hrvatskoj?", ["Rijeka", "Hajduk Split", "Dinamo Zagreb", "Osijek"], "c"),
        Pitanje("Tko je bio kapetan hrvatske nogometne reprezentacije na Svjetskom prvenstvu 2018.?", ["Dejan Lovren", "Ivan Rakitić", "Mario Mandžukić", "Luka Modrić"], "d"),
        Pitanje("U kojoj godini je hrvatska nogometna reprezentacija osvojila prvi put brončanu medalju na Svjetskom prvenstvu?", ["1998.", "2002.", "2014.", "2018."], "a"),
        Pitanje("Tko je osvojio zlatnu medalju za Hrvatsku na Olimpijskim igrama u Londonu 2012. u jedrenju?", ["Ivan Kustić", "Šime Fantela", "Marin Čilić", "Sandra Perković"], "b"),
        Pitanje("Koja hrvatska sportašica je višestruka svjetska prvakinja u bacanju diska?", ["Ivana Brkljačić", "Blanka Vlašić", "Sandra Perković", "Sara Kolak"], "c"),
        Pitanje("U kojoj godini je Hrvatska prvi put sudjelovala na Olimpijskim igrama kao samostalna država?", ["1990.", "1996.", "1994.", "1992."], "d"),
        Pitanje("Tko je bio prvi hrvatski tenisač koji je osvojio Grand Slam turnir?", ["Goran Ivanišević", "Marin Čilić", "Ivo Karlović", "Borna Ćorić"], "a"),
        Pitanje("Tko je otkrio diskontinuitet u Zemljinoj kori koji nosi njegovo ime?", ["Nikola Tesla", "Andrija Mohorovičić", "Ivan Vučetić", "Faust Vrančić"], "b"),
        Pitanje("Koji hrvatski znanstvenik je dobio Nobelovu nagradu za kemiju za istraživanja na području organske kemije?", ["Slavoljub Vukmanović", "Ruđer Bošković", "Vladimir Prelog", "Ivan Supek"], "c"),
        Pitanje("Tko je izumio torpeda, koja su revolucionirala pomorsku bitku?", ["Ivo Andrić", "Nikola Tesla", "Faust Vrančić", "Ivan Lupis"], "d"),
        Pitanje("Koji hrvatski izumitelj je poznat po izumu kemijske olovke?", ["Slavoljub Penkala", "Slavko Rožić", "Faust Vrančić", "Ladislav Bíró"], "a"),
        Pitanje("Tko je bio jedan od najvećih svjetskih fizičara, poznat po svojim istraživanjima u području elektriciteta i magnetizma?", ["Ruđer Bošković", "Nikola Tesla", "Andrija Mohorovičić", "Ivan Vučetić"], "b"),
        Pitanje("Koji hrvatski znanstvenik je bio jedan od začetnika moderne geologije?", ["Ruđer Bošković", "Nikola Tesla", "Andrija Mohorovičić", "Faust Vrančić"], "c"),
        Pitanje("Tko je izumio padobran, koji je spasio mnoge živote?", ["Ivan Lupis", "Nikola Tesla", "Andrija Mohorovičić", "Faust Vrančić"], "d"),
        Pitanje("Tko je razvio sustav klasifikacije otisaka prstiju koji je revolucionirao forenziku?", ["Ivan Vučetić", "Ruđer Bošković", "Andrija Mohorovičić", "Nikola Tesla"], "a"),
        Pitanje("Koji hrvatski znanstvenik je bio jedan od prvih koji je proučavao Sunčev sustav?", ["Andrija Mohorovičić", "Ruđer Bošković", "Nikola Tesla", "Faust Vrančić"], "b"),
        Pitanje("Tko je izumio leteći stroj koji je bio jedan od prethodnika modernog aviona?", ["Ivan Lupis", "Nikola Tesla", "Faust Vrančić", "Andrija Mohorovičić"], "c"),
        Pitanje("Tko je među sljedećim znanstvenicima bio Heisenbergov asistent?", ["Ruđer Bošković", "Andrija Mohorovičić", "Nikola Tesla", "Ivan Supek"], "d"),
        Pitanje("Koji je bio prvi hrvatski kralj?", ["Tomislav", "Zvonimir", "Petar Krešimir IV.", "Stjepan Držislav"], "a"),
        Pitanje("Koje godine je Hrvatska postala članica Europske unije?", ["2009.", "2013.", "2015.", "2017."], "b"),
        Pitanje("Koji je hrvatski grad bio glavni grad Hrvatske u srednjem vijeku?", ["Dubrovnik", "Split", "Knin", "Zagreb"], "c"),
        Pitanje("Koji je bio prvi hrvatski predsjednik?", ["Stjepan Mesić", "Zoran Milanović", "Ivo Josipović", "Franjo Tuđman"], "d"),
        Pitanje("Koji je hrvatski povjesničar napisao 'Povijest Hrvata'?", ["Vjekoslav Klaić", "Ivan Kukuljević Sakcinski", "Franjo Rački", "Ferdo Šišić"], "a"),
        Pitanje("Koji je hrvatski grad bio glavni grad Dalmacije u 19. stoljeću?", ["Split", "Zadar", "Dubrovnik", "Šibenik"], "b"),
        Pitanje("Koji je najveći otok u Hrvatskoj?", ["Hvar", "Cres", "Krk", "Brač"], "c"),
        Pitanje("Koji je najviši vrh u Hrvatskoj?", ["Sljeme", "Biokovo", "Velebit", "Dinara"], "d"),
        Pitanje("Koji je najjužniji grad u Hrvatskoj?", ["Dubrovnik", "Split", "Zadar", "Šibenik"], "a"),
        Pitanje("Koji je najveći poluotok u Hrvatskoj?", ["Pelješac", "Istra", "Konavle", "Prevlaka"], "b"),
        Pitanje("Koji je najveći nacionalni park u Hrvatskoj?", ["Krka", "Paklenica", "Plitvička jezera", "Risnjak"], "c"),
        Pitanje("Koji je najveći grad na Jadranskoj obali?", ["Rijeka", "Dubrovnik", "Zadar", "Split"], "d"),
        Pitanje("Koji je najveći grad u Slavoniji?", ["Osijek", "Vukovar", "Slavonski Brod", "Đakovo"], "a"),
        Pitanje("Koji je najveći grad u Istri?", ["Rovinj", "Pula", "Poreč", "Umag"], "b"),
        Pitanje("Tko je autor romana 'Na Drini ćuprija'?", ["Miroslav Krleža", "Ivan Goran Kovačić", "Ivo Andrić", "Antun Gustav Matoš"], "c"),
        Pitanje("Koji je poznati hrvatski slikar autor slike 'Smaknuće Matije Gupca'?", ["Vlaho Bukovac", "Ivan Meštrović", "Edo Murtić", "Oton Iveković"], "d"),
        Pitanje("Tko je režirao film 'Tko pjeva zlo ne misli'?", ["Krešo Golik", "Antun Vrdoljak", "Zvonimir Berković", "Branko Bauer"], "a"),
        Pitanje("Tko je autor romana 'Glembajevi'?", ["Ivo Andrić", "Miroslav Krleža", "Ivan Goran Kovačić", "Antun Gustav Matoš"], "b"),
        Pitanje("Koji je poznati hrvatski kipar autor skulpture 'Grgur Ninski'?", ["Frano Kršinić", "Antun Augustinčić", "Ivan Meštrović", "Vanja Radauš"], "c"),
        Pitanje("Tko je autor romana 'Zlatarovo zlato'?", ["Ivana Brlić Mažurnić", "Ivo Andrić", "Ivan Goran Kovačić", "August Šenoa"], "d"),
        Pitanje("Tko je režirao film 'Bitka na Neretvi'?", ["Veljko Bulajić", "Branko Bauer", "Krešo Golik", "Zvonimir Berković"], "a"),
        Pitanje("Tko je autor romana 'Kiklop'?", ["Miroslav Krleža", "Ranko Marinković", "Ivo Andrić", "Ivan Goran Kovačić"], "b"),
        Pitanje("Koji je poznati hrvatski kipar autor skulpture 'Indijanac'?", ["Frano Kršinić", "Antun Augustinčić", "Ivan Meštrović", "Vanja Radauš"], "c"),
    ]

    def postavi_pitanje(odabrana_pitanja):
        global trenutno_pitanje
        trenutno_pitanje = random.choice(odabrana_pitanja)
        odabrana_pitanja.remove(trenutno_pitanje)
        
        odgovori_tekst = "   |   ".join(["{}. {}".format(chr(97 + i), odgovor) for i, odgovor in enumerate(trenutno_pitanje.odgovori)])
        
        renpy.say(voditelj, "{}\n{}".format(trenutno_pitanje.tekst, odgovori_tekst))
        
        return

    def provjeri_odgovor(odgovor):
        if odgovor == trenutno_pitanje.tocan_odgovor:
            renpy.say(voditelj, "Točno!")
            return True
        else:
            renpy.say(voditelj, "Netočno. Točan odgovor je {}.".format(trenutno_pitanje.tocan_odgovor))
            return False

image bg = "kviz-menu-bg.png"
image voditelj = "voditelj.png"
define voditelj = Character("Voditelj")
define igrac = Character("Igrač")

label start:

    scene bg

    show voditelj at left:
        yalign 0.65
    
    voditelj "Dobrodošli u kviz!"
    
    $ valid_input = False
    while not valid_input:
        $ broj_pitanja = renpy.input("Unesite broj pitanja za kviz (najviše {}):".format(len(pitanja)), allow="0123456789")
        $ renpy.say(voditelj, broj_pitanja)
        if broj_pitanja is None:
            voditelj "Molimo unesite broj."
        elif broj_pitanja.isdigit():
            $ broj_pitanja = int(broj_pitanja)
            if 1 <= broj_pitanja <= len(pitanja):
                $ valid_input = True
            else:
                $ poruka = "Broj pitanja mora biti između 1 i " + str(len(pitanja)) + "."
                $ renpy.say(voditelj, poruka)
        else:
            voditelj "Neispravan unos. Molim unesite broj."

    $ odabrana_pitanja = random.sample(pitanja, broj_pitanja)  # Odabire nasumično broj pitanja iz liste
    
    $ broj_tocnih = 0
    $ pitanje_index = 0

    while pitanje_index < broj_pitanja:
        $ postavi_pitanje(odabrana_pitanja)
        
        $ odgovor = None
        while odgovor not in ["a", "b", "c", "d"]:
            $ odgovor = renpy.input("Odaberite odgovor (a, b, c, d):", allow="abcd")
            if odgovor is None or len(odgovor) != 1:
                voditelj "Molimo odaberite odgovor (a, b, c, d)."
                $ odgovor = None
        
        if provjeri_odgovor(odgovor):
            $ broj_tocnih += 1
        $ pitanje_index += 1

    $ rezultat = "Kviz je završen! Rezultat: " + str(broj_tocnih) + " / " + str(broj_pitanja) + " = " + str(round(100 * broj_tocnih / broj_pitanja, 2)) + " %%"
    $ renpy.say(voditelj, rezultat)

    return
