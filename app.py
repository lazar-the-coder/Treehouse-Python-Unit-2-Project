import calculations

def print_start():
    print("---Welcome to the Basketball Team Stat Tool---")
    calculations.main()
    main_menu()

def main_menu():
    print("\n\nWhat would you like to do?\nV) View Team Stats\nor\nQ) Quit")
    while True:
        choice = input("=>")
        if choice.lower() == "q":
            quit()
        elif choice.lower() == "v":
            break
        else:
            print("Sorry, we couldn't understand your request.")
    team_choice()

def team_choice():
    print("Type in the name of the team or the number beside it.")
    choices = calculations.teams_list
    print(f"1) {choices[0]} \n2) {choices[1]} \n3) {choices[2]}")
    while True:
        choice = input("=>")
        if choice.title() in choices:
            break
        elif choice.lower() == "q":
            quit()
        else:
            try:
                if int(choice) <= 3 and int(choice) > 0:
                    choice = choices[int(choice)-1]
                    break
                else:
                    print("Number not in range")
            except ValueError:
                print("Sorry, we couldn't understand your request.")
    display(choice.title())


def display(team):
    player_count, player_names, exp_players, inexp_players, ave_height, guardian_names = calculations.display_team_stats(team)
    print("\n", team)
    print("Total Players: ", player_count)
    print("Player Names: ")
    print(', '.join(player_names))
    print("Experienced Players:", exp_players)
    print("Inexperienced Players:", inexp_players)
    print("Average Height:", ave_height)
    print("Guardians:")
    print(', '.join(guardian_names))
    input("\nEnter anything to go back to menu")
    main_menu()

if __name__ == "__main__":
    print_start()
