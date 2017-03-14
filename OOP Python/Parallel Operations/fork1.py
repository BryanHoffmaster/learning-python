import os


def child():

    print("hello from child process", os.getpid())
    os._exit(0)


def parent():
    while True:
        newPID = os.fork()
        if newPID == 0:
            child()
        else:
            print("Hello From Parent Process:", os.getpid(), newPID)
        if input() == 'q':
            break


parent()
