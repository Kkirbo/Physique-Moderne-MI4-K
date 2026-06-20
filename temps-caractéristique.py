import numpy as np
import matplotlib.pyplot as plt
hbar = 1.055e-34
m = 9.11e-31
eV = 1.602e-19
E = 6.1 * eV
V0 = 6.0 * eV
a = np.linspace(0.0, 5e-9, 200)

v_g = np.sqrt(2 * E / m)

tau_classique = a / v_g

kappa = np.sqrt(2 * m * (V0 - E)) / hbar
tau_max = 2.5e-15

tau_q = tau_max * (1 - np.exp(-2 * kappa * a))


plt.figure(figsize=(8, 5))

plt.plot(a * 1e9, tau_classique * 1e15,'r--', label="Particule libre (classique)")

plt.plot(a * 1e9, tau_q * 1e15,'b', linewidth=2,label="Particule subissant l'effet tunnel en fonction de l'épaisseur de la barrière ")

plt.xlabel("Largeur de la barrière a (nm)")
plt.ylabel("Temps de traversée (fs)")
plt.title("Effet Hartman : comparaison classique vs quantique")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()