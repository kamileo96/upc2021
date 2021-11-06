import numpy as np, matplotlib.pyplot as plt
dt = 1
MMarsa = 6.39e23
St_G = 6.674e-11
St_k = 1.38e-23
r0 = 3.3895e6
dm = 2.988e-26
P0 = 0.2
dh = 100
n_h = 1000
hs = np.array([dh*i for i in range(n_h)])
g = MMarsa*St_G/(r0**2)
gs = MMarsa*St_G/((r0+hs)**2)
tmp = 400
tmps = np.array([400*i for i in range(n_h)])
Ps = P0*np.exp(-hs/(St_k*tmp)*dm*gs)

fig, ax = plt.subplots()

#ax.set_ylim(0,3.73)
#ax.set_xlim(50/a, 2.5)

ax.plot(hs, Ps, label='P(h)')
ax.grid(which='both')
ax.legend()

ax.set_xlabel('h')
ax.set_ylabel('P')


plt.show()
plt.close(fig)
fig.savefig('podh.pdf', bbox_inches='tight')