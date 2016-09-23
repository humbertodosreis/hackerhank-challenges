import sys

time = input().strip()
hour, min, sec = time[:-2].split(":")
meridian = time[-2:]
hour = int(hour)

if meridian == "AM":
    if hour == 12:
        hour-= 12
else:
    if hour < 12:
        hour+= 12

print("%s:%s:%s" % (str(hour).rjust(2, "0"), min, sec))