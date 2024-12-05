import os
import ctypes
import time
import subprocess
import sys

# Import necessary packages
try:
    import fade
    import pyuac
    from pystyle import System
    from utils.windows import windows
    from utils.winrar import winrar
except ImportError as e:
    print(f"Missing package: {e.name}. Installing...")
    # List of packages to install
    packages = ['pystyle', 'pyuac', 'fade']

    def install(package):
        """Install a package using pip."""
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

    for package in packages:
        try:
            install(package)
            print(f"{package} installed successfully.")
        except Exception as e:
            print(f"Failed to install {package}. Error: {e}")

# Set console title and size
title = ctypes.windll.kernel32.SetConsoleTitleW
System.Size(120, 30)

# Define the menu options
menu = """
                                                  ..,,;;;;;;,,,,
                                            .,;'';;,..,;;;,,,,,.''';;,..
                                         ,,''                    '';;;;,;''
                                        ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
                                       ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
                                          ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
                                         ;;@@@@@@;           , ';;;@@@@@@@@;;;.
                                          '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
                                             .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
                                               ''..,,     ''''    '  .,;'
                                                    ''''''::''''''''

                                                [ 1 ] Windows Activator
                                                [ 2 ] Winrar Activator
                                                [ 3 ] Exit"""

# Define a function to clear the console screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the main function
def main():
    cls()
    title("VPT Activator | .gg/fEqXe2CceZ")
    print(fade.blackwhite(menu))

    # Prompt the user for an option
    option = input(f"╔══[{os.getlogin()}@Option]\n╚══> ")

    # Check the user's option
    if option == "1":
        cls()
        windows()
    elif option == "2":
        cls()
        winrar()
    elif option == "3":
        print("Exiting...")
        time.sleep(2)
        return
    else:
        cls()
        print("Invalid option")
        time.sleep(2)

    # Call the main function again to display the menu again
    main()

# Check if the script is being run as an administrator
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("This program needs to be run as an administrator.")
        print("You can now close this window.")
        pyuac.runAsAdmin()
    else:
        main()