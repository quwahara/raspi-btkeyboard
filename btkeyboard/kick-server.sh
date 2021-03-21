#!/bin/bash
set -x

service bluetooth stop
/usr/lib/bluetooth/bluetoothd -P input &
python3 keyboard/btk_server.py
