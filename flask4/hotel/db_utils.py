import sqlite3
from typing import Union, List


def create_db():
    con = sqlite3.connect('hotel_db.db')
    cursor = con.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Rooms (
            ID INTEGER PRIMARY KEY,
            Number INTEGER NOT NULL UNIQUE,
            Level INTEGER NOT NULL,
            Status TEXT NOT NULL,
            Price INTEGER NOT NULL
        );'''
    )
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Tenants (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                PassportID INTEGER NOT NULL UNIQUE,
                Age INTEGER NOT NULL,
                Sex TEXT NOT NULL,
                City TEXT NOT NULL,
                Street TEXT NOT NULL,
                RoomNumber INTEGER NOT NULL
            );'''
    )
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Staff (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                PassportID INTEGER NOT NULL UNIQUE,
                Position TEXT NOT NULL,
                Salary REAL NOT NULL
            );'''
    )
    con.commit()
    con.close()


def get_all(table: str):
    with sqlite3.connect('hotel_db.db') as con:
        cursor = con.cursor()
        cursor.execute(
            f'SELECT * FROM {left_letters_and_numbers_only(table)};'
        )
        return cursor.fetchall()


def get_with_filter(table: str, column: str, values: list):
    with sqlite3.connect('hotel_db.db') as con:
        cursor = con.cursor()
        cursor.execute(
            f'''SELECT * FROM {left_letters_and_numbers_only(table)}
            WHERE {left_letters_and_numbers_only(column)} IN 
            ({', '.join(['?' for _ in range(len(values))])});''', values
        )
        return cursor.fetchall()


def add_new_item(table: str, value: dict):
    with sqlite3.connect('hotel_db.db') as con:
        cursor = con.cursor()
        cursor.execute(
            f'''INSERT INTO {left_letters_and_numbers_only(table)}
            VALUES (NULL, {', '.join(['?' for _ in range(len(value))])})''',
            [x[0] for x in value.values()]
        )
        con.commit()
        return True


def update_item(table: str, columns: List[str], values: List[Union[str, int]],
                key: str, item_identifier: Union[str, int]):
    with sqlite3.connect('hotel_db.db') as con:
        cursor = con.cursor()
        cursor.execute(
            f'''UPDATE {left_letters_and_numbers_only(table)}
            SET {', '.join([left_letters_and_numbers_only(column) + ' = ?' 
                            for column in columns])}
            WHERE {left_letters_and_numbers_only(key)} = ?;''',
            (*[x[0] for x in values], item_identifier)
        )
        if cursor.rowcount == 0:
            return False
        con.commit()
        return True


def delete_item(table: str, key: str, item_identifier: Union[str, int]):
    with sqlite3.connect('hotel_db.db') as con:
        cursor = con.cursor()
        cursor.execute(
            f'''DELETE FROM {left_letters_and_numbers_only(table)}
            WHERE {left_letters_and_numbers_only(key)} = ?;''',
            (item_identifier,)
        )
        if cursor.rowcount == 0:
            return False
        con.commit()
        return True


def left_letters_and_numbers_only(string):
    """Against SQL injections"""
    return ''.join([x for x in string if x.isalnum()])
