#version
__version__ = 1.3
#autheur
__author__ = "GLDDRK"

#création de la fonction main
def main():
    #explication de programme
    print("En premier entre ta note, puis entre sur combien est ta note, ensuite le programme calculera ta note en note sur 20")

    #demande de la note
    note = input("Quel est votre note: ")

    #sur combien de point
    sur = input("Sur combient de point: ")

    #petit easter-egg
    # Калашников
    if note == "AUTHOR":
        if sur == "AUTHOR":
            print("Je suis " + __author__ + " l'auteur de ce code python merci d'avoir demander qui je suis.")
            exit()
    #si les deux champs sont remplis par "VESRION" alors le programme donnera sa vesrion
    if note == "VERSION":
        if sur == "VERSION":
            print("Mon autheur a dit que je suis en version " + str(__version__))
            exit()

    #verification si les input sont des float
    if note != float:
        print("Tu déconne john, " + str(note), + " n'est pas un nombre")
        exit()
    if sur != float:
        print("Tu déconne john, " + str(note), + " n'est pas un nombre")
        exit()

    #calcul des input en note sur 20
    notesur20 = float(note) / float(sur) * 20

    #affichage de la note
    print("Voter note de " + str(note) + " sur " + str(sur) + " est égale a la note de " + str(notesur20) + "/20")

#appel de la fonction main
main()