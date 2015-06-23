from time import sleep, localtime
import RPi.GPIO as GPIO
import signal

#        ul,  u, ur,  m, bl,  b, br,  d
seg_h  = 26, 13,  6, 19,  2, 21, 20, 16
seg_m1 =  5,  9, 10, 11, 12,  7,  8, 25
seg_m0 = 22, 27, 17, 18, 24, 23, 15, 14

# ul, u, ur, m, bl, b, br
seg = [[True,   True,   True, False,   True,  True, True],
       [False, False,   True, False,  False, False, True],
       [False,  True,   True,  True,   True,  True, False],
       [False,  True,   True,  True,  False,  True, True],
       [True,  False,   True,  True,  False, False, True],
       [True,   True,  False,  True,  False,  True, True],
       [True,   True,  False,  True,   True,  True, True],
       [True,   True,   True, False,  False, False, True],
       [True,   True,   True,  True,   True,  True, True],
       [True,   True,   True,  True,  False,  True, True],
      ]

def sighandler(signum, frame):
  for pin in seg_h + seg_m1 + seg_m0:
    GPIO.output(pin, False)
  GPIO.cleanup()
  exit()

def show_seg(tseg, num):
    GPIO.output(tseg[:-1], seg[num])


if __name__ == '__main__':
  #GPIO initialization
  GPIO.setmode(GPIO.BCM)
  for pin in seg_h + seg_m1 + seg_m0:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

  signal.signal(signal.SIGINT, sighandler)
  signal.signal(signal.SIGTERM, sighandler)

  while True:
    t = localtime()
    h, m = t.tm_hour%12, t.tm_min
    # print('%02d : %02d'% (h, m))
    GPIO.output(seg_h[-1], True if h>9 else False)
    list(map(show_seg, (seg_h, seg_m1, seg_m0), (h%10, m//10, m%10)))
    sleep(60-t.tm_sec)