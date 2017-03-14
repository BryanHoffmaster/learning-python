import threading
import _thread


def actionFunc(i):
	print(i ** 32)


#sublcass with state retaining per thread

class Mythread(threading.Thread):
	"""This class will call use a single thread to print the passed integer arg"""
	def __init__(self, i):
		self.i = i
		threading.Thread.__init__(self)
	def run(self):
		print(self.i ** 32)

Mythread(2).start()
"""
Just for reference, here is what the start method will be doing:

start(self)
    Start the thread's activity.
    
    It must be called at most once per thread object. It arranges for the
    object's run() method to be invoked in a separate thread of control.
    
    This method will raise a RuntimeError if called more than once on the
    same thread object.


"""


#Pass the actionFunc into the thread
thread = threading.Thread(target=(lambda: actionFunc(2)))
thread.start()

"""
Just for reference here is what is callable to the thread.Thread class

class Thread(builtins.object)
 |  A class that represents a thread of control.
 |  
 |  This class can be safely subclassed in a limited fashion. There are two ways
 |  to specify the activity: by passing a callable object to the constructor, or
 |  by overriding the run() method in a subclass.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)

"""
# Same as previous call but no lambda wrapper for state
threading.Thread(target=actionFunc, args=(2,)).start()

"""

In the next examples we'll see the use of bound methods to use. These examples also
maintain state. 

"""

# a non-threaded class with state OOP
class Power:
	"""docstring for Power"""
	def __init__(self, i):
		self.i = i
	def action(self):
		print(self.i ** 32)

#now we reference the class
obj = Power(2)
#use the bound method in a new thread
threading.Thread(target=obj.action).start()


#here is a nested scop to retain state
def action(i):
	def power():
		print(i ** 32)
	return power

threading.Thread(target=action(2)).start()
		