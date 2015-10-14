class ShortInput(Exception):
    '''Short input exception class'''
    def __init__(self,length,atleast):
        '''Initialise Short input exception class'''
        self.length=length #object variable
        self.atleast=atleast#object variable
        print "Short in put exception,input should be mininmum 6"
o=ShortInput(8,5)
try:
    s=raw_input("input data:")
    if len(s)<6:
        raise ShortInput(len(s),6)
except ShortInput,x:
    print 'you enterd %d bytes expected %d bytes'%(x.length,x.atleast)
else:
    print 'ur data is %s'%s

