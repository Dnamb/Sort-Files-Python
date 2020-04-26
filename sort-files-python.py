#import libraries
import os
import shutil
from pathlib import Path

def categorize(file): # function to categorize the files based on the lists
        documents = ['xlsx','doc', 'docx', 'xlsm', 'txt']
        media = ['mp4', 'avi', 'mkv', 'mpeg','mov']
        compressed = ['zip', '7zip', 'rar']
        pictures = ['png', 'jpg', 'jpeg','gif']
        programs = ['exe', 'msi']
        
        file_format = file[len(file)-6:len(file)].split(".")[1]
        
        if file_format in documents:
            return "Document"
        elif file_format in media:
            return "Media"
        elif file_format in compressed:
            return "Compressed"
        elif file_format in pictures:
            return "Pictures"
        elif file_format in programs:
            return "Programs"
        else:
            return "Assorted"


path = Path(r"C:\Users\Deepak Nambiar\Downloads") #Update the folder location

files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        cat_path = os.path.join(path, categorize(file))
        if not os.path.isdir(cat_path):
            os.makedirs(cat_path)
            shutil.move(os.path.join(path, file), os.path.join(cat_path ,file))
        else:
            shutil.move(os.path.join(path, file), os.path.join(cat_path ,file))