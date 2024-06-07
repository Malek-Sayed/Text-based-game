import random
import time

score = 0

def get_input(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print_pause("Invalid input. Please try again.")

def print_pause(message):
    print(message)
    time.sleep(2)

def start_game():
    global score

    print_pause("Welcome to the Adventure Game!")
    print_pause("Your goal is to find the treasure and escape the island.")
    print_pause("You are standing on a beach with two paths in front of you.")
    
    path_options = ["left", "right"]
    path = random.choice(path_options)
    print_pause("Which path will you take? (left/right)")
    path_choice = get_input("> ", path_options)
    print_pause(f"You chose the {path_choice} path.")

    if path_choice == "left":
        print_pause("You encounter a river. Do you swim across or follow the river?")

        river_options = ["swim", "follow"]
        river_choice = random.choice(river_options)
        print_pause("What do you choose? (swim/follow)")
        river_choice = get_input("> ", river_options)
        print_pause(f"You chose to {river_choice} the river.")

        if river_choice == "swim":
            print_pause("You make it across the river, but lose some of your supplies.")
            score += 10
        else:
            print_pause("You follow the river and find a hidden cave.")
            score += 20

            print_pause("Inside the cave, you find a treasure chest with a key inside.")
            print_pause("You can either take the key or leave it. What do you do?")

            key_options = ["take", "leave"]
            key_choice = random.choice(key_options)
            print_pause("What do you choose? (take/leave)")
            key_choice = get_input("> ", key_options)
            print_pause(f"You chose to {key_choice} the key.")

            if key_choice == "take":
                print_pause("You take the key and continue on your journey.")
                score += 30
            else:
                print_pause("You leave the key behind and continue on your journey.")
                score += 20

    else:
        print_pause("You come across a dense forest. Do you go through it or around it?")

        forest_options = ["through", "around"]
        forest_choice = random.choice(forest_options)
        print_pause("What do you choose? (through/around)")
        forest_choice = get_input("> ", forest_options)
        print_pause(f"You chose to go {forest_choice} the forest.")

        if forest_choice == "through":
            print_pause("You get lost in the forest and waste a lot of time.")
            score += 10
        else:
            print_pause("You find a shortcut and save some time.")
            score += 20

            print_pause("You come across an abandoned house. Do you go inside or keep walking?")

            house_options = ["inside", "walk"]
            house_choice = random.choice(house_options)
            print_pause("What do you choose? (inside/walk)")
            house_choice = get_input("> ", house_options)
            print_pause(f"You chose to {house_choice} the house.")

            if house_choice == "inside":
                print_pause("You find some useful supplies inside the house.")
                score += 30
            else:
                print_pause("You decide to keep walking and continue on your journey.")
                score += 20

    print_pause("Congratulations! You found the treasure and escaped the island!")
    print_pause("Your final score is: " + str(score))

start_game()