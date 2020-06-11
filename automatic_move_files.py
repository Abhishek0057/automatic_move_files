import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        for folder in sub_folders:
            path = os.path.join(FOLDER_TO_TRACK, folder)
            os.makedirs(path, exist_ok=True)

    def on_modified(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            scr = FOLDER_TO_TRACK + "/" + filename
            file_extension = filename.split(".")
            try:
                if file_extension[-1] in development_file_exts:
                    sub_folder_name = sub_folders[0]
                elif file_extension[-1] in images_file_exts:
                    sub_folder_name = sub_folders[1]
                elif file_extension[-1] in other_file_exts:
                    sub_folder_name = sub_folders[2]
                elif file_extension[-1] in software_file_exts:
                    sub_folder_name = sub_folders[3]
                else:
                    continue
                destination = (
                    FOLDER_DESTINATION + "/" + sub_folder_name + "/" + filename
                )
                os.rename(scr, destination)
            except:
                print(
                    f"Folder '{filename}' detected not file, script cannot organise folder "
                )
            else:
                print(f"File '{filename}' organised successfully")
            finally:
                print("Script Run Successfully")


FOLDER_TO_TRACK = "/Users/abhisheksatbhai/Downloads"
FOLDER_DESTINATION = "/Users/abhisheksatbhai/Downloads"
development_file_exts = ["php", "sql", "zip", "html", "json", "xml", "htm", "css"]
images_file_exts = ["PNG", "png", "jpg", "jpeg", "JPG"]
other_file_exts = ["xls", "xlsx", "csv", "pdf", "docx", "doc"]
software_file_exts = ["pkg", "dmg"]
sub_folders = ["development", "images", "others", "softwares"]

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
