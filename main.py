import os
__version__ = str("1.9.3")
__author__ = str("GLDDRK")
def main():
    os.system("clear||cls")
    print("En premier entre ta note, puis entre sur combien est ta note, ensuite le script calculera ta note en note sur 20 \n(Attention si vous n'entrer pas des nombres le script bugra vous devrez le relancer)")
    note = input("Quel est votre note: ")
    sur = input("Sur combient de point: ")
    # Калашников
    if note == "AUTHOR":
        if sur == "AUTHOR":
            print("Je suis " + str(__author__) + " l'auteur de ce code python, merci d'avoir demander qui je suis.")
            exit()
    if note == "VERSION":
        if sur == "VERSION":
            print("Mon autheur a dit que je suis en version " + str(__version__))
            exit()
    notesur20 = float(note) / float(sur) * 20
    print("Votre note de " + str(note) + " sur " + str(sur) + " est égale a la note de " + str(notesur20) + "/20")
    restart = input("Voulez vous recommencer? (O/n)?")
    if restart == "O":
        os.system("clear||cls")
        main()
    else:
        os.system("clear||cls")
        exit()
main()