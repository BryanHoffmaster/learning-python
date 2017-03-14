import traceback
import sys


def exceptionTest(x):
    raise TypeError('string test of excpection TypeError')


try:
    exceptionTest('test1')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
