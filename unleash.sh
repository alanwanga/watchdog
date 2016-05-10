#!/usr/bin/env sh
#autostart /etc/rc.local

sudo motion &
sudo python bottle_control.py &
sudo pytnon server_check.py &
