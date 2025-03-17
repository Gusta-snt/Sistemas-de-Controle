import control
import sympy as sp

G = control.tf([1000, 8000], [1, 16, 63])
H = control.tf([1], [1])


FTMF = control.feedback(G, H, -1)
polos = control.poles(FTMF)

FTMA = G

polos = control.poles(FTMA)

print(polos)
