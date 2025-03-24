import sys

# Get arguments
def _get_arguments():

    args = {
        'folderpath' : sys.argv[1],
        'no_log' : False,
        'no_deletion' : False,
        'priority_folder': []
    }


    for i in range(len(sys.argv)):
        print(sys.argv[i])
        if sys.argv[i] in ["-nl", "-nolog"]:
            args['no_log'] = True
        elif sys.argv[i] in ["-nd", "-nodeletion"]:
            args['no_deletion'] = True
        elif sys.argv[i] in ["-pf", "-priorityfolder"]:
            args['priority_folder'] = sys.argv[i+1].split(",")


    return args

datas = _get_arguments()
for f in datas['priority_folder']:
    print(f)
