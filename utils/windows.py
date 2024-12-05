import fade
import subprocess
import time
import os

# Define the menu options
menu = """
                                                  ..,,;;;;;;,,,,
                                            .,;'';;,..,;;;,,,,,.''';;,..
                                         ,,''                    '';;;;,;''
                                        ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
                                       ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
                                          ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
                                         ;;@@@@@@;           , ';;;@@@@@@@@;;;.
                                          '';@@@@@,.  ,   .   ',;;;@@@@@;;' ,.:;'
                                               ''..,,     ''''    '  .,;'
                                                    ''''''::''''''''

                                                [ 1 ] Windows Home
                                                [ 2 ] Windows Pro
                                                [ 3 ] Windows Education
                                                [ 4 ] Windows Enterprise"""

HOME_KEY = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
PRO_KEY = "W269N-WFGWX-YVC9B-4J6C9-T83GX"
EDU_KEY = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
ENT_KEY = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
ACTIVATE_COMMAND = "slmgr /ato"
KMS_SERVER = "kms8.msguides.com"
SUCCESS_MESSAGE = "Windows has been activated."

# Dictionary to map user input to activation commands
activation_options = {
    1: f"slmgr /ipk {HOME_KEY} && slmgr /skms {KMS_SERVER} && {ACTIVATE_COMMAND}",
    2: f"slmgr /ipk {PRO_KEY} && slmgr /skms {KMS_SERVER} && {ACTIVATE_COMMAND}",
    3: f"slmgr /ipk {EDU_KEY} && slmgr /skms {KMS_SERVER} && {ACTIVATE_COMMAND}",
    4: f"slmgr /ipk {ENT_KEY} && slmgr /skms {KMS_SERVER} && {ACTIVATE_COMMAND}"
}

# Function to activate Windows
def windows():
    print(fade.blackwhite(menu))
    option = int(input(f"╔═[{os.getlogin()}@Option] \n╚══>"))
    
    # Check the user's option
    if option in activation_options:
        subprocess.run(activation_options[option], shell=True)
        print(SUCCESS_MESSAGE)
        time.sleep(2)
    else:
        print("Invalid option")
        time.sleep(2)