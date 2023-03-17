#A health check module to check the disk usage and cpu usage

#1. shebang
#! /usr/bin/env python3

#import shutil and psutil modules to chceck disk usage and cpu usage
import shutil
import psutil

#function to check disk usage and only return if the free space is greater than 20 of total space
def check_disk_usage(disk):
  disk_usage = shutil.disk_usage(disk)
  free = disk_usage.free/disk_usage.total*100
  return free > 20

#function to check cpu usage in a 1 sec interval and only return if usage is less than 75 percent
def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 75

#if loop to display a message if either function above does not return a value or if everything is running fine
if not check_disk_usage("/") or not check_cpu_usage():
  print("ERROR! Please fix code")
else:
  pritn("Everything is good!")
