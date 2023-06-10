import sqlite3

try:
    connection = sqlite3.connect('data.bd')
    cursor = connection.cursor()
except sqlite3.DatabaseError:
    print('произошла ошибка')
finally:
    connection.close()

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def get_users_list(cursor):
    command = '''
    SELECT * FROM users;
    '''
    result = cursor.execute(command)
    user = result.fetchall()
    print(user)

def create_table_user(cursor):
    command = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT);
    '''
    cursor.execute(command)

def add_user(cursor, user):
    command = '''
    INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
    '''
    cursor.execute(command, (user.name, user.surname, user.gender))
def get_user(cursor, user_id):
    command = '''
    SELECT * FROM users WHERE id = ?;
    '''
    result = cursor.execute(command, user_id)
    user = result.fetchall()
    print(user)
def update_user_name(cursor, value, user_id):
    command = '''
    UPDATE user SET name = ? WHERE id = ?;
    '''
    cursor.execute(command, (value, ((user_id))))
def delete_users(cursor):
    command = '''
    DELETE FROM users;
    '''
    cursor.execute(command)
if __name__=='__main__':
    with sqlite3.connect('data.bd') as cursor:
        create_table_user(cursor)
        delete_users(cursor)
        add_user(cursor, User('Maxim', 'Ivanov', 'male'))
        add_user(cursor, User('Raisa', 'Ivanova', 'female'))
        add_user(cursor, User('Dmitri', 'Ivanov', 'male'))
        get_users_list(cursor)
        get_user(cursor, '1')
        update_user_name(cursor, 'Pavel', 1)
        get_user(cursor, '1')