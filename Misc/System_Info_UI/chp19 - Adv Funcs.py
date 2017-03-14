# Recursive functions:
def mysum(mylist):
    if not mylist:
        return 0
    else:
        return mylist[0] + mysum(mylist[1:])


# recursive alternatives to previous function:

"""
def mysum(mylist):
	return 0 if not mylist else mylist[0] + mysum(mylist[1:])

def mysum(mylist):
	return mylist[0] if len(mylist) == 1 else mylist[0] + mysum(mylist[1:])

# Using extend sequence assignmnet  -- Neato
# This will work on ANY interable object, including open input files
def mysum(mylist):
	first, *rest = mylist
	return first if not rest else first + mysum(rest)



"""


def sumtree(L):
	tot = 0
    print(L)
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)

    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
