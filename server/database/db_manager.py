import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="wonder_weather",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

