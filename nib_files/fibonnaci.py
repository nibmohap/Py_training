class fibnum:
    def __init__(self):
        self.fn2=1
        self.fn1=1
    def next(self):
        (self.fn1,self.fn2,oldfn2)=(self.fn1+self.fn2,self.fn1,self.fn2)
        return oldfn2
    def __iter__(self):
        return self

f=fibnum()
for i in f:
    print i
    if i>10:
        break
