import schedule
import time
def a():
    print("drink water")
def b():
    print("check why your gf/bf is not calling you ?")
def c():
    print("Are you on the work desk ?")
schedule.every(1).hours.do(a)
schedule.every(120).seconds.do(b)
schedule.every().day.at("10:55").do(c)
