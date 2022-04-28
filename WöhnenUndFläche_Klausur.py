# Liste von Zimmern mit deren Flächen
# Jede Liste enthält das Zimmer und seine Fläche
# Fläche = länge * Breite (FLoat)
# BSP.: Wohnzimmer, 4 qm, 4 qm, Schlafzimmer, 4 qm, 5qm, Küche, 5.2 qm, 4.5 qm
# ==>1.Ausgabe: ['Wohnzimmer, 16qm'], ['Schlafzimmer', 20qm], ['Küche', 23.4qm]
# ==> 2.Ausgabe: alle Listen in einer Liste packen

# 1.Lösung
def fileName(f):
    z1, z2, z3 = f.readline(), f.readline(), f.readline()
    z1, z2, z3 = str(z1), str(z2), str(z3)
    z1, z2, z3 = z1.split(), z2.split(), z3.split()

    flaeche1 = float(z1[1]) * float(z1[2])
    flaeche2 = float(z2[1]) * float(z2[2])
    flaeche3 = float(z3[1]) * float(z3[2])

    liste1 = [z1[0], flaeche1]
    liste2 = [z2[0], flaeche2]
    liste3 = [z3[0], flaeche3]

    # 1.Aufgabe
    print(liste1, liste2, liste3, sep=", ")

    # 2.Aufgabe
    array = [liste1, liste2, liste3]
    print(array)

file = open(r"C:\Users\yazan\Desktop\GPT_Aufgaben\Wohnen.txt", "r")
fileName(file)

#2.Lösung
#def fileName(file):
#    l1 = file.readline()
#    l1 = str(l1)
#    l1 = l1.split()
#    # Fläche des Wohnzimmers
#    fw = float(l1[1])*float(l1[2])
#    del l1[1:]
#    l1.append(fw)
#
#    l2 = file.readline()
#    l2 = str(l2)
#    l2 = l2.split()
#    # Fläche des Schlafzimmers
#    fs = float(l2[1])*float(l2[2])
#    del l2[1:]
#    l2.append(fs)
#
#    l3 = file.readline()
#    l3 = str(l3)
#    l3 = l3.split()
#    # Fläche der Küche
#    fk = float(l3[1])*float(l3[2])
#    del l3[1:]
#    l3.append(fk)
#
#    print(l1, l2, l3, sep=", ") #1.Ausgabe
#    print([l1, l2, l3]) #2.Ausgabe
#
#
#
#f = open(r"C:\Users\yazan\Desktop\GPT_Aufgaben\Wohnen.txt", "r")
#fileName(f)




