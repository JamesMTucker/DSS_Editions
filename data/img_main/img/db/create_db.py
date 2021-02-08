# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error

def create_imgsdb(db_name):
    """
    Create database for images
    """
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_connection(db_name):
    """
    Return connection to the db
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table):
    """
    Create a new sql table in database
    """
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)

def main():
    db_name = 'imgs.db'
    create_imgsdb(db_name)

    create_imgs_table = """CREATE TABLE IF NOT EXISTS nli_images (
                            id integer PRIMARY KEY,
                            file_name TEXT NOT NULL,
                            nat_w integer NOT NULL,
                            nat_h integer NOT NULL,
                            dpi integer NOT NULL,
                            typ integer NOT NULL,
                            wv_s integer NOT NULL,
                            wv_e integer NOT NULL,
                            is_master integer NOT NULL,
                            img_cat_id integer NOT NULL,
                            is_recto integer NOT NULL)
                        """
    conn = create_connection(db_name)
    if conn is not None:
        create_table(conn, create_imgs_table)
    else:
        print(f"Error! cannot connect to {db_name}")

if __name__ == '__main__':
    main()