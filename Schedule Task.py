import schedule
import time
def a():
    print("join")
def b():
    print("how can you")
def c():
    print("now you are")
schedule.every(2).seconds.do(a)
