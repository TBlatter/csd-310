# TYSON Blatter 4/26 7.2

""" import statements """
import mysql.connector
from mysql.connector import errorcode


from dotenv import dotenv_values

# need .env in the same location as movies_queries or code will not work.
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

#
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}, Studio Name: {studio[1]}")

    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}, Genre Name: {genre[1]}")

    print("\n-- DISPLAYING Short Film RECORDS (run time less than 2 hours) --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    short_films = cursor.fetchall()
    for film in short_films:
        print(f"Film Name: {film[0]}, Runtime: {film[1]} minutes")

    print("\n-- DISPLAYING Director and Film Name RECORDS in Order --")
    cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director;")
    directors = cursor.fetchall()
    for director in directors:
        print(f"Director: {director[0]}, Film: {director[1]}")





finally:
    db.close()
