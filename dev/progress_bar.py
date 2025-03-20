import time
import sys

list = ["aiueahze", "azeoisdf", "auziejhsdf", "azeuh"]

# toolbar_width = 25
#
# # setup toolbar
# sys.stdout.write("[%s]" % ("-" * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
#
# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("X")
#     sys.stdout.flush()
#
# sys.stdout.write("]\n") # this ends the progress bar

total = 4
count = 1
old_len = 0

def _process_counter(count, total):
    count_zfill = str(count).zfill(len(str(total)))
    counter = f"{count_zfill}/{total}"
    return counter

def _update_print(msg, total):
    global old_len, count, total

    counter = _process_counter(count, total)

    # Clear line
    sys.stdout.write("\r")
    sys.stdout.write(" " * (old_len+len(counter)+3))
    sys.stdout.write("\r")

    # Get new length
    old_len = len(msg)

    # Write new
    sys.stdout.write(f"{counter} - {msg}")
    sys.stdout.flush()

    # increment
    count += 1

for i in list:
    _update_print(i)

sys.stdout.write("\n") # this ends the progress bar
