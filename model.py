import numpy as np, matplotlib.pyplot as plt
dt = 0.01
MMarsa = 6.39e23
St_G = 6.674e-11
St_k = 1.38e-23
r0 = 3.3895e6
m = 1.16736e-27

P0 = 0.2
g = MMarsa*St_G/(r0**2)
T = 350
v0 = np.sqrt(2*St_k*T/m)
xc = St_G*MMarsa*m/(r0*St_k*T)
he = 2.4e5
St_R = 8.314

A = g*np.exp(-he*m*g/(St_k*T))*v0*(1+xc)*np.exp(-xc)/(2*St_R*T*np.sqrt(np.pi))

print(v0*(1+xc)*np.exp(-xc)/(2*np.sqrt(np.pi)))
print(g*np.exp(-he*m*g/(St_k*T))/(St_R*T))
print((v0*(1+xc)*np.exp(-xc)/(2*np.sqrt(np.pi)))*(g*np.exp(-he*m*g/(St_k*T))/(St_R*T)))
"""
print(np.exp(-he*m*g/(St_k*T)))
print(g*np.exp(-xc)*(1+xc)/(2*np.sqrt(np.pi)))
print(v0/St_R)
print(A)
"""
loss = 0.01

pW = 0.2
pH = 0
pO = 0

pWs = np.array([pW])
pHs = np.array([pH])
pOs = np.array([pO])

i = 0
iis = np.array([i])
while(i<1000):
    
    dpH = dt*pW/9*loss
    pH += dpH
    pO += dpH*8
    pW -= dpH*9
    
    dpH = dt*pH*A
    pH -= dpH
    pO -= dpH*8  

    pWs = np.append(pWs, pW)
    pHs = np.append(pHs, pH)
    pOs = np.append(pOs, pO)

    i += 1
    iis = np.append(iis, i)


fig, ax = plt.subplots()

#ax.set_ylim(0,3.73)
#ax.set_xlim(50/a, 2.5)
"""
ax.plot(iis, pWs, label='Pw')
ax.plot(iis, pOs+pWs, label='Pw')
ax.plot(iis, pOs+pWs+pHs, label='Pw')
"""
ax.fill_between(iis, pWs, label='H2O')
ax.fill_between(iis, pOs+pWs, pWs, label='O')
ax.fill_between(iis, pHs+pWs+pOs, pOs+pWs, label='H')

ax.grid(which='both')
ax.legend()

ax.set_xlabel('t')
ax.set_ylabel('P')


plt.show()
plt.close(fig)
fig.savefig('podh2.pdf', bbox_inches='tight')