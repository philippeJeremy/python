import random

VIE_ENNEMI = 50
PLAYER_VIE = 50
NOMBRE_DE_POTIONS = 3
PASSER = False

while True:
    if PASSER:
        print("Vous passez votre tour...")
        PASSER = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input(
                "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice == "1":
            your_attack = random.randint(5, 10)
            VIE_ENNEMI -= your_attack
            print(
                f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔️")
        elif user_choice == "2" and NOMBRE_DE_POTIONS > 0:
            potion_health = random.randint(15, 50)
            PLAYER_VIE += potion_health
            NOMBRE_DE_POTIONS -= 1
            SKIP_TURN = True
            print(
                f"Vous récupérez {potion_health} points de vie ❤️ ({NOMBRE_DE_POTIONS} ? restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue

    if VIE_ENNEMI <= 0:
        print("Tu as gagné ?")
        break

    enemy_attack = random.randint(5, 15)
    PLAYER_VIE -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

    if PLAYER_VIE <= 0:
        print("Tu as perdu ?")
        break

    print(f"Il vous reste {PLAYER_VIE} points de vie.")
    print(f"Il reste {VIE_ENNEMI} points de vie à l'ennemi.")
    print("-" * 50)

print("Fin du jeu.")
