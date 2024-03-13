from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

DATABASE = "/Users/georgebarber/Dropbox/PycharmProjectsDropbox/flaskProject/checkindb.sqlite"


def create_connection(db_file):
    """
    Create a connection with the database
    :param db_file: name of the database file
    :return: a connection to the file
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def homework_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT first_name, last_name, yr_group, title, description, due_date, subject FROM homework " \
            "INNER JOIN students ON Student_id_fk=Student_id " \
            "INNER JOIN work_table ON slot_1_fk=work_id;"
    cur = con.cursor()
    cur.execute(query)
    homework_list = cur.fetchall()
    con.close()
    print(homework_list)

    return render_template('home.html', homework=homework_list)


if __name__ == '__main__':
    app.run()
