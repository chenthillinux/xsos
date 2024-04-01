AUTOMATED SOSREPORT ANALYSIS

xsosreport and xsupportconfig python Script has been designed to read the sosreport and supportconfig OS logs and extract data from sosreport/supportconfig for log analysis . This script pull the latest version of xsos open-source tool and will use them for extracting sosreport data and performs important error string search analysis from the messages , secure and dmesg files .

Redhat and Ubuntu Xsosreport analysis scripts leverage the latest version of the open-source Xsos tool to extract data from the sosreport and perform important error string search analysis on the messages, secure, and dmesg files.
SuSE Xsupportconfig analysis script was ingeniously developed from scratch without relying on any open-source tools. It was built to perform the same activities as the Redhat and Ubuntu Xsosreport tools, providing a comprehensive solution for log analysis across different Linux distributions.

More information on Xsos : https://access.redhat.com/discussions/469323  https://access.redhat.com/solutions/511753

We have developed three distinct scripts customized for the major Linux flavors running on the Azure Platform:

1. Redhat Xsosreport Python Script: Compatible to run on Red Hat Enterprise Linux, Oracle Linux, CentOS, Alma Linux, Rocky Linux, CBL-Mariner, and other Red Hat-based distributions.
2. Ubuntu Xsosreport Python Script: Designed for Ubuntu and other Debian-based Linux distributions.
3. SuSE Xsupportconfig Python Script: Tailored for openSUSE and SLES flavors.
   
Error String Analysis:-

These scripts provide eight different options to perform automated error string analysis for the given sosreport or supportconfig:


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

Note: In the future, we can enhance these scripts by incorporating additional error strings and scenarios, making them more intelligent and capable of handling multiple error conditions.

How to use this script :-

kindly download the  script o add execute permission to download file and trigger as the script as given below .

For Red Hat:
# python3 redhat_xsosreport_analysis.py sosreport-RHEL8LAB-2023-01-30-qxhbofe.tar.xz

For Ubuntu (Use Ubuntu 20.04 ):
# python3 redhat_xsosreport_analysis.py sosreport-ubuntu22node2-2024-03-13-yktkzek.tar

For SuSE:
# python3 suse_xsupport_config_analysis.py scc_suse15sp4lab_240319_1738.txz


