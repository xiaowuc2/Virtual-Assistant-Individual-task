import schedule
import time
def a():
    print("join")
def b():
    print("how can you")
schedule.every(2).seconds.do(a)
def c():
    print("now you are")
