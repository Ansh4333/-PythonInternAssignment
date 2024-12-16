# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:22:51 2024

@author: anshi
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage to hold app data temporarily
apps = {}

# Add App
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json
    app_id = len(apps) + 1
    apps[app_id] = data
    return jsonify({"id": app_id, "message": "App added successfully!"})

# Get App by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_data = apps.get(id)
    if not app_data:
        return jsonify({"error": "App not found"}), 404
    return jsonify(app_data)

# Delete App by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    if id not in apps:
        return jsonify({"error": "App not found"}), 404
    del apps[id]
    return jsonify({"message": "App deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
