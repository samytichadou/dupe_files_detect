# import datetime
#
# print(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

import time

start = time.time()
print("hello")
time.sleep(2)
end = time.time()
elapsed = float(end-start)
print(elapsed)
print(round(elapsed,5))
# print(round(elapsed, 2))
