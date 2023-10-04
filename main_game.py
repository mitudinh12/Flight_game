
def createPlayer():
    name = input("Enter your name: ")
    location = input("Which country are you in right now?: ")
    player = {
        "name": name,
        "current_location": location
    }
    return player


def main_game(location):
    flight_count = 0
    co2_budget = 10000
    print(f"Your current co2 budget: {co2_budget}")
    destination = input("Next destination: ")
    while (co2_budget >= 1000):
        if co2_budget >= 3000:
            if destination != location:
                co2_budget -= 3000
            else:
                co2_budget -= 1000
            flight_count +=1
            location = destination
            print(f"Current value: {co2_budget}")
            destination = input("Next destination: ")

        if co2_budget < 3000:
            if destination != location:
                print("WARNING: You don't have enough co2 budget to make this flight!")
                break
            else:
                co2_budget -= 1000
                flight_count +=1
                location = destination
                if co2_budget == 0:
                    break
            print(f"Current value: {co2_budget}")
            destination = input("Next destination: ")

    print(f"Game over, your final score is {flight_count}. Current location: {location}")
    result = co2_budget, location, flight_count
    print(result)
    return result

def updatePlayer(name, co2_remaining, updated_location, score):
    player_name = name
    player_co2 = co2_remaining
    player_location = updated_location
    player_score = score
    player_data = player_name, player_co2, player_location, player_score
    return player_data

def playGame():
    player = createPlayer()
    print(player)
    game_start = main_game(player['current_location'])
    update_player = updatePlayer(player['name'], game_start[0],game_start[1], game_start[2])
    print(update_player)
    return update_player

playGame()








