#importation du module os
import os

#version
__version__ = str("1.9.2")

#Autheur
__author__ = str("GLDDRK")

#fonction main()
def main():
    #clear console
    os.system("clear||cls")

    #expliction du script
    print("En premier entre ta note, puis entre sur combien est ta note, ensuite le script calculera ta note en note sur 20 \n(Attention si vous n'entrer pas des nombres le script bugra vous devrez le relancer)")

    #demande de la note
    note = input("Quel est votre note: ")

    #su combien est la note
    sur = input("Sur combient de point: ")
    # Калашников

    #easter-egg
    if note == "AUTHOR":
        if sur == "AUTHOR":
            print("Je suis " + str(__author__) + " l'auteur de ce code python, merci d'avoir demander qui je suis.")
            exit()

    #si les deux entrée son VERSION le script donne sa version
    if note == "VERSION":
        if sur == "VERSION":
            print("Mon autheur a dit que je suis en version " + str(__version__))
            exit()

    #calcule de la note
    notesur20 = float(note) / float(sur) * 20

    #affichage de la note
    print("Votre note de " + str(note) + " sur " + str(sur) + " est égale a la note de " + str(notesur20) + "/20")

    #damande si il vet recommancer
    restart = input("Voulez vous recommencer? (O/n)?")

    #si oui recomancer
    if restart == "O":
        os.system("clear||cls")
        main()

    #sinon fermer le script
    else:
        os.system("clear||cls")
        exit()

#execution fonction main()
main()
