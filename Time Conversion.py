import os
import sys

def amPmTo24HoursTime(s):
    time = int(s[0:2])
    if(s[-2:] == "PM"):
        if(time == 12):
            s = s.replace(s[0:2], "12")
        else:
            newTime = 12 - time
            newTime = 24 - newTime
            s = s.replace(s[0:2], str(newTime))

    if (s[-2:] == "AM"):
        if(time < 12 ):
            newTime = time
            if (newTime == 0):
                s = s.replace(s[0:2], "00")
            else:
                s = s.replace(s[0:2], "0"+str(newTime))
        else:
            newTime = 12-time
            if(newTime == 0):
                s = s.replace(s[0:2], "00")
            else:
                s = s.replace(s[0:2], "0"+str(newTime))

    s = s[:-2]
    return s



s = input()
result = amPmTo24HoursTime(s)
print(result)
