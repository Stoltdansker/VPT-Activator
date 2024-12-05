import os
import shutil
import time
import fade

# Define the registration data for WinRAR
data = """RAR registration data
WinRAR
Unlimited Company License
UID=4b914fb772c8376bf571
6412212250f5711ad072cf351cfa39e2851192daf8a362681bbb1d
cd48da1d14d995f0bbf960fce6cb5ffde62890079861be57638717
7131ced835ed65cc743d9777f2ea71a8e32c7e593cf66794343565
b41bcf56929486b8bcdac33d50ecf773996052598f1f556defffbd
982fbe71e93df6b6346c37a3890f3c7edc65d7f5455470d13d1190
6e6fb824bcf25f155547b5fc41901ad58c0992f570be1cf5608ba9
aef69d48c864bcd72d15163897773d314187f6a9af350808719796"""

# Define the source and destination paths
source = "rarreg.key"
destination = "C:/Program Files/WinRAR"

# Banner
eye = """
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
                                                    ''''''::''''''''"""

# Function to activate WinRAR
def winrar():
    # Print the ASCII art with a black and white fade effect
    print(fade.blackwhite(eye))

    # Write the registration data to a file
    with open("rarreg.key", "w") as file:
        file.write(data)

    # Wait for 2 seconds
    time.sleep(2)

    # Check if the file already exists in the destination directory
    if os.path.isfile('C:/Program Files/WinRAR/rarreg.key'):
        # Remove the existing file
        os.remove('C:/Program Files/WinRAR/rarreg.key')

    # Move the new file to the destination directory
    shutil.move(source, destination)
    print("Winrar is now activated")

    # Wait for 1.5 seconds
    time.sleep(1.5)