import configparser
import os
import time
import promptlib
from art import *
from datetime import datetime


def display_logo():
    # Will display logo, is reused when menu needs to be reloaded.
    os.system('cls')
    tprint("File Organizer")
    print("                            a small, but handy file organizer!")
    print("\r\n")


class DesktopOrganizer:
    def __init__(self):
        self.config = self.read_config_file()
        items_to_move = []
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
        time.sleep(5)
        os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/folders")
        os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/others")
        for current in self.config["Formats"]:
            os.mkdir(f"{self.folder_path}/Backup - {time_suffix}/{current}")
            extensions_in_folder = self.config["Formats"][current].split(",")
            for item in items_to_move:
                was_moved = False
                for extension in extensions_in_folder:
                    print(extension)
                    if item.endswith(extension):
                        os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/{current}/{item}")
                        items_to_move.remove(item)
                        was_moved = True
                if was_moved == False:
                    os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/others/{item}")
        for item in items_to_move:
            os.replace(f"{self.folder_path}/{item}", f"{self.folder_path}/Backup - {time_suffix}/folders/{item}")

            

    def display_help_menu(self):
        pass

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
