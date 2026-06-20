import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d
hbar = 1.054571817e-34
m = 9.11e-31
# Grille spatiale 
x_min, x_max = -20e-9, 20e-9 
nx = 500
x = np.linspace(x_min, x_max, nx)
dx = x[1] - x[0]


t_max = 50e-15 
dt = 2e-19  
nt = int(t_max / dt)
times = np.linspace(0, t_max, nt)

V0 = 5 * 1.6e-19 #5eV

# Paramètres du paquet d'onde initial (Reculé à -12 nm)
x0_paquet = -12e-9
largeur_paquet = 1e-9  
gamma = largeur_paquet**2 / 4
k0 = 5e9
N = (1 / (2 * np.pi * gamma))**0.25

def simuler_effet_tunnel(a_barrier, animer=False):
    x1 = 0.0
    x2 = a_barrier
    
    V = np.zeros(nx)
    if a_barrier > 0:
        V[(x >= x1) & (x <= x2)] = V0
    
    # Initialisation de la fonction d'onde
    Psi = np.zeros((nt, nx), dtype=complex)
    Psi[0] = N * np.exp(-((x - x0_paquet)**2) / (4 * gamma)) * np.exp(1j * k0 * x)
    
    coeff = 1j * hbar / (2 * m * dx**2)
    pot_coeff = -1j * V / hbar
    for n in range(nt - 1):
        lap = np.zeros(nx, dtype=complex)
        lap[1:-1] = Psi[n, 2:] - 2 * Psi[n, 1:-1] + Psi[n, :-2]
        Psi[n + 1] = Psi[n] + dt * (coeff * lap + pot_coeff * Psi[n])           
    density = np.abs(Psi)**2
    if animer:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(x_min * 1e9, x_max * 1e9)
        hauteur_max = np.max(density[0])
        ax.set_ylim(-0.05 * hauteur_max, hauteur_max * 1.1)
        if a_barrier > 0:
            ax.fill_between(x * 1e9, 0, hauteur_max * 0.5, where=(x >= x1) & (x <= x2),
                            color="red", alpha=0.3, label=f"Barrière ({a_barrier*1e9:.2f} nm)")
        
        line, = ax.plot([], [], color="#1a00aa", lw=2, label=r"Densité $|\Psi(x, t)|^2$")
        ax.set_xlabel("Position x (nm)")
        ax.set_ylabel("Densité de probabilité")
        ax.legend(loc="upper left")
        ax.grid(True, linestyle="--", alpha=0.5)
        pas_affichage = 400
        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            idx = i * pas_affichage
            if idx < nt:
                line.set_data(x * 1e9, density[idx])
            return line,
        ani = FuncAnimation(fig, animate, init_func=init, frames=nt // pas_affichage, interval=20, blit=False)
        plt.show() 
b = simuler_effet_tunnel(a_barrier=0.1e-9, animer=True)