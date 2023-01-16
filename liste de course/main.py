import sys

liste_de_course = []

a = input("""Choisissez parmi les 5 options suivantes :
1:Ajouter un élément à la liste
2:Retirer un élément de la liste
3:Afficher les éléments de la liste
4:Vider la liste
5:Quitter
?Votre choix :""")

if (a < 1 or a > 5):
    print("Veuillez choisir une option valide...")

if a == 1:
    liste_de_course.append(input("Donnez le nom de l'élément à ajouter :"))

elif a == 2:
    item = input("Donnez le nom  de l'élément à retirer :")
    if item in liste_de_course:
        liste_de_course.remove(item)
    else:
        print(f"L'élément {item} n'est pas dans la liste.")

elif a == 3:
    if liste_de_course:
        for i, element in enumerate(liste_de_course):
            print(i, element)
    else:
        print("Votre liste ne contient aucun élément.")

elif a == 4:
    liste_de_course.clear()
    print('La liste a été vidée')

elif a == 5:
    sys.exit()
