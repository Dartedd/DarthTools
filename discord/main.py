import os
import sys
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define ASCII Art and Color Constants
ART = """
████████▄     ▄████████    ▄████████     ███        ▄█    █▄        ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
███   ▀███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
███    ███   ███    ███   ███    ███    ▀███▀▀██   ███    ███      ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
███    ███   ███    ███  ▄███▄▄▄▄██▀     ███   ▀  ▄███▄▄▄▄███▄▄     ███   ▀ ███    ███ ███    ███ ███         ███        
███    ███ ▀███████████ ▀▀███▀▀▀▀▀       ███     ▀▀███▀▀▀▀███▀      ███     ███    ███ ███    ███ ███       ▀███████████ 
███    ███   ███    ███ ▀███████████     ███       ███    ███       ███     ███    ███ ███    ███ ███                ███ 
███   ▄███   ███    ███   ███    ███     ███       ███    ███       ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
████████▀    ███    █▀    ███    ███    ▄████▀     ███    █▀       ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                          ███    ███                                                              ▀                      
"""
def clear_terminal():
    # Clear the terminal screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def open_new_terminal(command):
    # Determine the OS and open a new terminal accordingly
    if sys.platform == "win32":
        # For Windows
        subprocess.Popen(["start", "cmd", "/k", command], shell=True)
    elif sys.platform == "darwin":
        # For macOS
        subprocess.Popen(["open", "-a", "Terminal", command])
    elif sys.platform == "linux":
        # For Linux
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
    else:
        print(Fore.RED + "Unsupported OS. Cannot open new terminal.")
        return

def run_script(script_path):
    clear_terminal()  # Clear the terminal before running the script
    print(Fore.CYAN + f"Opening new terminal and running {script_path}...")
    open_new_terminal(f"python {script_path}")

def print_menu():
    print(Fore.CYAN + Style.BRIGHT + ART)
    print(Fore.GREEN + Style.BRIGHT + "DarthTools Home Menu")
    print(Fore.YELLOW + "1. Run Discord Bot Nuker")
    print(Fore.YELLOW + "2. Run Webhook Spammer")
    print(Fore.YELLOW + "3. Run Script 3")
    print(Fore.YELLOW + "4. Run Script 4")
    print(Fore.YELLOW + "5. Run Script 5")
    print(Fore.RED + "6. Exit")

def home_menu():
    while True:
        print_menu()
        choice = input(Fore.BLUE + "Enter your choice (1-6): ").strip()

        if choice == '1':
            run_script("things/BotNuke.py")
        elif choice == '2':
            run_script("things/WebHookSpammer.py")  # Replace with actual path
        elif choice == '3':
            run_script("things/AnotherScript3.py")  # Replace with actual path
        elif choice == '4':
            run_script("things/AnotherScript4.py")  # Replace with actual path
        elif choice == '5':
            run_script("things/AnotherScript5.py")  # Replace with actual path
        elif choice == '6':
            print(Fore.RED + "Exiting...")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    home_menu()
