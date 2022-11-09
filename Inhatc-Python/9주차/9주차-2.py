import numpy as np
var = np.array(np.arange(10)**3)
print(var)
print(var[2])
print(var[2:5])
print(var[2:-1])
print(var[2:])

var[:6:2] = 1000
print(var)
print(var[::-1])

var = np.array(var.reshape(2, 5))
print(var)
# res = np.sum(var, axis=1)
