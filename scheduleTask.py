from datetime import datetime
import schedule
import time
from getData import getData

def testSchedule():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Current Time =", current_time)
 
def scheduleTask(status):
        if status == "production":
              schedule.every().day.at("06:00").do(getData("production"))
        else:
           # For Testing you can try the 5 Sec 
           schedule.every(5).seconds.do(testSchedule)
        while True:
            schedule.run_pending()
            time.sleep(1)