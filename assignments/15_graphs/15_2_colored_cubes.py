import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(8,5))
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=1)
plt.title("Colored Cubes")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.colorbar()
plt.show()
