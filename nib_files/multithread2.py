import threading
def fun(*i):
    print "this is fun:",i
def smile(j):
    print "hav a smile",j

thread=[]
t1=threading.Thread(target=fun,args=(2,3,4))
t2=threading.Thread(target=smile,args=(3,))
t1.run()
t2.run()

thread.append(t1)
thread.append(t2)
print thread
