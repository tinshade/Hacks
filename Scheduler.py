#For scheduling task execution
import schedule
import time

def job():
    print("It's a minute")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
