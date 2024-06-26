from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='newdb',
                            user='postgres',
                            password='Nipun2399@')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    
    # Construct a plain text response
    response = ""
    for book in books:
        response += ', '.join(map(str, book)) + '\n'
    
    return response

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

