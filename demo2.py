# imports database adapter for python, psycopg2
import psycopg2

# establish connection to database using psycopg2
connection = psycopg2.connect('dbname = test')

# cursor is an interface that allows you to start queuing up work and
# transactions.
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

# using %s turns the statement into a template that we can inject data in
cursor.execute('''
    INSERT INTO table2(
        id, completed)
    VALUES (
        %s, %s 
    );
''', (1, True))  # arguments that will be passed to %s as tuples

cursor.execute('''
    INSERT INTO table2(
        id, completed)
    VALUES (
        %(id)s, %(completed)s 
    );
''', {
    'id': 2,
    'completed': False
})  # arguments that will be passed to %s as a dictionary

# OR clean up code and write it this way

SQL = '''
    INSERT INTO table2(
        id, completed)
    VALUES (
        %(id)s, %(completed)s 
    );
'''

data = {
    'id': 3,
    'completed': False
}

# arguments that will be passed to %s as a dictionary
cursor.execute(SQL, data)

# Fetch data from DB
cursor.execute('SELECT * from table2;')

# result = cursor.fetchall()
# print(result)

result = cursor.fetchmany(2)
print(result)

result2 = cursor.fetchone()
print(result2)
# Next you commit the work

connection.commit()

# Close the connection

connection.close()

# Close the cursor

cursor.close()
