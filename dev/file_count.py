import os

directory = r"/home/tonton/pCloudDrive/"

file_count = sum(len(files) for _, _, files in os.walk(directory))
print(file_count)
