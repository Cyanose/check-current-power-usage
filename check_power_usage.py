#!/bin/python
import os
from colorama import Fore

battery_prefix = "/sys/class/power_supply/BAT0/"
ac_prefix = "/sys/class/power_supply/AC"
color = Fore.CYAN
color_reset = Fore.RESET


power_now = int(os.popen(f"cat {battery_prefix}/power_now").read())
total_energy = int(os.popen(f"cat {battery_prefix}/energy_now").read())
capacity_percent = int(os.popen(f"cat {battery_prefix}/capacity").read())
ac_connected = bool(int(os.popen(f"cat {ac_prefix}/online").read()))

power_now /= 100**3
total_energy /= 100**3

print(f"Total Energy: {color}{total_energy}{color_reset} Wh ({color}{capacity_percent}%{color_reset})")
print(f"Power Usage:  {color}{power_now}{color_reset} W")
print(f"AC Connected: {color}{ac_connected}{color_reset}")
