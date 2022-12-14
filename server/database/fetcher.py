from database.connection_manager import connection

def weather_options():
    try:
        with connection.cursor() as cursor:
            weather_query = "SELECT * FROM weather"
            cursor.execute(weather_query)
            weather_result = cursor.fetchall()
            result = {"weather": [e["weathers"]for e in weather_result]}
            return result
    except TypeError as e:
        print(e)
        return {"weather": "Error: couldnt resolve"}

def location_options():
    try:
        with connection.cursor() as cursor:
            location_query = "SELECT * FROM location"
            cursor.execute(location_query)
            location_result = cursor.fetchall()
            result = {"location": [e["locations"]for e in location_result]}
            return result
    except TypeError as e:
        print(e)
        return {"location":  "Error: couldnt resolve"}


def vacation(weather, location):
    try:
        with connection.cursor() as cursor:
            date_query = f'SELECT date FROM data WHERE weathers = "{weather}" AND locations = "{location}";'
            print(date_query)
            cursor.execute(date_query)
            result = cursor.fetchone()
            print(result)
            return result
    except TypeError as e:
        print(e)
        return {"weathers": "Error: couldnt resolve", "locations":  "Error: couldnt resolve"}

