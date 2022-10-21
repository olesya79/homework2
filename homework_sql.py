import sqlite3 as sq

with sq.connect('phonebook.db') as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS names(
    id INTEGER,
    firstname TEXT,
    surname TEXT,
    phonenumber INTEGER
    );
    """)

    cur.execute(""" INSERT INTO names(id, firstname, surname, phonenumber)
    VALUES(1, 'Simon', 'Howeis', 01223349752)""")
    con.commit()

    cur.execute(""" INSERT INTO names(id, firstname, surname, phonenumber)
    VALUES(2, 'Karen', 'Phillips', 01954295773)""")
    con.commit()

    cur.execute(""" INSERT INTO names(id, firstname, surname, phonenumber)
    VALUES(3, 'Darren', 'Smith', 01583749012)""")
    con.commit()

    cur.execute(""" INSERT INTO names(id, firstname, surname, phonenumber)
    VALUES(4, 'Anne', 'Jones', 01323567322)""")
    con.commit()

    cur.execute(""" INSERT INTO names(id, firstname, surname, phonenumber)
    VALUES(5, 'Mark', 'Smith', 01223855534)""")
    con.commit()



