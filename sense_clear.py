#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# this script makes any LED's hat were preveously on be overwritten
# different script may have left on

print("clearing LEDs")

sense.clear()
