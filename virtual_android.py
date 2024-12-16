import random

def setup_virtual_android():
    print("Setting up a virtual Android environment...")
    print("Virtual Android environment initialized.")

def install_app(apk_path):
    print(f"Installing {apk_path}...")
    print(f"App {apk_path} installed successfully.")

def log_system_info():
    system_info = {
        "os_version": "Android 11",
        "device_model": "VirtualPixel",
        "available_memory": f"{random.randint(1, 4)} GB"
    }
    print("System Information:", system_info)
    return system_info

if __name__ == "__main__":
    setup_virtual_android()
    install_app("demo_app.apk")
    log_system_info()
