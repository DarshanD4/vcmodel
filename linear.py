import numpy as np
c = 16
m = 16
x = [x for x in range(1, 11)]  # Adjusted range to start from 1
for i in range(len(x)):
    result = c * x[i]
    print(f"{c} * {x[i]} = {result}")
