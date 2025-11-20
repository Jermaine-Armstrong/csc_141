import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(6,4))
plt.scatter(x_values, y_values)
plt.title("First Five Cubes")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(8,5))
plt.scatter(x_values, y_values, s=1)
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube")
plt.show()
