import os

power_now = int(os.popen("cat /sys/class/power_supply/BAT0/power_now").read())
total_energy = int(os.popen("cat /sys/class/power_supply/BAT0/energy_now").read())
capacity_percent = int(os.popen("cat /sys/class/power_supply/BAT0/capacity").read())

power_now /= 100 ** 3
total_energy /= 100 ** 3

print(f"Power Consumption: {power_now} W")
print(f"Total Energy: {total_energy} Wh ({capacity_percent}%)")
