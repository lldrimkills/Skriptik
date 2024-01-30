#!/usr/bin/env python

import shutil   # For copy fail
import os       # Foo GetFileSize and Check if file exist
import sys      # For CLS Arguments

if(len(sys.argv) < 4):
    print("Missing arguments! is script.py 10")
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):          # Check if file exist
    logfile_size = os.stat(file_name).st_size   # Get Filesize in Bytes
    logfile_size = logfile_size / 1024          # Convert from Bytes to Kilobytes

    if(logfile_size >= limitsize):
        if(logfile_size > 0):
            for currentsFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentsFileNum-1)
                dst = file_name + "_" + str(currentsFileNum)
                if(os.path.isfile(dst) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + "  to " + dst)


            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "  to " + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()
