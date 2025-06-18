def start_game():
    print("Welcome to the Choose Your Own Adventure Game!")
    print("You awaken in a mysterious forest at dusk. The trees are thick, and a chill runs down your spine.")
    print("There are two winding paths ahead: one to the left and one to the right.")

    choice1 = input("Do you go left or right? (left/right): ").strip().lower()

    if choice1 == "left":
        print("\nYou take the left path. The trees close in above you, and soon you find a rushing river blocking your way.")
        print("You notice a rickety old bridge and, further down, a shallow-looking spot in the river.")
        choice2 = input("Do you cross the bridge or try to wade across the river? (bridge/wade): ").strip().lower()

        if choice2 == "bridge":
            print("\nYou step carefully onto the bridge. Halfway across, the wood creaks loudly!")
            print("Do you rush forward or retreat?")
            choice3 = input("Do you rush or retreat? (rush/retreat): ").strip().lower()
            if choice3 == "rush":
                print("\nYou sprint forward and barely make it as the bridge collapses behind you.")
                print("On the other side, you find a hidden village. The villagers welcome you as a hero for surviving the bridge. You live out your days as the village wise one. The End.")
            elif choice3 == "retreat":
                print("\nYou try to retreat, but the boards snap and you fall into the river below.")
                print("The current is swift, and you struggle to swim. Sadly, you are swept away downstream and never seen again. The End.")
            else:
                print("\nUnable to decide, you freeze. The bridge gives out and you fall. Your adventure ends here.")
        elif choice2 == "wade":
            print("\nYou brave the cold water and start to wade across.")
            print("Halfway through, you spot something shiny under the water.")
            choice3 = input("Do you dive for the shiny object or keep crossing? (dive/keep crossing): ").strip().lower()
            if choice3 == "dive":
                print("\nYou dive and grab an old, jeweled locket! You make it to the other side, wet but richer.")
                print("The locket is magical and grants you safe passage home. You become famous for your discovery. The End.")
            elif choice3 == "keep crossing":
                print("\nYou keep your eyes on the prize: dry land. You reach the other side safely.")
                print("You find a map on the ground leading you out of the forest and to new adventures. The End.")
            else:
                print("\nYou hesitate too long and slip, hitting your head on a rock. Your adventure sadly ends here.")
        else:
            print("\nConfused, you wander along the river until night falls. Lost, you are never heard from again. The End.")

    elif choice1 == "right":
        print("\nYou choose the right path, which leads to a dark cave entrance.")
        print("From inside, you hear both the sound of water dripping and faint singing.")
        choice2 = input("Do you enter the cave or follow the singing? (enter/follow): ").strip().lower()

        if choice2 == "enter":
            print("\nYou step into the cave. It's cold and dark, but you keep going.")
            print("You find a fork in the tunnel: one path slopes up, the other down.")
            choice3 = input("Do you go up or down? (up/down): ").strip().lower()
            if choice3 == "up":
                print("\nYou climb upward. At the top, you find a hidden chamber filled with treasure.")
                print("You live a life of luxury, always remembering your brave adventure. The End.")
            elif choice3 == "down":
                print("\nYou descend deeper into the earth, but the tunnel collapses behind you.")
                print("Trapped, you discover ancient cave paintings and spend your days recording them, becoming a legend among explorers. The End.")
            else:
                print("\nParalyzed by indecision, you trip and fall, hitting your head. Your adventure ends here.")
        elif choice2 == "follow":
            print("\nYou follow the singing and find a clearing where a group of forest spirits dance.")
            print("They invite you to join. Do you accept or decline?")
            choice3 = input("Do you join or decline? (join/decline): ").strip().lower()
            if choice3 == "join":
                print("\nYou join the dance and are swept away into the spirit realm.")
                print("You become a forest guardian, protecting the woods forever. The End.")
            elif choice3 == "decline":
                print("\nYou politely decline and the spirits show you a secret path out of the forest.")
                print("You return home, forever changed by your magical encounter. The End.")
            else:
                print("\nYou hesitate, and the spirits vanish. The forest grows dark, and you are lost forever. The End.")
        else:
            print("\nUnable to decide, you wander aimlessly and are lost to the depths of the forest. The End.")
    else:
        print("\nThat's not a valid choice. Your adventure ends before it begins.")

if __name__ == "__main__":
    start_game()
