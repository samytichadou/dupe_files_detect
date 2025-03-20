import sys, time

for t in ['print1', 'print2']:
    sys.stdout.write('\033[K' + t + '\r')
    time.sleep(2)

sys.stdout.write('\n')
