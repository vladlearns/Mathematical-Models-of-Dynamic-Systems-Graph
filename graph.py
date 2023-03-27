import matplotlib.pyplot as plt


H = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PR_V0 = [264, 254, 244, 221.5, 199, 179, 159, 124, 89, 86.5, 84]
PR_V50 = [191.5, 189, 186.5, 171.5, 156.5, 144, 131.5, 104, 76.5, 72.75, 69]


plt.plot(H, PR_V50, label="V = 50 м/с")

plt.xlabel("H (км)")
plt.ylabel("PR")
plt.title("Висотно-швидкісні характеристики двигуна PR=f(H)")

plt.legend()


plt.show()
