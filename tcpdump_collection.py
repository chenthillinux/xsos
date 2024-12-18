# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:46:44 2024

@author: chlingam
"""

import subprocess
import time
import os
import threading


# Function to trigger tcpdump for 10 minutes
def run_tcpdump():
    # Check if tcpdump is already running
    tcpdump_running = subprocess.run(['pgrep', 'tcpdump'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

    if not tcpdump_running:
        # Run tcpdump for 10 minutes
        tcpdump_command = ['sudo', 'tcpdump', '-i', 'eth0', '-w', 'capture_tcpdump_`date +%y%m%d-%H:%M:%S`', '-G', '60', '-W', '1']
        subprocess.Popen(tcpdump_command)


def top_collection():
    top_output = subprocess.check_output("top -b -n 5", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("top_output.txt", "a") as top_file:
        top_file.write(date_output.decode())
        top_file.write(top_output.decode())

def iotop_collection():
    iotop_output = subprocess.check_output("iotop -b -n 5", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("iotop_output.txt", "a") as iotop_file:
        iotop_file.write(date_output.decode())
        iotop_file.write(iotop_output.decode())

def sar_collection():
    sar_output = subprocess.check_output("sar -dp 1 3", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("sar_output.txt", "a") as sar_file:
        sar_file.write(date_output.decode())
        sar_file.write(sar_output.decode())

def ps_memory_collection():
    psmem_output = subprocess.check_output("ps -e -o stat,pid,ppid,user,pcpu,pmem,args,wchan:32,args --sort=-pmem | head -50", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("psmem_output.txt", "a") as psmem_file:
        psmem_file.write(date_output.decode())
        psmem_file.write(psmem_output.decode())

def ps_cpu_collection():
    pscpu_output = subprocess.check_output("ps -e -o stat,pid,ppid,user,pcpu,pmem,args,wchan:32 --sort=-pcpu | head -50", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("ps_cpu_output.txt", "a") as pscpu_file:
        pscpu_file.write(date_output.decode())
        pscpu_file.write(pscpu_output.decode())

def dstate_collection():
    dstate_output = subprocess.check_output("ps -e -o stat,pid,ppid,user,pcpu,cmd,wchan:32 --sort=stat | grep -w D", shell=True)
    date_output = subprocess.check_output("date", shell=True)
    with open("Dstate_output.txt", "a") as dstate_file:
        dstate_file.write(date_output.decode())
        dstate_file.write(dstate_output.decode())


def watch_log_and_tcpdump(file_path, error_strings):
    new_file_path = 'error_log.txt'
    tcpdump_triggered = False

    # Command to continuously monitor the log file
    tail_command = ['tail', '-f', file_path]

    # Start the tail command process
    process = subprocess.Popen(tail_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Open a new file to write the error string lines
    with open(new_file_path, 'a') as new_file:
        start_time = time.time()
        while time.time() - start_time <= 300:  # Monitor for 1 day
            line = process.stdout.readline().strip()
            if line:
                for error_string in error_strings:
                    if error_string in line:
                        print(f"Error string '{error_string}' found in log: {line}")
                        new_file.write(f"{line}\n")  # Write the error string line to the new file
                        if not tcpdump_triggered:
                            #run_tcpdump()
                            t1 = threading.Thread(target=run_tcpdump, name='t1')
                            t2 = threading.Thread(target=top_collection, name='t2')
                            t3 = threading.Thread(target=iotop_collection, name='t3')
                            t4 = threading.Thread(target=sar_collection, name='t4')
                            t5 = threading.Thread(target=ps_memory_collection, name='t5')
                            t6 = threading.Thread(target=ps_cpu_collection, name='t6')
                            t7 = threading.Thread(target=dstate_collection, name='t7')


                            t1.start()
                            t2.start()
                            t3.start()
                            t4.start()
                            t5.start()
                            t6.start()
                            t7.start()

                            t1.join()
                            t2.join()
                            t3.join()
                            t4.join()
                            t5.join()
                            t6.join()
                            t7.join()
                            #tcpdump_triggered = True
                            #break

# Example usage: Watch for multiple error strings in '/var/log/syslog' file for 1 day
error_strings_to_watch = ['ERROR', 'WARNING', 'CRITICAL']
watch_log_and_tcpdump('/var/log/syslog', error_strings_to_watch)
