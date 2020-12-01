#version
__version__ = 1.5

#auteur
__author__ = "GLDDRK"

#creation de la fonction main
def main():
    #explcation du programme
    print("En premier entre ta note, puis entre sur combien est ta note, ensuite le programme calculera ta note en note sur 20")

    #demande de la note
    note = input("Quel est votre note: ")

    #sur combien
    sur = input("Sur combient de point: ")
    # Калашников

    #petit easter-egg
    if note == "AUTHOR":
        if sur == "AUTHOR":
            print("Je suis " + __author__ + " l'auteur de ce code python, merci d'avoir demander qui je suis.")
            exit()

    #si "VERSION" est dans les deux input afficher la version du progamme
    if note == "VERSION":
        if sur == "VERSION":
            print("Mon autheur a dit que je suis en version " + str(__version__))
            exit()

    notesur20 = float(note) / float(sur) * 20
    print("Votre note de " + str(note) + " sur " + str(sur) + " est égale a la note de " + str(notesur20) + "/20")
main()