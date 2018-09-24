from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

import time

def task(arg):
    print(arg)
    time.sleep(2)

pool = ThreadPoolExecutor(5)
# pool = ProcessPoolExecutor(5)

for i in range(50):
    pool.submit(task, i)