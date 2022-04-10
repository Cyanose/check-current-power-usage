#!/bin/sh

# important for math:
# There are 2 batteries in this x270 thinkpad: 
# 1. internal battery with the design capacity of 23.48Wh (26.54% of full energy pull)
# 2. external battery with the design capacity of 65Wh (73.46% of full energy pool)

echo - | awk "{printf \"Power Consumption: %.1fW\n\", ($(< /sys/class/power_supply/BAT0/power_now)+$(< /sys/class/power_supply/BAT1/power_now))/1000000 }"
echo - | awk "{printf \"Total Energy: %.1fWh (%.f%)\n\", 
($(< /sys/class/power_supply/BAT0/energy_now) + $(< /sys/class/power_supply/BAT1/energy_now) )/1000000,
( ($(< /sys/class/power_supply/BAT0/capacity) * 26.54 + $(< /sys/class/power_supply/BAT1/capacity) * 73.46)/100) } "
