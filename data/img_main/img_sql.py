import sqlite3
from sqlite3 import Error
import pandas as pd


def fetch_images():
    """
    Return a pandas dataframe of the available iaa images
    """
    # sqlite3 does not have regexp, so this is solved in the dataframe
    sql_query = """SELECT * FROM nli_images"""
    conn = sqlite3.connect('img/db/imgs.db')

    df = pd.read_sql_query(sql_query, conn)
    df['PLATE'] = df['file_name'].str.extract('^(?:[Pp|plate])?(?: )?([0-9A-z]+)')

    # THE IAA file names are not systematic. Fix for URL
    df['file_name'].replace(u'\u0020', '%20', inplace=True, regex=True)

    return df