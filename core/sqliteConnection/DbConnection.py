import sqlite3
from sqlite3 import Error
import configparser

def create_connection(db_file):
    """ Create connection to a SQLlite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating connection to SqlLite database {e}")
    finally:
        if conn:
            conn.close

def execute(conn, sql):
    """ Executes a statement """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        # todo : change to log
        print(e)

def run_startup_script(conn):
    config = configparser.ConfigParser()
    startupScript = config['startupScriptLocation']
    if conn is not None:
        try:
            execute(conn, startupScript)
        except Error as e:
            # todo : change to db log
            print(e)
        
        
