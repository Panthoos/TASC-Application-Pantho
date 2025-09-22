#!/usr/bin/env python3
# Note I just initialized these variables with specifec values
# Typically I assume the program would collect these values from somewhere else
# like an ex. relationship like motor/sensor -> txt file -> python file -> publisher/subscriber nodes 

lat, lon = 37.5, 40.3 # deg
bat_level = 63 # some % based on a charge function
object_dist = 4.7 # in meters
internal_temp, external_temp = 39.6, -5.0 # degrees celcius
signal_strength = 70 # dBm
commanded_speed = 0.50 # m/s
measured_speed = 0.43

gps = [lat, lon]
battery = [bat_level]
sensors = [object_dist, internal_temp, external_temp]
comstrength = [signal_strength]
motorfeedback = [commanded_speed, measured_speed]
