import threading
def fun():
    print "this is fun:"
def smile():
    print "hav a smile"

thread=[]
t1=threading.Thread(target=fun)
t2=threading.Thread(target=smile)
t1.run()
t2.start()

thread.append(t1)
thread.append(t2)
print thread
