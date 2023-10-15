import mysql.connector
def get_continent(country):  # search for the equivalent continent of a given country
    sql = f"SELECT continent FROM country WHERE name = '{country}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_result = cursor.fetchall()
    continent = database_result[0][0]
    return continent

def add_result_database(player): # save a player's game record
    sql = "INSERT INTO player_record (player_name, co2_budget, location, score) VALUES (%s, %s, %s, %s)"
    value_to_add = player
    cursor = connection.cursor()
    cursor.execute(sql, value_to_add)
    connection.commit()

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='pass_word',
         autocommit=True
         )
def get_all_countries(): # get all country names from the database
    sql = "SELECT name FROM country"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    country_list = []
    for i in result:
        country_list.append(i[0])
    return country_list

def check_country_existence(country): # check if a country name is in the 'country' database
    countries = get_all_countries()
    if country in countries:
        return True
    else:
        return False

def validate_destination(next_location, location_list):
    # check country name typo
    locations = location_list
    while check_country_existence(next_location) is False:
        next_location = input("Country not found!!! Type again your destination: ")

    # prevent duplicate country name, avoid travelling to the same country again
    while next_location in locations:
        print("\nYou have already travelled to this country. Try again")
        next_location = input("Next destination: ")
        while check_country_existence(next_location) is False:
            next_location = input("\nCountry not found!!! Type again your destination: ")

    return next_location

def play_game():
    locations = [] # list of all countries a player has travelled during a game
    name = input("Enter your name: ")
    current_country = input("Which country are you in right now?: ")
    while check_country_existence(current_country) is False:
        current_country = input("\nCountry not found. Where are you at again?: ")
    locations.append(current_country)
    current_continent = get_continent(current_country)
    flight_count = 0 # player's score of the game
    co2_budget = 10000
    print(f"\nYour current co2 budget: {co2_budget}, continent: {current_continent}")

    next_country_input = input("\nNext destination: ")
    next_country = validate_destination(next_country_input, locations)
    locations.append(next_country)
    next_continent = get_continent(next_country)
    print(next_continent)

    # game logic: check game_rule
    while (co2_budget >= 1000):
        if co2_budget >= 3000:
            if next_continent != current_continent:
                co2_budget -= 3000
            else:
                co2_budget -= 1000
            flight_count += 1
            current_continent = next_continent
            current_country = next_country
            print(f"\nFLIGHT SUCCESS! Current budget: {co2_budget}, continent: {current_continent}")

            next_country_input = input("\nNext destination: ")
            next_country = validate_destination(next_country_input,locations)
            locations.append(next_country)
            next_continent = get_continent(next_country)

        if co2_budget < 3000:
            if next_continent != current_continent:
                print("\nWARNING: You don't have enough co2 budget to make this flight!")
                break
            else:
                co2_budget -= 1000
                flight_count +=1
                current_continent = next_continent
                current_country = next_country
                if co2_budget == 0:
                    break
            print(f"\nFLIGHT SUCCESS! Current budget: {co2_budget}, continent: {current_continent}")

            next_country_input = input("\nNext destination: ")
            next_country = validate_destination(next_country_input, locations)
            locations.append(next_country)
            next_continent = get_continent(next_country)

    print(f"\nGame over, your final score is {flight_count}. Current location: {current_country}")

    # return final result after the game is over.
    result = name, co2_budget, current_country, flight_count
    # add final result to all players record
    add_result_database(result)















