import main_game


def show_introduction():
    file = open("game_introduction.txt", "r")
    print(file.read())

def start_game():
    return main_game.play_game()

def show_rule():
    file = open("game_rule.txt", "r")
    print(file.read())

def show_menu():
    show_introduction()
    while True:
        menu = open("game_menu.txt", "r")
        print(menu.read())
        player_option = int(input("Choose an option to proceed... : "))

        if player_option == 1:
            show_rule()

        if player_option == 2:
            start_game()

        if player_option == 3:
            print("Thank you for playing... Goodbye! ")
            break

show_menu()









