import numpy as np

SIZE = 2_000_000

# Create Python's lists
l1 = range(SIZE)
l2 = range(SIZE)

# Create Numpy Arrays
a1=np.arange(SIZE)
a2=np.arange(SIZE)


# The point to point sum on both data structures
def python_lists():
  result = [(x+y) for x,y in zip(l1,l2)]

def numpy_arrays():
  result = a1 + a2

# Time test:
%time python_lists()
print('-'*50)
%time numpy_arrays()