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

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # and output results to the terminal window.

    query = (
        "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )

    cursor.execute(query)
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # the films before the other instructions
    show_films(cursor, "DISPLAYING FILMS")

    # I picked my favorite movie
    cursor.execute(
        "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
        "VALUES ('Inception', '2010', 148, 'Christopher Nolan', "
        "(SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), "
        "(SELECT genre_id FROM genre WHERE genre_name = 'SciFi'))"
    )
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien
    cursor.execute(
        "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') "
        "WHERE film_name = 'Alien'"
    )
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")


    cursor.execute(
        "DELETE FROM film WHERE film_name = 'Gladiator'"
    )
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


finally:
    db.close()
