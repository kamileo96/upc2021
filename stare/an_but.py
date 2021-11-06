import numpy as np, scipy.optimize, matplotlib.pyplot as plt

x = np.array([230, 380, 530, 680, 830, 980, 1130, 1280, 1430, 1580])

y = np.array([313, 236, 204, 186, 162, 152, 146, 140, 136, 122])

dy = 5
dys = np.array([5,5,5,5,5,5,5,5,5,5])
v0 = 150

def fnc(v, alpha, f0):
    return f0*(v/v0)**alpha

p0 = [-0.5, 370]

popt, pcov = scipy.optimize.curve_fit(fnc, x, y, p0=p0, sigma=dys)
al = popt[0]
d_array = np.sqrt(np.diag(pcov))
#alpha
print("Alpha = "+str(popt[0])+"±"+str(d_array[0]))
#f0
print("f0 = "+str(popt[1])+"±"+str(d_array[1]))

#test chi^2
R = 0
i = 0
for v in x:
    R += ((y[i]-fnc(v,*popt))/dy)**2
    i += 1
print("R equals: "+str(R))

basex = np.array(range(x[-1]+100))
fit = np.array([fnc(n,*popt) for n in basex])

fig, ax = plt.subplots()

#ax.set_xscale('log')
#ax.set_yscale('log')

ax.set_ylim(100,np.amax(y)+25)
#ax.set_ylim(np.amin(y)-10,np.amax(y)+10)

#ax.set_xlim(x[0]-10, basex[-1])
ax.set_xlim(0, basex[-1])

ax.errorbar(x,y,yerr=dy,label='Zmierzone wartości f',fmt='.')
ax.plot(basex, fit, label='Dopasowana funkcja')
ax.grid(which='both')
ax.legend()

#ax.set_title('Zależność f(V) w skali liniowej')
#ax.set_title('Zależność f(V) w skali logarytmicznej')

ax.set_xlabel('V[ml]')
ax.set_ylabel('f[Hz]')

plt.show()
plt.close(fig)