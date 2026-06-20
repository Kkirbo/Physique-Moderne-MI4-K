from numpy import pi, exp, real, imag, linspace
import matplotlib.pyplot as plt

amp = 1

k = 2*pi / 1
omega = 2*pi / 2
t = 0

def PlaneWave(amp, k, omega, x, t):
    return amp * exp(1j * (k*x - omega*t))

x = linspace(-2, 2, 100)

psi = PlaneWave(amp, k, omega, x, t)

fig, ax = plt.subplots()

ax.plot(x, real(psi), label="Re(psi)")
ax.plot(x, imag(psi), label="Im(psi)")

plt.show()