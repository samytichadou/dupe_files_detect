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
        'no_log' : False
    }


    for i in range(len(sys.argv)):
        if sys.argv[i]=="-nl":
            args['no_log'] = True

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
    logfile = open(f"{dtime_stamp}_log_dupe.txt","w")

_log("", None)
_log(f"Folder : {args['folderpath']}", logfile)
_log(f"{dtime_read} - Starting to analyze files", logfile)
_log("", None)

# Get datas
datas = _get_file_datas(args['folderpath'])
folder_datas = {}

_log("", logfile)
_log("", logfile)

# Format/Log datas
# By file
_log("DUPE FILE LIST --------------------------------------------------", logfile)
_log("", logfile)

for k in datas:

    # Iterate dupes
    if len(datas[k]['occurences']) > 1:

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

_log("", logfile)

# By folder
_log("DUPE FOLDER LIST ------------------------------------------------", logfile)
_log("", logfile)

for fp in folder_datas:
    _log(f"FOLDER - {fp} - dupes found :", logfile)
    for f in folder_datas[fp]['dupes']:
        _log(f"    {f}", logfile)

    _log("", logfile)

time_elapsed = float(time.time()-time_start)
_log(f"Folder analyzed in {round(time_elapsed, 5)} seconds", logfile)
