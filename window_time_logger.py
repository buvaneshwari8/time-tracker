import subprocess
import time
import os
import csv
import sys
from datetime import datetime, timedelta

# -- set update/round time (seconds)

period = 1




def currtime(tformat=None):
    return time.strftime("%d_%m_%Y-%H_%M_%S") if tformat == "file" \
        else time.strftime("%d-%m-%Y %H:%M:%S")


def get(command):
    try:
        return subprocess.check_output(command).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        pass


def time_format(s):
    # convert time format from seconds to h:m:s
    (m, s) = divmod(s, 60)
    (h, m) = divmod(m, 60)
    return '%d:%02d:%02d' % (h, m, s)


def summarize():
    with open('/home/bhuvana/names.csv', 'w') as csvfile:
       # startt = currtime()
        start_time=datetime.now()
        endtime = start_time
        fieldnames = ['Starting_Time','Ending_Time', 'Application_Name', 'Total_Time', 'Screen_Time', 'Screen_Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        totaltime = sum([it[2] for it in winlist])
        for app in applist:
            wins = [r for r in winlist if r[0] == app]
            apptime = sum([it[2] for it in winlist if it[0] == app])
            appperc = round(100 * apptime / totaltime)
            for w in wins:
                   
                endtime = start_time + timedelta(seconds=w[2])
                                       
                print(start_time)
                print(endtime)
                print(w[1])
		 #application name(app), total time(app time), screen time(w[2]),screen name (w[1])
                writer.writerow({'Starting_Time': start_time,'Ending_Time': endtime,'Application_Name': app, 'Total_Time': time_format(apptime),'Screen_Time': time_format(w[2]),'Screen_Name': w[1]})
                start_time = endtime 		 


t = 0
applist = []
winlist = []
start_time=datetime.now()
endtime = start_time
while True:
    time.sleep(period)
    frpid = get(['xdotool', 'getactivewindow', 'getwindowpid'])
    frname = get(['xdotool', 'getactivewindow', 'getwindowname'])
    app = (get(['ps', '-p', frpid, '-o', 'comm=']) if frpid
                                                      != None else 'Unknown')

    # fix a few names

    if 'gnome-terminal' in app:
        app = 'gnome-terminal'
    elif app == 'soffice.bin':
        app = 'libreoffice'

    # add app to list

    if not app in applist:
        applist.append(app)
    checklist = [item[1] for item in winlist]
    if not frname in checklist:
        winlist.append([app, frname, 1 * period])
    else:

        winlist[checklist.index(frname)][2] = \
            winlist[checklist.index(frname)][2] + 1 * period
    if t == 60 / period:
        summarize()
        t = 0
    else:
        t += 1


