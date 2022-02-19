import matplotlib.pyplot as plt

squares = [x**2 for x in range(1,5)]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
