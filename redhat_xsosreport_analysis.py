#!/usr/bin/env python3

import os
import subprocess
import sys
import re
import glob
import gzip
import shutil


print('cmd entry:', sys.argv)


xsos_download = subprocess.run(["curl","-Lo","/usr/local/bin/xsos","bit.ly/xsos-direct"])
xsos_download_status = xsos_download.returncode

if ( xsos_download_status == 0 ):
        print("xsos downloaded sucessfully.")
else:
        print("xsos failed to get download.")

xsos_execute_permission = subprocess.run(["chmod","+x","/usr/local/bin/xsos"])
xsos_execute_permission_returcode = xsos_execute_permission.returncode

if ( xsos_execute_permission_returcode == 0 ):
        print("xsos execute granded .")
else:
        print("xsos execute premission granting failed")


sosreport_unxz = subprocess.run(["unxz",sys.argv[1]])
sosreport_unxz_status = sosreport_unxz.returncode

if ( sosreport_unxz_status == 0 ):
        print("sosreport extracted sucessfully.")
else:
        print("sosreport extraction failed")

unxz_tar_file_name = sys.argv[1]
sosreport_directory = unxz_tar_file_name.split(".tar",1)[0]
print(sosreport_directory)
sosreport_var_log_directory = "{}/var/log".format(sosreport_directory)
print(sosreport_var_log_directory)

current_dir = os.getcwd()
print(current_dir)

absolute_path = os.path.join(current_dir, sosreport_var_log_directory)
full_path_sosreport_var_log_directory = os.path.join(current_dir, sosreport_var_log_directory)
print(full_path_sosreport_var_log_directory)

tar_file_name  = unxz_tar_file_name.split(".xz",1)[0]

untar_filename = subprocess.run(["tar","-xf",unxz_tar_file_name.split(".xz",1)[0]])
untar_filename_status = untar_filename.returncode

if ( untar_filename_status == 0 ):
        print("tar  extracted sucessfully.")
else:
        print("tar extraction failed")

xsos_execution =  subprocess.run(["/usr/local/bin/xsos","--all",unxz_tar_file_name.split(".tar",1)[0]])
xsos_execution_status = xsos_execution.returncode

if ( xsos_execution_status == 0 ):
        print("xsos execution completed sucessfully.")
else:
        print("xsos execution failed")



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
        os.chdir(full_path_sosreport_var_log_directory)
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
def error_string_search_dmesg(strings_to_search):
# Find all .txt files in the current directory
        os.chdir(full_path_sosreport_var_log_directory)
        # Find all .txt fils in the current directory
        txt_files = glob.glob('dmesg*')
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

#### Function to search secure files the Error string ########
def error_string_search_secure(strings_to_search):
# Find all .txt files in the current directory
        os.chdir(full_path_sosreport_var_log_directory)
        # Find all .txt fils in the current directory
        txt_files = glob.glob('secure*')
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



#### Messages greping section #################

while True:
    options = {1: "To fetch error related to file system and disk", 2: "To fetch the error related to Memory", 3: "To fetch the error related to softlock CPU and kernel panic", 4: "To fetch possible error related to Antivirus issues and endpoint security daemon", 5: "To fetch all possible error related to the messages", 6:"To search any given strings from messages file ", 7: "To search any given strings from dmesg file ", 8: "To search any given strings from secure file ", 9: "Exit option selected to come out of this script"}

    print("Select an option , i.e provide the input as number for the option:")
    for key, value in options.items():
        print(key, value)

    selected_option = int(input())

    if selected_option == 1:

        print("You selected Option 1 , which fetch error related to file system and disk")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_sosreport_var_log_directory)

        # List of strings to search for
        strings_to_search = ['fsck','XFS internal error','xfs_force_shutdown','I/O error','xfs_do_force_shutdown','Corruption detected','xfs_buf_ioend','xfs_trans_read_buf','xfs_inode block','io_schedule_timeout','xfs_inode','xfs_inactive_ifree','xfs_iunlink_remove','xfs_imap_to_bp','EXT4-fs error','EXT4-fs warning','JBD: Spotted dirty metadata buffer','EXT3-fs error','blk_update_request','Buffer I/O error']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 2:
        print("You selected Option 2, which fetch error related to Memory")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_sosreport_var_log_directory)
        # List of strings to search for
        strings_to_search = ['lowmem_reserve','Out of memory:','Killed process','oom-killer','check_panic_on_oom','oom_score_adj','do_page_fault']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 3:
        print("You selected Option 3, which fetch error related to softlock CPU and kernel panic")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_sosreport_var_log_directory)
        # List of strings to search for
        strings_to_search = ['BUG: soft lockup','__do_softirq','RIP:','_raw_spin_unlock_irqrestore','unable to handle kernel paging request','unable to handle kernel NULL pointer dereference','Oops:','BUG:','PGD','Oops:','segfault at','do_page_fault','Kernel panic - not syncing','Fatal exception']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 4 :
        print("To fetch possible error related to Antivirus issues and endpoint security daemon")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_sosreport_var_log_directory)
        # List of strings to search for
        strings_to_search = ['falcon_lsm_serviceable','twnotify_sys_close','twnotify','tmhook_invoke','tmhook_handler','dsa_filter','core_pkt_filter','core_pkt_hook','symev_rh_','symev_hook','cshook_network_ops']
        #### Calling Function to search the Error string ####
        error_string_search(strings_to_search)

    elif selected_option == 5 :
        print("To fetch all possible error related to the messages")

        ## Calling Uncompress Function inside /var/log #####
        gz_extract(full_path_sosreport_var_log_directory)
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
        error_string_search_dmesg(strings_to_search)



    elif selected_option == 8 :

        #### To fetch the input string #######
        print("This option will help you to search errors inside secure file . Please provide your  one or more error strings as requested below")
        input_strings_to_search = input("Enter multiple strings separated by comma: ")
        strings_to_search = input_strings_to_search.split(",")
        error_string_search_secure(strings_to_search)

    elif selected_option == 9 :

        #### To exit the program #######
        exit()
    else:
        print("Invalid option selected")