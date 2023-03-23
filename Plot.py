import matplotlib.pyplot as plt

def show(x, y):
    plt.figure(figsize=(8,6))
    plt.plot(x, y, color='blue', linewidth=3)
    plt.title("Heat Transport", fontsize=20)
    plt.xlabel("x", fontsize=15)
    plt.ylabel("y", fontsize=15)
    plt.grid(True)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.show()