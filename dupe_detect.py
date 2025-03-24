import os, sys, time, datetime

# File progress bar variable
count = 0
old_len = 0

# Get file country
def _get_file_count(folderpath):
    file_count = sum(len(files) for _, _, files in os.walk(folderpath))
    return file_count

# Log message
def _log(
    msg,
    logfile=None,
):
    print(msg)
    if logfile:
        logfile.write(f"{msg}\n")

# Get file datas
def _get_file_datas(
    folderpath,
):

    _log("Counting files to process", None)
    total = _get_file_count(folderpath)
    _log("Processing files : ", None)

    def _process_counter(count, total):
        count_zfill = str(count).zfill(len(str(total)))
        counter = f"{count_zfill}/{total}"
        return counter

    def _update_print(count, counter_len, total):
        counter = _process_counter(count, total)

        # Clear line
        sys.stdout.write("\r")
        sys.stdout.write(" " * counter_len)
        sys.stdout.write("\r")

        # Write new
        sys.stdout.write(counter)
        sys.stdout.flush()

    counter_len = len(_process_counter(0,total))

    datas = {}

    count = 0
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            count += 1
            _update_print(count, counter_len, total)

            # Exclusion check
            exclude = False
            for ex in args['exclusion_folder']:
                if ex in os.path.abspath(root):
                    exclude = True
                    break
            if exclude:
                continue

            filepath = os.path.join(root, filename)
            filesize = os.path.getsize(filepath)
            identifier = f"{filename}_{filesize}"

            if identifier not in datas:
                datas[identifier] = {
                    'name' : filename,
                    'size' : filesize,
                    'occurences' : []
                }

            datas[identifier]['occurences'].append(filepath)

    sys.stdout.write("\n")

    return datas

# Get valid argument
def _get_valid_argument():
    if len(sys.argv)<=1:
        print("Missing folderpath argument")
        exit()
    elif not os.path.isdir(sys.argv[1]):
        print("Invalid folderpath argument")
        exit()

# Get arguments
def _get_arguments():

    args = {
        'folderpath' : sys.argv[1],
        'no_log' : False,
        'no_deletion' : False,
        'exclusion_folder': [],
        'priority_folder': [],
        'dry_run': False,
        'verbose': 0
    }


    for i in range(len(sys.argv)):
        if sys.argv[i] in ["-nl", "-nolog"]:
            args['no_log'] = True
        elif sys.argv[i] in ["-nd", "-nodeletion"]:
            args['no_deletion'] = True
        elif sys.argv[i] in ["-pf", "-priorityfolder"]:
            args['priority_folder'] = sys.argv[i+1].split(",")
        elif sys.argv[i] in ["-d", "-dry"]:
            args['dry_run'] = True
        elif sys.argv[i] in ["-v", "-verbose"]:
            args['verbose'] = sys.argv[i+1]
        elif sys.argv[i] in ["-ex", "-exclusion"]:
            args['exclusion_folder'] = sys.argv[i+1].split(",")

    return args


### PROCESS

# Start timer
time_start = time.time()

_get_valid_argument()
args = _get_arguments()

dtime = datetime.datetime.now()
dtime_stamp = dtime.strftime('%Y%m%d-%H%M%S')
dtime_read = dtime.strftime('%Y-%m-%d %H:%M:%S')

# Open log file to write
logfile = None
if not args['no_log']:
    logfile = open(f"{dtime_stamp}_dupe.log","w")

_log("", None)
_log(f"Folder : {args['folderpath']}", logfile)
_log(f"{dtime_read} - Starting to analyze files", logfile)
_log("", None)
_log("Arguments :", None)
_log(args, None)
_log("", None)

# Get datas
datas = _get_file_datas(args['folderpath'])
folder_datas = {}
dupe_datas = {}

_log("", logfile)
_log("", logfile)

# Format/Log datas
# By file
_log("DUPE FILE LIST --------------------------------------------------", logfile)
_log("", logfile)

for k in datas:

    # Iterate dupes
    if len(datas[k]['occurences']) > 1:

        # Get only dupe datas in dict
        dupe_datas[k] = datas[k]

        _log(f"FILE - {datas[k]['name']} - found in :", logfile)

        for fp in datas[k]['occurences']:
            parentdir = os.path.dirname(fp)
            _log(f"    {parentdir}", logfile)

            # Get folder datas
            if fp not in folder_datas:
                folder_datas[parentdir] = {
                    'dupes' : []
                }
            folder_datas[parentdir]['dupes'].append(datas[k]['name'])

_log("", logfile)

# By folder
_log("DUPE FOLDER LIST ------------------------------------------------", logfile)
_log("", logfile)

for fp in folder_datas:
    _log(f"FOLDER - {fp} - dupes found :", logfile)
    for f in folder_datas[fp]['dupes']:
        _log(f"    {f}", logfile)

time_elapsed = float(time.time()-time_start)

_log("", logfile)
_log(f"Folder analyzed in {round(time_elapsed, 5)} seconds", logfile)
_log(f"{len(dupe_datas)} Dupes found", logfile)

### REMOVE FILES GUI
if not args['no_deletion']:

    _log("", logfile)
    _log("Launching deletion sequence", logfile)
    _log("", logfile)

    # Automatic removal
    if args['priority_folder']:

        _log("Automatic removal with priority_folder", logfile)

        dupe_to_remove = []
        for dupe in dupe_datas:

            prio = []
            occurences = dupe_datas[dupe]['occurences']

            for fp in occurences:
                for patt in args['priority_folder']:
                    if patt in fp:
                        prio.append(fp)
                        break

            if len(prio)==1:
                for fp in occurences:
                    if fp not in prio:
                        _log(f"Automatic Deleting - {fp}", logfile)
                        if not args['dry_run']:
                            os.remove(fp)
                dupe_to_remove.append(dupe)

        for dupe in dupe_to_remove:
            del dupe_datas[dupe]

    # Manual removal
    _log("", logfile)

    if not dupe_datas:
        _log("End of dupe files, exiting", None)
        logfile.close()
        exit()

    _log("Manual removal with user input", logfile)

    import tkinter as tk
    from tkinter import ttk, filedialog

    # TKinter gui class
    class RemoveFilesApp(tk.Tk):
        file_count = 0
        total = len(dupe_datas)

        def __init__(self):
            tk.Tk.__init__(self)
            self.title("Deletion")
            self.create_widget()

        def manual_quit(self):
            _log("User exiting", logfile)
            logfile.close()
            exit()

        def delete_file(self, filepath):
            # Delete filepath
            for fp in dupe_datas[list(dupe_datas)[self.file_count]]['occurences']:
                if fp != filepath:
                    if os.path.isfile(fp):
                        _log(f"Manual Deleting - {fp}", logfile)
                        if not args['dry_run']:
                            os.remove(fp)
                    else:
                        _log(f"Invalid filpath - {fp}", logfile)

            # Increment
            self.file_count += 1

            # Quit when finished
            if self.file_count>=self.total:
                _log("End of dupe files, exiting", logfile)
                logfile.close()
                exit()

            # Reload
            self.destroy()
            self.__init__()

        def create_widget(self):
            tk.Label(
                text = "Choose a file to keep :",
            ).pack()

            for fp in dupe_datas[list(dupe_datas)[self.file_count]]['occurences']:
                tk.Button(
                    self,
                    text = fp,
                    command = lambda fp=fp: self.delete_file(fp)
                ).pack()

            tk.Button(
                self,
                text = "Quit",
                command = self.manual_quit,
            ).pack()

    # Launch app
    app = RemoveFilesApp()
    app.mainloop()

logfile.close()
