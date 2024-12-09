#!/bin/bash

mkdir -p /mnt/new/
cd /mnt/new/

OUTPUT_FILENAME="run_stats.txt"

while true; do
  sleep 30
  echo "*********************" >> $OUTPUT_FILENAME
  echo "`date`" >> $OUTPUT_FILENAME
  echo "`top -b -n 1 | head -6`" >> $OUTPUT_FILENAME
  echo "--------- TOP IO PROCS ------------" >> $OUTPUT_FILENAME
  echo "`iotop -P -a -o -b -n 1`" >> $OUTPUT_FILENAME
  echo "--------- TOP MEM PROCS ------------" >> $OUTPUT_FILENAME
  echo "`ps -e -o stat,pid,ppid,user,pcpu,pmem,args,wchan:32,args --sort=-pmem | head -5`" >> $OUTPUT_FILENAME
  echo "--------- TOP CPU PROCS ------------" >> $OUTPUT_FILENAME
  ps -e -o stat,pid,ppid,user,pcpu,pmem,args,wchan:32 --sort=-pcpu | head -15 >> $OUTPUT_FILENAME
  echo "--------- Procs in D state ------------" >> $OUTPUT_FILENAME
  ps -e -o stat,pid,ppid,user,pcpu,cmd,wchan:32 --sort=stat | grep "^D" | head -n 15 >> $OUTPUT_FILENAME
  ps -efl | awk 'BEGIN {running = 0; blocked = 0} $2 ~ /R/ {running++}; $2 ~ /D/ {blocked++} END {print "Number of running/blocked/running+blocked processes: "running"/"blocked"/"running+blocked}' >> $OUTPUT_FILENAME
  echo "--------- memory of individual process time ------------" >> $OUTPUT_FILENAME
  ps -eo size,pid,user,command --sort -size |awk '{ hr=$1/1024 ; printf("%13.2f Mb ",hr) } { for ( x=4 ; x<=NF ; x++ ) { printf("%s ",$x) } print "" }' |cut -d "" -f2 | head -n 500  >> $OUTPUT_FILENAME
  echo "-------- process calculated for RSS memory consumption ------" >> $OUTPUT_FILENAME
  ps -eo user,pid,ppid,cmd,pmem,rss --no-headers --sort=-rss | awk '{if ($2 ~ /^[0-9]+$/ && $6/1024 >= 1) {printf "PID: %s, PPID: %s, Memory consumed (RSS): %.2f MB, Command: ", $2, $3, $6/1024; for (i=4; i<=NF; i++) printf "%s ", $i; printf "\n"}}'
  echo "--------- N/W Info state ------------" >> $OUTPUT_FILENAME
  ip addr show >> $OUTPUT_FILENAME
  echo "--------- Netstat ------------" >> $OUTPUT_FILENAME
  ss -tnp | sort -t: -k2 -n >> $OUTPUT_FILENAME
  echo "--------- ss ------------" >> $OUTPUT_FILENAME
  ss -s >> $OUTPUT_FILENAME
  echo "--------- vmstat ------------" >> $OUTPUT_FILENAME
  vmstat -w -S M >> $OUTPUT_FILENAME
  echo "--------- vmstat disk ------------" >> $OUTPUT_FILENAME
  vmstat -d >> $OUTPUT_FILENAME
  echo "--------- sar disk ------------" >> $OUTPUT_FILENAME
  sar -d -p 5 2 >> $OUTPUT_FILENAME
  echo "--------- sar cpu ------------" >> $OUTPUT_FILENAME
  sar -P ALL 5 1 >> $OUTPUT_FILENAME
  echo "--------- done time ------------" >> $OUTPUT_FILENAME
  echo "`date`" >> $OUTPUT_FILENAME

  size="$(stat --format=%s $OUTPUT_FILENAME)"
  #if file is greater than 500mb tar gzip it
  if [ $size -gt 500000000 ]
  then
    if [ -f run_stats.tar.gz ]
    then
      #cp --force --backup=numbered run_stats.tar.gz run_stats.tar.gz
      rm run_stats.tar.gz
    fi
    tar -czf run_stats.tar.gz run_stats.txt
    rm run_stats.txt
    touch run_stats.txt
  fi
done

