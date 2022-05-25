# imports database adapter for python, psycopg2
import psycopg2

# establish connection to database using psycopg2
# On Windows OS, provide username and password of postgres user
# connection = psycopg2.connect("dbname=test user=postgres password=root")

connection = psycopg2.connect('dbname = test')

# cursor is an interface that allows you to start queuing up work and
# transactions.
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

cursor.execute('''
    INSERT INTO table2(
        id, completed)
    VALUES (
        1, true
    );
''')

# Next you commit the work

connection.commit()

# Close the connection

connection.close()

# Close the cursor

cursor.close()
