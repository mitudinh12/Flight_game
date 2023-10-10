

def main_game():
    name = input("Enter your name: ")
    location = input("Which country are you in right now?: ")
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
    result = name, co2_budget, location, flight_count
    print(result)
    return result


main_game()








