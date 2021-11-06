import numpy as np, matplotlib.pyplot as plt
dt = 1
MMarsa = 6.39e23
St_G = 6.674e-11
St_k = 1.38e-23
r0 = 3.3895e6
m0 = 1.16736e-27


dm = m0
P0 = 0.2
g = MMarsa*St_G/(r0**2)
tmp = 350
v0 = np.sqrt(2*St_k*tmp/dm)
xc = St_G*MMarsa*dm/(r0*St_k*tmp)
he = 2.4e5
St_R = 8.314
tkrpk = v0*(1+xc)*np.exp(-xc)/(2*np.sqrt(np.pi))
kwiat = -tkrpk*g*np.exp(-he*dm*g/(St_k*tmp))/(St_R*tmp)
kwiat = g/(2*np.sqrt(np.pi)*St_R*tmp)*np.exp(-he*dm*g/(St_k*tmp))*v0*(1+xc)*np.exp(-xc)
t = np.log(1/2)/kwiat
print(v0)
print(xc)
print(tkrpk)
print(kwiat)
print(t)
"""
y = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0.])
nn = 9
x = np.array(range(nn))+1

for i in range(nn):
    dm = m0*(i+1)
    P0 = 0.2
    g = MMarsa*St_G/(r0**2)
    tmp = 350
    v0 = np.sqrt(2*St_k*tmp/dm)
    xc = St_G*MMarsa*dm/(r0*St_k*tmp)
    he = 2.5e5
    St_R = 8.314
    tkrpk = v0*(1+xc)*np.exp(-xc)/(2*np.sqrt(np.pi))
    kwiat = -tkrpk*g*np.exp(-he*dm*g/(St_k*tmp))/(St_R*tmp)
    t = np.log(1/2)/kwiat
    y[i] = -kwiat
    


fig, ax = plt.subplots()

#ax.set_ylim(0,3.73)
#ax.set_xlim(50/a, 2.5)

ax.plot(x, y, label='P(h)')
ax.grid(which='both')
ax.legend()

ax.set_yscale('log')

ax.set_xlabel('h')
ax.set_ylabel('P')


plt.show()
plt.close(fig)
fig.savefig('podh.pdf', bbox_inches='tight')
"""
