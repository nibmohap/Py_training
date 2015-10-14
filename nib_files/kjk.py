import fnmatch
import os
for file in os.list('.'):
    if fnmatch.fnmatch(file,'*.xml'):
        print file
