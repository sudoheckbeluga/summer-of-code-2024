from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
DB_HOST = "your_host"
DB_NAME = "your_dbname"
DB_USER = "your_dbuser"
DB_PASS = "your_dbpassword"

# Establishing the connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM your_table')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/add', methods=['POST'])
def add_data():
    new_data = request.json
    name = new_data.get('name')
    age = new_data.get('age')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO your_table (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'Data added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
