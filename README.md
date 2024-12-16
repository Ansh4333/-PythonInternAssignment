# -PythonInternAssignment
Task 1
API Endpoints
POST /add-app: Adds app details to the database (app_name, version, description).
GET /get-app/{id}: Retrieves app details by ID.
DELETE /delete-app/{id}: Removes an app by ID.
Deliverables:

API Codebase
README.md File
Instructions:
Setup the Python Environment:

Install Flask:
bash
Copy code
pip install Flask
Run the API:

Clone the repository containing the API code:
bash
Copy code
git clone <repository-url>
cd <repository-directory>
Start the Flask server:

bash
Copy code
python app.py  # Replace 'app.py' with your Flask app file name
Test the API using Postman:

Open Postman and follow these steps:
POST /add-app:
Method: POST
URL: http://localhost:5000/add-app
Body: Form Data
Key: app_name, Value: MyApp
Key: version, Value: 1.0
Key: description, Value: Sample app
GET /get-app/{id}:
Method: GET
URL: http://localhost:5000/get-app/{1} 
DELETE /delete-app/{id}:
Method: DELETE
URL: http://localhost:5000/delete-app/{1}
API Codebase:
Task 2: Database Management
Database Schema
Design a simple SQLite or PostgreSQL database to store app information:
Fields: app_name, version, description
Deliverables:

Database Schema File
Sample Data
Instructions:
Setup the Database:

Install SQLite or PostgreSQL:
bash
Copy code
pip install sqlite3  # For SQLite
# or
pip install psycopg2  # For PostgreSQL
Integrate the Database with the API:

Modify your API code to connect to the database and manage the CRUD operations.
Example of SQLite integration in Flask:
python
Copy code
import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()
c.execute('''CREATE TABLE apps (id INTEGER PRIMARY KEY, app_name TEXT, version TEXT, description TEXT)''')
conn.commit()
Test the Integration:

After setting up the database, test CRUD operations using the API.
Task 3 
setup_virtual_android(): This function initializes a virtual Android environment. It prints out a message to indicate that the virtual environment has been set up.

Output Example:
arduino
Copy code
Setting up a virtual Android environment...
Virtual Android environment initialized.
install_app(apk_path): This function simulates the installation of an APK file in the virtual Android environment. It accepts the path to the APK file as a parameter and prints a message indicating the successful installation.

Example Usage:
python
Copy code
install_app("demo_app.apk")
Output Example:
Copy code
Installing demo_app.apk...
App demo_app.apk installed successfully.
log_system_info(): This function retrieves and logs system information from the virtual Android environment. It randomly generates data such as the OS version, device model, and available memory. These details are then printed for confirmation.

Output Example: 
System Information: {'os_version': 'Android 11', 'device_model': 'VirtualPixel', 'avai
Setting up a virtual Android environment...
Virtual Android environment initialized.
Installing demo_app.apk...
App demo_app.apk installed successfully.
System Information: {'os_version': 'Android 11', 'device_model': 'VirtualPixel', 'available_memory': '3 GB'}

Task 4: Basic Networking
Deliverables:

Networking Script
Brief Explanation
Instructions:
Setup Backend Server:

Ensure your backend server (from Task 1) is running.
Connect to the Backend Server:

Write a Python script to establish a TCP or HTTP connection with the backend server.
Example (TCP):
python
Copy code
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))  # Replace with your server address
s.sendall(b'Hello, server')
data = s.recv(1024)
print('Received', repr(data))
s.close()
Send and Receive Mock Data:

Send mock data from the virtual Android system to the backend API.
Example:
python
Copy code
import requests

response = requests.post('http://localhost:5000/add-app', data={'app_name': 'TestApp', 'version': '1.0', 'description': 'Test description'})
print(response.text)
Brief Explanation:

How the script connects and communicates with the backend server.
How to test the connection using mock data.
Networking Script: Network.py

