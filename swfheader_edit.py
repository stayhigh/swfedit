#!/usr/bin/python

import sys
import struct

def show_err(msg,exit_code):
    print msg
    print "# overwrite the header of filesize in swf"
    print "[usage] " + sys.argv[0] + " <swf_file>  "  + " <filesize>"
    exit(exit_code)

if len(sys.argv) != 3:
    show_err("system arg in wrong", 1)

filename = sys.argv[1]
filesize = int(sys.argv[2])
mode = "rb+"

f = open(filename, mode)
f.seek(4)
f.write(struct.pack('@i',filesize))
f.close()
