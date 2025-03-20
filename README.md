# Dupe file detect

Simple cross-platform python script to detect dupe files in a folder and its subfolders.  
The script generates a log file with two categories :
- Dupe file list : each dupe file has an entry, and folders containing it are noted
- Dupe folder list : each folder containing dupe files has an entry, and files in it which are dupe

### Usage
The script needs python 3 to work. 
Here is the syntax :
`python3 <script_file_path> <folderpath_to_analyze>`  
The output will be in the console and in a log file next to the script when process is finished.  
`-nl` argument can be used to not generate the log file. Output is only show in console window.
