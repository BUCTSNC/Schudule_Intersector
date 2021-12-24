import sqlite3

schedule = sqlite3.connect('{}{}.db'.format())
schedule.cursor().execute('''CREATE TABLE HEAD
    (   KEY         TEXT    PRIMARY KEY     NOT NULL,
        VALUE       TEXT                    NOT NULL;''')

schedule.cursor().execute('''CREATE TABLE BODY
    (   ID          INT     PRIMARY KEY     NOT NULL,
        LESSON_NAME TEXT                    NOT NULL,
''')
