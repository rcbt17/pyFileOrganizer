import configparser
import os
import time
import promptlib
from art import *
from datetime import datetime


def display_logo():
    # Will display logo, is reused when menu needs to be reloaded.
    os.system('cls')
    tprint("Simple File Organizer")
    print("                            a small, but handy file organizer!")
    print("\r\n")


class DesktopOrganizer:
    def __init__(self):
        self.config = self.read_config_file()
        # Initializing the folder path as empty, so that we can later check if user has selected a folder or pressed cancel
        self.folder_path = ""

    def read_config_file(self):
        # The config file is called settings.ini, stores all default settings and allows for further user customization
        config = configparser.ConfigParser()
        config.read("settings.ini")
        return config

    def display_menu(self):
        # The menu is reloaded when certain options are chosen!
        valid_answer = False
        display_logo()
        while not valid_answer:
            print("[Menu - Please select an option]")
            print("[1] Start Desktop Organizer with the current settings")
            print("[2] Open the configuration file and return to main menu")
            print("[3] Help and How to Use")
            print("[0] Exit\r\n")
            try:
                answer = int(input("Please input your option: "))
                # Making sure the answer is within the expected range
                if answer < 0 or answer > 3:
                    valid_answer = False
                    display_logo()
                else:
                    return answer
            except:
                valid_answer = False
                display_logo()

    def open_config_file(self):
        os.startfile("settings.ini")

    def run_desktop_cleaner(self):
        display_logo()
        prompter = promptlib.Files()
        # Making sure user selects a folder, if path is of a len < 5 it is null!
        while len(self.folder_path) < 5:
            try:
                self.folder_path = prompter.dir()
            except:
                print("Sorry, you must choose a directory!")
        items_to_move = os.listdir(self.folder_path)
        total_items_to_sort = len(items_to_move)

        #Creating a dictionary to help track what files were moved and what files haven't been moved
        file_tracking = {}
        for item in items_to_move:
            if '.' in item:
                file_tracking[item] = 0
        print(f"[+] File Organizer found a total of {total_items_to_sort} files and/or folders that should be sorted.")
        
        #Creating a Folder inside the "to backup" folder, called Backup - current time. It will contain all backed up files
        now = datetime.now()
        time_suffix = now.strftime("%d-%m-%Y %H-%M")
        try:
            os.mkdir(f"{self.folder_path}/Backup - {time_suffix}")
            print(f"[+] We have created the folder Backup - {time_suffix}")
        except Exception as e:
            print("[!] Sorry, we are unable to create a new folder on Desktop. Maybe not enough write privileges?")
            exit(e)
        # Waiting 5 seconds so that the user has the chance to hard abort
        time.sleep(5)

        #Creating the 2 extra folders that are not included within the settings.ini file ( folder for other folders and others for uncategorized files)

        os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/folders")
        os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/others")

        # Parsing the Formats section from our settings.ini and checking as we parse if our files meet the criteria,
        for current in self.config["Formats"]:
            os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/{current}")
            extensions_in_folder = self.config["Formats"][current].split(",")
            for extension in extensions_in_folder:
                for item in items_to_move:
                    if item.endswith(extension):
                        # Using the replace function from "os" to be able to move files. (similar to unix "mv" function)
                        os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/{current}/{item}")
                        print(f"[+] Success - Moved file {item} to the folder {current}")
                        file_tracking[item] = 1
        for item in items_to_move:
            # Checking if current item is a folder, if so, moved it accordingly
            if '.' not in item:
                os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/folders/{item}")
                print(f"[+] Success - Moved folder {item} to the 'folders'")
            # if it isn't a folder and it has not been tracked as already moved, it should be moved to the "others" folder.
            elif file_tracking[item] == 0:
                os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/others/{item}")
                print(f"[+] Success - Moved file {item} to the folder 'others' ")

            

    def display_help_menu(self):
        print("[HELP] Simple file organizer is a simple, yet effective and customizable tool to help you organize your files and folders!")
        print("[HELP] Usage is straightforward, you simply need to press [1] in the menu. It will then simply ask you to select the folder you"
              "want organized and start the job. ")
        print("[HELP] To further customize this software, press [2] to open the settings.ini file. There you can add your own folders and extensions."
              "For example, if you need to put your presentation files in a new folder called School, you simply add the line \r\n"
              "School = .ppt,pptx\r\n")
        input("Press Enter to continue!")

    def start(self):
        answer = self.display_menu()
        while answer != 0:
            if answer == 0:
                exit("Thank you for using our software")
            elif answer == 1:
                self.run_desktop_cleaner()
                answer = 0
            elif answer == 2:
                self.open_config_file()
                answer = self.display_menu()
            elif answer == 3:
                self.display_help_menu()
                answer = self.display_menu()

if __name__ == "__main__":
    DesktopOrganizer().start()
