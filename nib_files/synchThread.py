import threading
import logging
import time
logging.basicConfig(level=logging.DEBUG,\
    format='[%(levelname)s](%(threadName)-10s)%(message)s',)
def consumer(cond):
    '''wait for the condition n use resourse'''
    logging.debug('starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resourse is available to consumer')
def producer(cond):
    '''set up the resourse to be used by the consumer'''
    logging.debug('starting producer thread')
    with cond:
        logging.debug('making resource available')
        cond.notifyAll()
condition=threading.Condition()
c1=threading.Thread(name='c1',target=consumer,args=(condition,))
c2=threading.Thread(name='c2',target=consumer,args=(condition,))
p=threading.Thread(name='p',target=producer,args=(condition,))
c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

