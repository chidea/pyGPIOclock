#!/usr/bin/env bash

if [ $(id -u) != "0" ]; then
    echo "You should use sudo."
    exit 1
fi

if [ -d /home/pi ]; then
    trg=raspberry_pi
elif [ -d /home/rock ]; then
    trg=radxa
else
    echo "Cannot find proper user folder."
    exit 1
fi

mkdir /etc/gpio_clock
cp $trg/clock.py /etc/gpio_clock/

chmod 755 $trg/gpio_clock
cp $trg/gpio_clock /etc/init.d/
update-rc.d gpio_clock defaults
service gpio_clock start