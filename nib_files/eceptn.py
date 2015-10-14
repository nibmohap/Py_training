try:
    x=int(raw_input("enter some data:"))
except ValueError as e:
    print "Enter integer data only",e
except Exception,e1:
    print "New Exception :",e1
else:
    print "No Exception :",x
