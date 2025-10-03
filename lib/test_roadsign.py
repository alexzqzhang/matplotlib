import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.text(0.5,0.5, "Road Sign", bbox=dict(boxstyle= "RightRoadsign", pad = 0.3, facecolor="orange"),
        ha="center", va="center", fontsize=14)

plt.show()

