import pymysql

def create_database(db_name):
    try:
        initial_connection = pymysql.connect(
            host="localhost",
            user="root",
            password=""
        )
        initial_connection.cursor().execute(f'create database {db_name};')
        initial_connection.commit()
        print(f"database with name: {db_name} created successfully")
    except TypeError as e:
        print(e)

def create_table(connection, table_name, fields):

    try:
        query = f'CREATE TABLE {table_name} ({fields});'
        print(query)
        connection.cursor().execute(query)
        connection.commit()
        print(f"table name: {table_name} created successfully with the fields : {fields}")
    except TypeError as e:
        print(e)


def init_db():
    create_database("wonder_weather")
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="wonder_weather",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
    )
    create_table(connection, 'location', 'location VARCHAR(20)')
    create_table(connection, 'data', 'weather VARCHAR(20), date DATE, location VARCHAR(20)')
    create_table(connection, 'weather', 'weather VARCHAR(20), tumbnail VARCHAR(2000)')

init_db()
 
# #add ingridients:
# try:
#     initial_connection = pymysql.connect(
#         host="localhost",
#         user="root",
#         password="",
#         db="recipes_app",
#         charset="utf8",
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     with initial_connection.cursor() as cursor:
#         print("inserting values...")
#         dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
#         gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]
#         for dairy in dairy_ingredients:
#             cursor.execute(f"INSERT IGNORE INTO dairy(dairy_ingredients) values('{dairy}')")
#             initial_connection.commit()

#         get_number = f"SELECT * FROM dairy"
#         print(get_number)
#         cursor.execute(get_number)
#         result = cursor.fetchall()
#         print(result)

#         for gluten in gluten_ingredients:
#             cursor.execute(f"INSERT IGNORE INTO gluten(gluten_ingredients) values('{gluten}')")   
#             initial_connection.commit()

#         get_number = f"SELECT * FROM gluten"
#         print(get_number)
#         cursor.execute(get_number)
#         result = cursor.fetchall()
#         print(result)    
            
#         print("Done!")    
# except Exception: 
#     print(Exception.args[0])
#     print("coudlnt insert values!")

