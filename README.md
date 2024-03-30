AUTOMATED SOSREPORT ANALYSIS

This python Script has been designed to read the sosreport for RHEL 8 version and extract data from sosreport for log analysis . This script pull the latest version of xsos open-source tool and will use them for extracting sosreport data and performs important error string search analysis from the messages , secure and dmesg files .

More information on Xsos : https://access.redhat.com/discussions/469323  https://access.redhat.com/solutions/511753

How to use this script :-

kindly download the main.py script on RHEL 8 VM and add execute permission to download main.py file and trigger as the script as given below .

Example :- #./main.py sosreport-RHEL8LAB-2023-01-30-qxhbofe.tar.xz

Error String Analysis :-

This script provide 8 different option to perform a error string analysis for the messages file present inside the sosreport .

Case 1 :- 1 To fetch error related to file system and disk

Case 2 :- 2 To fetch the error related to Memory

Case 3:- 3 To fetch the error related to softlock CPU and kernel panic

Case 4:- 4 To fetch possible error related to Antivirus issues and endpoint security daemon

Case 5:- 5 To fetch all possible error related to the messages files

Case 6:- 6 To search your own choice of one or more error strings from messages files

Case 7:- 7 To search your own choice of one or more error strings from dmesg files

Case 8:- 8 To search your own choice of one or more error strings from secure files

case 9:- 9 Exit option selected to come out of this script

Future Plan : We are planning to extend the AUTOMATED SOSREPORT ANALYSIS for differnet version on RHEL , Centos and Oracle linux and SUSE distro also . a) Preparing similar script for RHEL 7 and 9 which will compatible for similar version on Centos and Oracle linux . b) Preparing separate script to Suse 12 and Suse 15 .

https://snapcraft.io/install/xsos/opensuse
