import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 4, 6, 5, 3, 1.5, 2.5, 3.5])
fx = np.array(
    [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630]
)
"""
x=x.reshape(8,1)
x=fx.reshape(8,1)
"""
DB = pd.DataFrame({"x": x, "fx1": fx})
fn = fx.copy()
n = len(x)
for j in range(2, n + 1):
    temp = []
    for i in range(n - 1, j - 2, -1):
        temp.insert(0, (fn[i] - fn[i - 1]) / (x[i] - x[i - j + 1]))

    fn = temp.copy()
    for k in range(n - len(fn)):
        fn.insert(0, 0)
    col = "fx" + str(j)
    add = pd.DataFrame({col: fn})
    DB["" + col + ""] = add["" + col + ""]

val = 2

fxval = fx[0]

for i in range(2, n + 1):
    bn = DB["fx" + str(i) + ""][i - 1]
    for j in range(i - 1):
        bn = bn * (val - x[j])
    fxval = fxval + bn

prod = 1
for i in range(n - 1):
    prod = prod * (val - x[i])
    print(i, prod)
error = prod * DB["fx" + str(n) + ""][n - 1]

# initial Values
plt.scatter(x, fx, label="initial values")
# calculated value
plt.scatter(val, fxval, color="red", label="calculted value")
plt.legend()
plt.show()
print(error)
