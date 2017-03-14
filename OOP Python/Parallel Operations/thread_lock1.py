"""
Synchronize access to sdout through thread locking:
because it is a shared global, thread outputs may be intermixed if not
synced.

"""

import _thread as thread
import time


def counter(threadID, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print("[%s] =>%s" % (threadID, i))
        mutex.release()


mutex = thread.allocate_lock()

for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print("Exiting Main Thread.")


"""

OUTPUT:
[3] =>0
[4] =>0
[2] =>0
[1] =>0
[0] =>0
[1] =>1
[2] =>1
[4] =>1
[3] =>1
[0] =>1
[3] =>2
[4] =>2
[1] =>2
[2] =>2
[0] =>2
[1] =>3
[2] =>3
[3] =>3
[4] =>3
[0] =>3
[1] =>4
[2] =>4
[3] =>4
[0] =>4
[4] =>4
Exiting Main Thread.

"""
