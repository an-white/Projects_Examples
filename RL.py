import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Lineal regresion with machine learning with sklearn ##
# fixing the entry values #
esf = np.array([5, 10, 15, 20, 25, 30, 35, 40])
t = np.array([40, 30, 25, 40, 18, 20, 22, 15])
esf = esf.reshape(8, 1)
t = t.reshape(8, 1)
plt.scatter(t, esf)

from sklearn.model_selection import train_test_split as tts

# Training the model
t_train, t_test, esf_train, esf_test = tts(t, esf, test_size=0.2)

lr = linear_model.LinearRegression()
# making prediction
lr.fit(t_train, esf_train)
y_p = lr.predict(t)

# ploting prediction
plt.scatter(t_test, esf_test)
plt.plot(t, y_p, color="red", linewidth=3)
plt.xlabel("Time")
plt.ylabel("Effort")
plt.show()

a = lr.coef_
b = lr.intercept_

print("Value of coefficient a:", a, "\nValue of coefficient b:", b)
print("Model accuracy:", lr.score(esf_train, t_train))
