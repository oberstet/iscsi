import os
import time
import datetime

def utcnow():
   now = datetime.datetime.utcnow()
   return now.strftime("%Y-%m-%dT%H:%M:%SZ")

while True:
    fd = os.open("/tank0/data0/check", os.O_TRUNC | os.O_CREAT | os.O_RDWR)
    now = utcnow()
    os.write(fd, now)
    os.fsync(fd)
    os.close(fd)
    print "written %s" % now
    time.sleep(1)
