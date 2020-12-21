import numpy as np

mu_array = np.array([1, 2, 3, 4, 1408, 1429, 1430, 1432, 1434, 1436, 1441, 1442, 2020, 50, 60, 70, 70, 80, 90, 100])
print(mu_array)

print(mu_array.ndim)

print(mu_array[10])

print(mu_array[5:15])

print(mu_array.dtype)

new_mu_array = mu_array.copy()

print(new_mu_array)

view_mu_array = mu_array.view()

print(view_mu_array)

print(mu_array.shape)

reshape_mu_array = mu_array.reshape(2, 10)
reshape_mu_array = mu_array.reshape()

print(reshape_mu_array)