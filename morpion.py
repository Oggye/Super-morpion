import random

#présentation et consigne du jeu 
print("Bienvenue dans le super morpion!!")
print("Voici les consigne: ")
print("-tu dois choisir une colone et la ligne entre 0 et 2 pour mettre ton X dans le jeu ")
print("-tu es le Joueur: X")
print("-ton Ennemi est : O") 
print("Que la partie commence! \n") 

#fonction qui affiche la grille 
def afficher_grille(grille):
    for ligne in grille:
        print("".join(ligne))

#fonction qui vérifie la victoire pour l'adversaire et le joueur
def verifier_victoire(grille,symbole):
  
    for i in range(3):
        #Vérification de la victoire si le pion est aligné horizontalement(ligne)
        if grille[i][0]==grille[i][1]==grille[i][2]==symbole:
            return True
        #Vérification de la victoire si le pion est aligné verticalement(colonne)
        if grille[0][i]==grille[1][i]==grille[2][i]==symbole:
            return True

   
    #Vérification de la victoire si le pion est aligné à la diagonale (de gauche à droite)
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    #Vérification de la victoire si le pion est aligné à la diagonale (de droite à gauche)
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False

#fonction qui permet au joueur de placer un pion
def tour_joueur(grille):
    joueur="X"
    while True:
        colonne=int(input("\nSaisir une colonne entre 0 et 2: "))
        ligne=int(input("Saisir une ligne entre 0 et 2: "))
        if 0<=colonne<3 and 0<=ligne<3 and grille[ligne][colonne]=="-":
            grille[ligne][colonne]=joueur
            return colonne,ligne
        else:
            print("case deja remplie, réessaye")

#cette fonction permet a l'ennemi de placer un pion dans la grille de maniére aléatoire
def tour_ennemi(grille):
   print("\nA l'ennemi maintenant\n")
   ennmi="O"
   while True:
    colonne=random.randint(0,2)
    ligne=random.randint(0,2)
    if grille[ligne][colonne]=="-":
        grille[ligne][colonne]=ennmi
        return colonne,ligne
    
#fonction qui gère le déroulement du jeu 
def jouer():
    grille=[["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

    while True:
        #Vérification de la victoire du joueur
        afficher_grille(grille)
        tour_joueur(grille)
        if verifier_victoire(grille,"X"):
            afficher_grille(grille)
            print("\nT'AS GAGNE !\n")
            break
    
        #Vérification du match nul
        if not any("-" in ligne for ligne in grille):
            afficher_grille(grille)
            print("GAME OVER !")
            break

        #Vérification de la victoire de l'ennemi
        tour_ennemi(grille)
        if verifier_victoire(grille,"O"):
            afficher_grille(grille)
            print("\nL'ennemi a gagné la bataille mais pas la guerre.\n")
            break

    #proposition au joueur de relancer ou non le jeu 
    replay=input("Voulez-vous rejouer oui ou non ? ")
    if replay.lower()=="oui":
        jouer()
    else:
        print("A la prochaine!")

jouer()