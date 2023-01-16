from random import randint

number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

while remaining_attempts > 0:
    print(
        f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    user_choice = int(user_choice)

    if number_to_find > user_choice:
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice:
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:
        break

    remaining_attempts -= 1

if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
    print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

print("Fin du jeu.")
