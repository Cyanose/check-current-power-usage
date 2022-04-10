# Check current power usage on linux laptop

Simple script to estimate the  current power usage of linux laptop, works fine on x270 thinkpad running Arch

# Calculations

The calculations will work properly only with 24Wh internal battery combined with 65Wh external battery(weighted mean), many thinkpads are distributed with external battery of 24Wh capacity, in this case while estimating the remaining % you can just add the two values from /sys/class/power_supply/BAT*(x)*/capacity and divide them by 2(arithemtic mean)
