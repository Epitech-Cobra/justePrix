from random import randrange

def Main():
    playerOne = input("Comment vous appelez vous ? (Premier joueur) : ")
    price = 1000
    playerInput = 0

    print("Vous devez trouver le juste prix: !")

    playerInput = int(input("Entrez un nombre : "))

    if (playerInput != price):
        print("C'est pas gagné !")



Main()