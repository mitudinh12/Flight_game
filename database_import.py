import mysql.connector

#user example is a tuple of (name, co2_budget, location, game score)
user_example = ('Tu', 10000, 'Finland', 0)

def getContinent(country):
    sql = f"SELECT continent FROM country WHERE name = '{country}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result #return a list of a tuple


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='pass_word',
         autocommit=True
         )
continent_result = getContinent(user_example[2])
location = continent_result[0][0]
print(location)







