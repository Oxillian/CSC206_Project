import numpy as np
# Online Python - IDE, Editor, Compiler, Interpreter

base = 10
step = 5
numcells = 6
upper_limit = base + (step * numcells)
axes_2d = np.arange(base, upper_limit, step).reshape([2,3])
print(axes_2d)
