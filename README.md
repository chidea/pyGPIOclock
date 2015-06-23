#piGPIOclock
A digital wall clock which utilizes seven segments connected to raspberry pi and python GPIO libraries.

## Test and verified on
- Raspberry pi B+

## Test and verify going on
- Radxa lite

Currently the developer myself has no more money to add any embedded systems on the list.
> If you're willing to lend me your system and let it be tested and verified, I'm always ok with it.

## Requirements
- Raspberry pi (these are usually already installed with recent kernels)
  - python3
  - RPi.GPIO
- Radxa lite
  - python (may installed by default)
  - pyRock

```

sudo apt-get install gcc python-dev
git clone https://github.com/radxa/pyRock.git
cd pyRock
sudo python setup.py install
cd ..
rm -rf pyRock

```

### Features
- You can easily modify source yourself to choose which GPIO pins for which 7seg part.
- An init.d linux service file is included, so that you don't need to turn the program on every boot-ups.

### How to add as service
Simply run install_service.sh file with root access and `sh` command like this...
>sudo sh install_service.sh

### Example of GPIO pin connections
One 100 ohm resistor is connected to ground line of breadboard which will be connected with 7 segs ground pins.
Other 7 seg pins are connected to bunch of 3.3v GPIO pins on Radxa lite.
![alt tag](https://raw.github.com/chidea/pyGPIOclock/master/dist/image/IMG_20150624_060722_HDR.jpg)

### Features that may come in future...
- Pin configuration file
- Dot beeping & configuration to show periods of a second.