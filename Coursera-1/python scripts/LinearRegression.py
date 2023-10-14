import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



X = np.random.rand(100,1)
y = 4 + 5 * X + np.random.randn(100,1)

reg = LinearRegression()
reg.fit(X,y)

x_vals = np.linspace(0,1,100).reshape(-1,1)
y_vals = reg.predict(x_vals)

plt.scatter(X,y)
plt.plot(x_vals, y_vals, color='r')
plt.show()