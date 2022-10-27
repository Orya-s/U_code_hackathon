import pymysql
import pandas as pd

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
        connection.cursor().execute(query)
        connection.commit()
        print(f"table name: {table_name} created successfully with the fields : {fields}")
    except TypeError as e:
        print(e)

def insert_data(connection, table_name, entries_list):
    try:
        for entry in entries_list:
            values = ""
            for e in entry:
                values += f'"{e}",'
            values = values[:-1]
            print(values)
            query = f'INSERT INTO {table_name} VALUES ({values});'
            connection.cursor().execute(query)
            connection.commit()
    except TypeError as e:
        print(e)


def pull_data(csv_path):	
	df = pd.read_csv(csv_path, sep=',')
	print(df)
	tuples = [tuple(x) for x in df.values]
	return tuples


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
    create_table(connection, 'location', 'locations VARCHAR(20)')
    create_table(connection, 'weather', 'weathers VARCHAR(20), tumbnail VARCHAR(2000)')
    create_table(connection, 'data', 'weathers VARCHAR(20), locations VARCHAR(20), date DATE')

    insert_data(connection, 'data', pull_data("C:\\Users\\Rent\\Desktop\\Hackathon\\data-init\\data.csv"))
    insert_data(connection, 'location', pull_data("C:\\Users\\Rent\\Desktop\\Hackathon\\data-init\\location.csv"))
    insert_data(connection, 'weather', pull_data("C:\\Users\\Rent\\Desktop\\Hackathon\\data-init\\weather.csv"))


init_db()
 
