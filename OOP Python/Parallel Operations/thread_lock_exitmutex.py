"""
Uses mutexes to know when threads are done (globally) in parent/main thread,
instead of time.sleep; lock stdout to avoid comingled prints.

"""
import _thread as thread

# This gives a pointer to the locking mechanism for each thread to use.
stdoutmutex = thread.allocate_lock()

# Creates an iterator that makes a set of 10  LOCKED threads in a list.
# They will be "acquired" when the the iterable thread has itself gained
# a lock from "stdoutmutex" and then released it.acquire
# NOTE: I have a feeling this isn't a good way to do this.acquire
exitmutexes = [thread.allocate_lock() for i in range(10)]


def counter(threadID, count):
    for i in range(count):
        stdoutmutex.acquire()
        print("[%s] =>%s" % (threadID, i))
        # make sure to release the lock!!
        stdoutmutex.release()
    # signal to main thread:
    exitmutexes[threadID].acquire()


for i in range(10):
    thread.start_new_thread(counter, (i, 2))

for mutex in exitmutexes:
    while not mutex.locked():
        pass

print('Main Thread Exiting')
