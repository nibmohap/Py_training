import fnmatch
import os
import glob
l=glob.iglob("*.py")
print list(l)
for file in os.listdir('.'):
    if fnmatch.fnmatch(file,'*.txt'):
        print file
