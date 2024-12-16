from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('app_database.db')

# Create table on startup
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        version TEXT NOT NULL,
        description TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

create_table()

# POST /add-app
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    app_name = data['app_name']
    version = data['version']
    description = data['description']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO apps (app_name, version, description)
    VALUES (?, ?, ?)
    ''', (app_name, version, description))
    conn.commit()
    conn.close()
    return jsonify({"message": "App added successfully"}), 201

# GET /get-app/<id>
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM apps WHERE id = ?', (id,))
    app = cursor.fetchone()
    conn.close()

    if app:
        return jsonify({
            "id": app[0],
            "app_name": app[1],
            "version": app[2],
            "description": app[3]
        }), 200
    else:
        return jsonify({"error": "App not found"}), 404

# DELETE /delete-app/<id>
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM apps WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        return jsonify({"message": "App deleted successfully"}), 200
    else:
        return jsonify({"error": "App not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
