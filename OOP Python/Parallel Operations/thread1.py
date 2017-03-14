"""

Will spawn threads till you type 'q'

"""

import _thread


def child(tid):
    print("hello from thread", tid)


def parent():
    i = 0
    while True:
        i += 1
        # quick and dirty tuple (i,)
        _thread.start_new_thread(child, (i,))
        if input() == 'q':
            break


parent()
