# app.py

from flask import Flask, jsonify
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Function to establish a connection to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['POSTGRES_HOST'],
        user=app.config['POSTGRES_USER'],
        password=app.config['POSTGRES_PASSWORD'],
        dbname=app.config['POSTGRES_DB']
    )
    return conn

# Example route to test the connection
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({'database_version': db_version[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

# Example route to interact with the 'customer' table
@app.route('/customers')
def get_customers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Example: Retrieving customers from the 'customer' table
        cursor.execute("SELECT * FROM customer")
        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({'customers': customers})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
