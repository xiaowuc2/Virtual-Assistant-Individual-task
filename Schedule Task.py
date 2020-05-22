import schedule
import time

#---------------------------------------------

def a():
    print("join")

def b():
    print("how can you")

def c():
    print("now you are")

schedule.every(2).seconds.do(a)
schedule.every(4).seconds.do(b)
schedule.every().day.at("10:55").do(c)

while 1:
    schedule.run_pending()
    time.sleep(1)
    time.sleep(1)
