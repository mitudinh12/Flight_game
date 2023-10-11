import mysql.connector

#user example is a tuple of (name, co2_budget, location, game score)
user_example = ('Tu', 10000, 'Finland', 0)
user_example_2 = ('Minh', 10000, 'Sweden', 3)


def get_continent(country):
    sql = f"SELECT continent FROM country WHERE name = '{country}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_result = cursor.fetchall()
    continent = database_result[0][0]
    return continent #return a list of a tuple


def add_result_database(player):
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

def get_all_countries():
    sql = "SELECT name FROM country"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    country_list = []
    for i in result:
        country_list.append(i[0])
    return country_list


def check_country_existence(country):
    countries = get_all_countries()
    if country in countries:
        return bool(True)
    else:
        return bool(False)


def get_destination():
    next_location = input("Next destination: ")
    while check_country_existence(next_location) is False:
        next_location = input("Country not found!!! Type again your destination: ")
    next_continent = get_continent(next_location)
    destination = dict(country=next_location, continent=next_continent)
    print(destination)
    return destination


def play_game():
    name = input("Enter your name: ")
    location = input("Which country are you in right now?: ") #country name must be correct, for now
    current_continent = get_continent(location)
    flight_count = 0
    co2_budget = 10000
    print(f"Your current co2 budget: {co2_budget}, continent: {current_continent}")

    next_location = get_destination()
    next_country = next_location["country"]
    next_continent = next_location["continent"]

    while (co2_budget >= 1000):
        if co2_budget >= 3000:
            if next_continent != current_continent:
                co2_budget -= 3000
            else:
                co2_budget -= 1000
            flight_count +=1
            current_continent = next_continent
            location = next_country
            print(f"Current budget: {co2_budget}, continent: {current_continent}")

            next_location = get_destination()
            next_country = next_location["country"]
            next_continent = next_location["continent"]

        if co2_budget < 3000:
            if next_continent != current_continent:
                print("WARNING: You don't have enough co2 budget to make this flight!")
                break
            else:
                co2_budget -= 1000
                flight_count +=1
                current_continent = next_continent
                location = next_country
                if co2_budget == 0:
                    break
            print(f"Current budget: {co2_budget}, continent: {current_continent}")

            next_location = get_destination()
            next_country = next_location["country"]
            next_continent = next_location["continent"]

    print(f"Game over, your final score is {flight_count}. Current location: {location}")
    result = name, co2_budget, location, flight_count
    add_result_database(result)




















