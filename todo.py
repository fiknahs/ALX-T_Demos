import psycopg2

connection = psycopg2.connect('dbname = todo')

cursor= connection.cursor()

cursor.execute('DROP TABLE IF EXISTS todos;')

cursor.execute('''
    CREATE TABLE todos(
        id serial PRIMARY KEY,
        description VARCHAR NOT NULL
    );
''')

cursor.execute('''
    INSERT INTO todos(
        id, description)
    VALUES(
        1, 'This might just work');
''')

connection.commit()

connection.close()
cursor.close()