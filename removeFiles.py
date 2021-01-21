import os
import shutil
import time
days = 6
path_file = 'test'


def main():
    folders_to_delete = 0
    files_to_delete = 0
    seconds = time.time() - convert_days_to_sec(days)


    if os.path.exists(path_file):
        for root, dirs, files in os.walk(path_file):
            if  get_ctime(root) <= seconds:
                folders_to_delete += 1
                
            else:
                print(files)

                for folder in dirs:
                    dir_path = os.path.join(root, folder)
                    if get_ctime(dir_path) <= seconds:
                        folders_to_delete += 1

                for file in files:
                    file_path = os.path.join(root, file)
                    print(file_path)
                    if get_ctime(file_path) <= seconds:
                        files_to_delete += 1

    else:
        print('wrong path')

    return folders_to_delete, files_to_delete


def get_ctime(path):
    ctime = os.stat(path).st_ctime
    return ctime


def convert_days_to_sec(days):
    time_in_sec = days*24*60*60
    return time_in_sec


print(main())
