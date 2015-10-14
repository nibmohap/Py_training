import threading
import logging
import time
logging.basicConfig(level=logging.DEBUG,\
    format='[%(levelname)s](%(threadName)-10s)%(message)s',)
def daemon():
    logging.debug('starting')
    time.sleep(5)
    logging.debug('exiting')
d=threading.Thread(name='daemon',target=daemon)
d.setDaemon(True)
def non_daemon():
    logging.debug('starting')
    logging.debug('exiting')
t=threading.Thread(name='non_daemon',target=non_daemon)
#w=threading.Thread(name='worker',target=worker)
#w2=threading.Thread(target=worker)
d.start()
t.start()
d.join()
t.join()

