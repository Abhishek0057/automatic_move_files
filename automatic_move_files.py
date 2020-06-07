from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 

import os
import time 

class MyHandler(FileSystemEventHandler):

    def __init__(self):
        for folder in sub_folders:
            path = os.path.join(folder_to_track, folder) 
            os.makedirs(path, exist_ok = True)

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            scr = folder_to_track + "/" + filename
            file_extension = filename.split('.')
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
                
                destination = folder_destination + "/" + sub_folder_name + "/" + filename
                os.rename(scr, destination)
            except:
                print(f"Folder '{filename}' detected not file, script cannot organise folder ")
            else:
                print(f"File '{filename}' organised successfully")
            

folder_to_track = '/Users/abhisheksatbhai/Downloads'
folder_destination = '/Users/abhisheksatbhai/Downloads'
development_file_exts = ['php', 'sql', 'zip', 'html', 'json', 'xml', 'htm', 'css']
images_file_exts = ['PNG', 'png', 'jpg', 'jpeg', 'JPG']
other_file_exts = ['xls', 'xlsx', 'csv', 'pdf', 'docx', 'doc']
software_file_exts = ['pkg', 'dmg']
sub_folders = ['development', 'images', 'others', 'softwares']

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()