import requests
from virtual_android import setup_virtual_android, install_app, log_system_info

def connect_to_server():
    # Set up virtual Android environment
    setup_virtual_android()
    install_app("demo_app.apk")
    system_info = log_system_info()

    # Backend server URL (replace with your server's URL)
    url = "http://127.0.0.1:5000/add-app"
    
    # Add system info as mock data to the server
    data = {
        "app_name": "VirtualSystemApp",
        "version": system_info["os_version"],
        "description": f"Device: {system_info['device_model']}, Memory: {system_info['available_memory']}"
    }

    # Send data to server
    try:
        response = requests.post(url, json=data)
        print("Server Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error connecting to the server:", e)

if __name__ == "__main__":
    connect_to_server()
