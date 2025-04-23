import string #Importation du module "string" 
from random import choice #Importation de la commande choice provenant du module "random"

def generer_mdp(longueur=12): #Création d'une fonction qui s'appelle "generer_mdp" qui permet de définir la longueur par défaut à 12

    tous_les_caracteres=string.ascii_letters + string.digits + string.punctuation #Création variale "tous_les_caracteres", string.ascii_letters appelle toutes les lettres, string.digits appelle tous les chiffres et string.punctuation appelle tous les caractères speciaux 
    mdp = ''.join(choice(tous_les_caracteres) for _ in range(longueur)) #"mdp" va appeler "tous_les_caracteres" et choisir au hasard grâce au code random.choice. "for" est une boucle en python, range va faire produire longueur x fois (si longueur = 5, alors range va produire une séquence 5 fois)
    return mdp #Renvoie mdp
while True:#Boucle infinie "Tant que la condition est vraie, exécuté le code en boucle"
    longueur = int(input("Choisis la longueur du mot de passe : "))#Demande à la personne la longueur du mot de passe 
    if longueur <= 4: #Si la longue est inférieur à 4 alors..
        print("Trop court, le minimum est strictement supérieur à 4") #Écrire le message 
    else:#Sinon
        break#Casse la boucle

mot_de_passe = generer_mdp(longueur)#Appelle la fonction generer_mdp avec la longueur donnée et stocke le résultat dans la variable mot_de_passe.

print("Voici un mot de passe sécurisé :", mot_de_passe)#Donne le mot de passe avec une phrase devant