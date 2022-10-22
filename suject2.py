from random import randrange

def Main():
    playerOne = input("Comment vous appelez vous ? (Premier joueur) : ")
    price = 100
    i = 0
    playerInput = 0
    maxTry = 10
    print("Vous devez trouver le juste prix: !")

    while i < maxTry:
        i += 1
        playerInput = int(input("Entrez un nombre : "))
        if (playerInput != price):
            print(f"C'est pas gagné, il vous reste {maxTry - i} essais !")



Main()