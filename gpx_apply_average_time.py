from datetime import *
import datetime as dt
import math

# --- Read .gpx file from route planner ---
in_file = open("file_from_route_planner.gpx", "r") # Add detail
lines = in_file.readlines()
in_file.close()

# --- Define start & end time ---
start_time = datetime.strptime("11/02/22 09:00", "%d/%m/%y %H:%M") # Add detail
finish_time = datetime.strptime("11/02/22 16:00", "%d/%m/%y %H:%M") # Add detail
t_stamps = [start_time]

# --- Calculate time increment ---
trkpt_count = 0
for line in lines:
    if "</trkpt>" in line:
        trkpt_count += 1

diff = finish_time - start_time
time_increment = math.floor(diff.seconds/trkpt_count)

# --- Logic ---
def time_print(line,time_stamps):
    if "<time>" in line:        
        tstamp = datetime.strftime(time_stamps[-1],"%H:%M:%S")
        time_stamps.append(time_stamps[-1] + dt.timedelta(seconds=time_increment))
        return '    <time> 2022-02-11T{}Z</time>'.format(tstamp)
    else:
        return line

result = [ time_print(x,t_stamps) for x in lines ]

# --- Print result ---
out_file = open("result.xml", "w")
for element in result:
    out_file.write(element)
out_file.close()
