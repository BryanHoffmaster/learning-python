"""
This example will use the Queue module to allow threads to work on a
on a global stack.
"""

import threading
import queue
import time


numconsumers = 2
numproducers = 4
nummessages = 5

safePrint = threading.Lock()
dataQueue = queue.Queue()


def producer(threadID):
    for msgnum in range(nummessages):
        time.sleep(threadID)
        dataQueue.put('[producer id=%d, count=%d]' % (threadID, msgnum))


def consumer(threadID):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safePrint:
                print('consumer', threadID, 'got=>', data)


if __name__ == '__main__':
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i,))
        # cannot exit while not enabled as a daemon!!
        thread.daemon = True
        thread.start()

    waitfor = []
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i,))
        thread.start()

    for thread in waitfor:
        thread.join()
        # or a time.sleep long enough for here
    print('Main Thread Exit.')
