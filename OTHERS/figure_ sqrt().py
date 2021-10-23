import numpy as np
from matplotlib import pyplot as plt
import math

plt.rcParams["figure.dpi"] = 140

fig, ax = plt.subplots()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

origin = [0, 0]

# 45
plt.plot(
    np.linspace(0, 100, 100),
    np.sqrt(np.linspace(0, 100, 100)),
    color="k",
)

ax.set_aspect("auto")
plt.xlim(-0.25, 100)
plt.ylim(0, 100)
plt.yticks(ticks=np.linspace(0, 100, 6))
plt.show()