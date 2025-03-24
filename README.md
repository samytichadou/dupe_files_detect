# Dupe file detect

Simple cross-platform python script to detect dupe files in a folder and its subfolders.  
The script generates a log file with two categories :
- Dupe file list : each dupe file has an entry, and folders containing it are noted
- Dupe folder list : each folder containing dupe files has an entry, and files in it which are dupe  

It also proceed to automatic deletion if priority folders are set (see arguments) and ask user for a file to keep manually.

### Usage
The script needs python 3 to work. 
Here is the syntax :
`python3 <script_file_path> <folderpath_to_analyze>`  
The output will be in the console and in a log file next to the script when process is finished.  
- `-nl` or `-nolog` argument can be used to not generate the log file. Output is only show in console window.
- `-nd` or `-nodeletion` argument can be used to prevent automatic and manual deletion of files
- `-d` or `-dry` argument can be used to launch as dry-run, meaning no real deletion but log file created
- `-pf` or `-priorityfolder` argument, followed by a comma separated list of string contained in priorities folder. When a dupe is found with a priority folder string in one of its occurences filepath (and only one) the other occurences will be automatically deleted.
Command example : `python3 <script_file_path> <folderpath_to_analyze> -pf "myfolder","anotherfolder"`  
- `-ex` or `-exclusion` argument, followed by a comma separated list of folders to exclude as string.
Command example : `python3 <script_file_path> <folderpath_to_analyze> -ex "myfolder","anotherfolder"`  
