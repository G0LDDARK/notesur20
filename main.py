__author__ = "GLDDRK"
def main():
    print("En premier entre ta note, puis entre sur combien est ta note, ensuite le programme calculera ta note en note sur 20")
    note = input("Quel est votre note: ")
    sur = input("Sur combient de point: ")
    if note == "AUTHOR":
        if sur == "AUTHOR":
            print("Je suis " + __author__ + " l'auteur de ce code python merci d'avoir demander qui je suis.")
            exit()
    if note or sur != float:
        print("Tu déconne john, " + str(note), "/ " + str(sur) + " ne sont pas des chiffres")
        exit()
    notesur20 = float(note) / float(sur) * 20
    print("Voter note de " + str(note) + " sur " + str(sur) + " est égale a la note de " + str(notesur20) + "/20")
main()