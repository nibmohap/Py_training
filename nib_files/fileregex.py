import re
import sys
import fileinput
pattern=re.compile(sys.argv[-1])
for line in fileinput.input(sys.argv[2:]):
    if pattern.search(line):
        fmt='{filename:<20}:{lineno}:{line}'
        print fmt.format(filename=fileinput.filename(),lineno=fileinput.filelineno(),line=line.rstrip())
        
