import time
import pyfakewebcam
import numpy as np
import sys

import cv2 as cv
import time
import math

check = True

def seconds_to_hhmmss(seconds):
  return time.strftime('%H:%M:%S', time.gmtime(seconds))

def decimal(x, n):
  return math.floor(x * 10 ** n) / (10 ** n)

start = time.time()

args = sys.argv

blue = np.zeros((480,640,3), dtype=np.uint8)
blue[:,:,2] = 255

dev = args[1]
camera = pyfakewebcam.FakeWebcam(dev, 640, 480)

while True:

    copy = blue.copy()
    process_time = decimal(time.time() - start, 2)
    text = seconds_to_hhmmss(process_time)
    print(text)
    cv.putText(copy, text, (10, 470), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 2, cv.LINE_AA)

    camera.schedule_frame(copy)
    time.sleep(1/10.0)

    if check:
      cv.imshow("fakecam",cv.cvtColor(copy, cv.COLOR_RGB2BGR))
      cv.waitKey(30)

