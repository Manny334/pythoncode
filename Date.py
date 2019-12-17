import time
import calendar
localtime = time.localtime(time.time())
print("THe local time is ", localtime)
readtime = time.asctime(time.localtime(time.time()))
print("THe readable format of time is ", readtime)
cal = calendar.month(2019, 11)
print("Here is the calendar")
print(cal)