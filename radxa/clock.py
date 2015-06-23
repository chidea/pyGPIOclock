from time import sleep, localtime
from pyRock.radxa_gpio import radxa_gpio
import signal

GPIO = radxa_gpio()
#           ul,           u,             ur,         m,         bl,          b,         br,           d
seg_h =  GPIO.j12p37, GPIO.j12p36, GPIO.j12p35, GPIO.j12p32, GPIO.j12p34, GPIO.j8p9, GPIO.j12p31, GPIO.j12p38
seg_m1 = GPIO.j8p32,  GPIO.j8p28,  GPIO.j8p27,  GPIO.j8p31,  GPIO.j8p22,  GPIO.j8p21,  GPIO.j8p20,  GPIO.j8p19
seg_m0 = GPIO.j8p26,  GPIO.j8p24,  GPIO.j8p23,  GPIO.j8p12,  GPIO.j8p14,  GPIO.j8p15,  GPIO.j8p13,  GPIO.greenLED

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
  exit()

def show_seg(tseg, num):
  for i, pin in enumerate(tseg[:-1]):
    GPIO.output(pin, int(seg[num][i]))

if __name__ == '__main__':
  #GPIO initialization
  GPIO.init()
  for pin in seg_h + seg_m1 + seg_m0:
      GPIO.output(pin, False)

  signal.signal(signal.SIGINT, sighandler)
  signal.signal(signal.SIGTERM, sighandler)

  while True:
    t = localtime()
    h, m = t.tm_hour%12, t.tm_min
    # print('%02d : %02d'% (h, m))
    GPIO.output(seg_h[-1], 1 if h>9 else 0)
    list(map(show_seg, (seg_h, seg_m1, seg_m0), (h%10, m//10, m%10)))
    sleep(60-t.tm_sec)