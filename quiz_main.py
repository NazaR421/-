import sqlite3
conn=None
cursor=None
db_name = "quiz.sqlite"

def open():
    global conn,cursor
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
def close():
    cursor.close()
    conn.close()
def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    open()
    query="DROP TABLE IF EXISTS quiz_content"
    do(query)
    query="DROP TABLE IF EXISTS question"
    do(query)
    query="DROP TABLE IF EXISTS quiz"
    do(query)
    close()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz(
       id INTEGER PRIMARY KEY,
       name VARCHAR)''')
    do('''CREATE TABLE IF NOT EXISTS question(
       id INTEGER PRIMARY KEY,
       question VARCHAR,
       answer VARCHAR,
       wrong1 VARCHAR.
       wrong2 VARCHAR,
       wrong3 VARCHAR,
       )''')
    do('''CREATE TABLE IF NOT EXISTS quiz_content(
       id INTEGER PRIMARY KEY,
       quiz_id INTEGER,
       question_id INTEGER,
       FOREIGN KEY (quiz_id) REFERENCES quiz(id)
       FOREIGN KEY (question_id) REFERENCES question(id)
       )''')
    close()
def add_questions():
    questions=[('1+1=','2','4','6','3'),
               ('2+2=','4','5','6','3'),
               ('3+3=','2','4','5','3'),
               ('4+4=','8','4','6','3'),
               ('5+5=','10','4','6','3')]
    open()
    cursor.executemany('''INSERT INTO question (
                       question,answer,wrong1,wrong2,wrong3)
                       VALUES (?,?,?,?,?)''',questions)
    conn.commit()
    close() 
