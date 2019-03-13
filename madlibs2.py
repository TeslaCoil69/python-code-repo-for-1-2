import time
import calendar
def timesince():
    a= calendar.timegm(time.gmtime())
    b=a/1000
    c=b%60
    d=b//60
    e=d//60
    f=e%24
    print("seconds:", b, "\nminutes:", d,"\nhours",e)
    print("current time, seconds:", c, "\nminutes:", d, "\nhours", f) 
while 1:
    

    time.sleep(1)
    timesince()
