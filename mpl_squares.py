import matplotlib.pyplot as plt

value = range(1, 6)
squares = [x**2 for x in value]
fig, ax = plt.subplots()
ax.plot(value, squares, linewidth=1)

# Назначение заголовка и меток осей
ax.set_title("Квадраты", fontsize=10)
ax.set_xlabel("Значения", fontsize=10)
ax.set_ylabel("Квадраты значений", fontsize=10)

ax.tick_params(axis='both', labelsize=10)

plt.show()
