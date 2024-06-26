import datetime as dt
import os
from scheduler import Scheduler


import time
import subprocess

hour_timeout=5

def run_long_function():
    try:
        subprocess.run('python long_function.py',timeout=hour_timeout*60*60)
    except Exception as e:
        print(e)
        print('-------------------------------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')



# run_long_function()

schedule = Scheduler()
schedule.cyclic(dt.timedelta(weeks=1), run_long_function) 
print(schedule)

subprocess.run('minimize.cmd')
run_long_function()
while True:
    schedule.exec_jobs()
    time.sleep(1)
