#!/usr/bin/env python3

import os
import subprocess
import sys
import re
import glob
import gzip
import shutil

print('cmd entry:', sys.argv)
print("Uncompressing the supportconfig file:", sys.argv[1])

supportconfig_unxz = subprocess.run(["tar", "-xf", sys.argv[1]])
supportconfig_unxz_status = supportconfig_unxz.returncode

if supportconfig_unxz_status == 0:
    print("supportconfig extracted successfully.")
else:
    print("supportconfig extraction failed")

unxz_tar_file_name = sys.argv[1]
print(unxz_tar_file_name)

supportconfig_directory = unxz_tar_file_name.split(".")[0]
print(supportconfig_directory)

current_dir = os.getcwd()
print(current_dir)

absolute_path = os.path.join(current_dir, supportconfig_directory)
full_path_supportconfig_directory = os.path.join(current_dir, supportconfig_directory)
print(full_path_supportconfig_directory)


# Checking the present of the file

def is_file_present(directory, file_name):

    file_path = os.path.join(directory, file_name)
    return os.path.isfile(file_path)

# Working on the basic-environment.txt to extract the data

def basic_environment_file(directory):

    file_name = "basic-environment.txt"
    complete_path_of_file = os.path.join(directory, file_name)
    print(complete_path_of_file)


    if is_file_present(directory, file_name):
        print(f"The file {file_name} exists in {directory}")
        x = open(complete_path_of_file)
        for line in x:
            if line.startswith("Linux"):
                print("\n")
                print("Basic Environment Content of the VM:")
                words = line.split()
                print("Hostname: ",words[1])
                print("Kernel Version: ",words[2])
                print("Architecture :",words[13])
                print("\n")
        x.close()
    else:
        print(f"The file {file_name} does not exist in {directory}")

    if is_file_present(directory, file_name):
        print("OS Release version and Manufacturer:")
        x = open(complete_path_of_file)
        for line in x:
            if line.startswith("NAME"):
                print(line)
            if line.startswith("VERSION="):
                print(line)
            if line.startswith("VERSION_ID"):
                print(line)
            if line.startswith("PRETTY_NAME="):
                print(line)
            if line.startswith("Manufacturer"):
                print(line)
            if line.startswith("Hardware"):
                print(line)
            if line.startswith("Hypervisor"):
                print(line)
        x.close()
    else:
        print(f"The file {file_name} does not exist in {directory}")


def basic_health_check_file(directory):

    file_name = "basic-health-check.txt"
    complete_path_of_file = os.path.join(directory, file_name)
    print(complete_path_of_file)


    if is_file_present(directory, file_name):
        x = open(complete_path_of_file,'r')
        print(x.read())
    else:
        print(f"The file {file_name} does not exist in {directory}")


def boot_information(directory):
    file_name = "boot.txt"  # Replace with the actual filename
    complete_path_of_file = os.path.join(directory, file_name)
    print(complete_path_of_file)
    print("BOOTED INFORMATION:-")

    start_string = '/usr/bin/last'
    end_string = '#==[ Configuration File ]'

    with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)



def memory_information(directory):
   file_name = "memory.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("MEMORY INFORMATION:-")

   start_string = '#==[ Command ]==='
   end_string = '#==[ Configuration'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)



def kdump_information(directory):
   file_name = "crash.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("KDUMP INFORMATION:-")

   start_string = 'Verification'
   end_string = '#==[ Configuration File'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def cron_information(directory):
   file_name = "cron.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("CRON INFORMATION:-")

   start_string = 'Verification'
   end_string = '### System Cron Job File Content ###'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)


def ha_config_show(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("HA CLUSTER CONFIG SHOW")

   start_string = '# /usr/sbin/crm configure show'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)


def ha_crm_mon(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("HA CLUSTER - CRM_MON -A -1")

   start_string = '# /usr/sbin/crm_mon -A -1'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def ha_crm_mon(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("HA CLUSTER - CRM_MON -A -1")

   start_string = '# /usr/sbin/crm_mon -A -1'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def pacemaker_status(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("PACEMAKER STATUS")

   start_string = '# /bin/systemctl status pacemaker.service'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def corosync_conf(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("COROSYNC CONF FILE - /etc/corosync/corosync.conf :-")

   start_string = '# /etc/corosync/corosync.conf'
   end_string = '#==[ Configuration File ]===========================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)


def corosync_conf(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("COROSYNC CONF FILE - /etc/corosync/corosync.conf :-")

   start_string = '# /etc/corosync/corosync.conf'
   end_string = '#==[ Configuration File ]===========================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)


def sbd_conf(directory):
   file_name = "ha.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("SBD CONF FILE - /etc/sysconfig/sbd :-")

   start_string = '# /etc/sysconfig/sbd'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def network_service_status(directory):
   file_name = "network.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("NETWORK SERVICE STATUS :-")

   start_string = '# /bin/systemctl status network.service'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def wicked_service_status(directory):
   file_name = "network.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("WICKED SERVICE STATUS :-")

   start_string = '# /usr/sbin/wicked ifstatus --verbose all'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)


def ip_route_status(directory):
   file_name = "network.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("IP ROUTE STATUS :-")

   start_string = '# /sbin/ip route'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def ip_link_status(directory):
   file_name = "network.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("IP LINK STATUS :-")

   start_string = '# /sbin/ip route'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)

def netstat_status(directory):
   file_name = "network.txt"  # Replace with the actual filename
   complete_path_of_file = os.path.join(directory, file_name)
   print(complete_path_of_file)
   print("NETSTAT STATUS :-")

   start_string = '# /bin/netstat -nap'
   end_string = '#==[ Command ]======================================#'

   with open(complete_path_of_file, 'r') as file:
        printing = False  # Flag to control printing lines
        for line in file:
            if start_string in line:
                printing = True  # Start printing when start_string is found
            elif end_string in line:
                printing = False  # Stop printing when end_string is found
            elif printing:
                print(line.rstrip())  # Print lines between start and end (remove trailing whitespace)
                
                
### Function to Uncompress the .gz file inside the /var/log #####
def gz_extract(directory):
    extension = ".gz"
    os.chdir(directory)
    for item in os.listdir(directory): # loop through items in dir
      if item.endswith(extension): # check for ".gz" extension
          gz_name = os.path.abspath(item) # get full path of files
          file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] #get file name for file within
          with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
              shutil.copyfileobj(f_in, f_out)
          os.remove(gz_name) # delete zipped file

#### Function to search messages files the Error string ########
def error_string_search(strings_to_search):
# Find all .txt files in the current directory
        os.chdir(full_path_supportconfig_directory)
        # Find all .txt fils in the current directory
        txt_files = glob.glob('messages*')
        # Iterate over the files
        for txt_file in txt_files:
            with open(txt_file) as f:
                # Read the contents of the file into a string
                file_contents = f.read()
                # Iterate over the strings to search for
                for search_string in strings_to_search:
                    # Search for the string in the file
                    if re.search(search_string, file_contents):
                        print(f'Found {search_string} in {txt_file}')
                        # Print the lines containing the string
                        for line in file_contents.split('\n'):
                            if search_string in line:
                                print(line)
                                
#### Function to search dmesg files the Error string ########
def error_string_search_warn(strings_to_search):
# Find all .txt files in the current directory
        os.chdir(full_path_supportconfig_directory)
        # Find all .txt fils in the current directory
        txt_files = glob.glob('warn*')
        # Iterate over the files
        for txt_file in txt_files:
            with open(txt_file) as f:
                # Read the contents of the file into a string
                file_contents = f.read()
                # Iterate over the strings to search for
                for search_string in strings_to_search:
                    # Search for the string in the file
                    if re.search(search_string, file_contents):
                        print(f'Found {search_string} in {txt_file}')
                        # Print the lines containing the string
                        for line in file_contents.split('\n'):
                            if search_string in line:
                                print(line)

basic_environment_file(full_path_supportconfig_directory)
basic_health_check_file(full_path_supportconfig_directory)
boot_information(full_path_supportconfig_directory)
#memory_information(full_path_supportconfig_directory)
network_service_status(full_path_supportconfig_directory)
wicked_service_status(full_path_supportconfig_directory)
ip_route_status(full_path_supportconfig_directory)
ip_link_status(full_path_supportconfig_directory)
netstat_status(full_path_supportconfig_directory)
kdump_information(full_path_supportconfig_directory)
cron_information(full_path_supportconfig_directory)
ha_config_show(full_path_supportconfig_directory)
ha_crm_mon(full_path_supportconfig_directory)
pacemaker_status(full_path_supportconfig_directory)
corosync_conf(full_path_supportconfig_directory)
sbd_conf(full_path_supportconfig_directory)

#### Messages greping section #################

while True:
    options = {1: "To fetch error related to file system and disk", 2: "To fetch the error related to Memory", 3: "To fetch the error related to softlock CPU and kernel panic", 4: "To fetch possible error related to Antivirus issues and endpoint security daemon", 5: "To fetch all possible error related to the messages", 6:"To search any given strings from messages file ", 7: "To search any given strings from Warning file ", 8: "Exit option selected to come out of this script"}

    print("Select an option , i.e provide the input as number for the option:")
    for key, value in options.items():
        print(key, value)

    selected_option = int(input())

    if selected_option == 1:

        print("You selected Option 1 , which fetch error related to file system and disk")

        ## Calling Uncompress Function #####
        gz_extract(full_path_supportconfig_directory)

        # List of strings to search for
        strings_to_search = ['fsck','XFS internal error','xfs_force_shutdown','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp','EXT4-fs error','EXT4-fs warning','JBD: Spotted dirty metadata buffer','EXT3-fs error','blk_update_request','Buffer I/O error']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 2:
        print("You selected Option 2, which fetch error related to Memory")

        ## Calling Uncompress Function  #####
        gz_extract(full_path_supportconfig_directory)
        # List of strings to search for
        strings_to_search = ['lowmem_reserve','Out of memory:','Killed process','oom-killer','check_panic_on_oom','oom_score_adj','do_page_fault']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 3:
        print("You selected Option 3, which fetch error related to softlock CPU and kernel panic")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_supportconfig_directory)
        # List of strings to search for
        strings_to_search = ['BUG: soft lockup','__do_softirq','RIP:','_raw_spin_unlock_irqrestore','unable to handle kernel paging request','unable to handle kernel NULL pointer dereference','Oops:','BUG:','PGD','Oops:','segfault at','do_page_fault','Kernel panic - not syncing','Fatal exception']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 4 :
        print("To fetch possible error related to Antivirus issues and endpoint security daemon")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_supportconfig_directory)
        # List of strings to search for
        strings_to_search = ['falcon_lsm_serviceable','twnotify_sys_close','twnotify','tmhook_invoke','tmhook_handler','dsa_filter','core_pkt_filter','core_pkt_hook','symev_rh_','symev_hook','cshook_network_ops']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 5 :
        print("To fetch all possible error related to the messages")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_supportconfig_directory)
        # List of strings to search for
        strings_to_search = ['fsck','XFS internal error','xfs_force_shutdown','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp','EXT4-fs error','EXT4-fs warning','JBD: Spotted dirty metadata buffer','EXT3-fs error','blk_update_request','Buffer I/O error''lowmem_reserve','Out of memory:','Killed process','oom-killer','check_panic_on_oom','oom_score_adj','do_page_fault','BUG: soft lockup','__do_softirq','RIP:','_raw_spin_unlock_irqrestore','unable to handle kernel paging request','unable to handle kernel NULL pointer dereference','Oops:','BUG:','PGD','Oops:','segfault at','do_page_fault','Kernel panic - not syncing','Fatal exception','falcon_lsm_serviceable','twnotify_sys_close','twnotify','tmhook_invoke','tmhook_handler','dsa_filter','core_pkt_filter','core_pkt_hook','symev_rh_','symev_hook']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)


    elif selected_option == 6 :

        #### To fetch the input string #######
        print("This option will help you to search errors inside messages file . Please provide your one or more error strings as requested below")
        input_strings_to_search = input("Enter multiple strings separated by comma: ")
        strings_to_search = input_strings_to_search.split(",")

        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)


    elif selected_option == 7 :

        #### To fetch the input string #######
        print("This option will help you to search errors inside dmesg file . Please provide your one or more error strings as requested below")
        input_strings_to_search = input("Enter multiple strings separated by comma: ")
        strings_to_search = input_strings_to_search.split(",")
        error_string_search_warn(strings_to_search)


    elif selected_option == 8 :

        #### To exit the program #######
        exit()
    else:
        print("Invalid option selected")
