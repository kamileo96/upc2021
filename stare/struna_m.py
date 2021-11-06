import numpy as np, matplotlib.pyplot as plt, scipy.optimize



ms = [0.58656,
1.08656,
1.58656,
2.08656,
2.58656,
3.08656,
3.58656,
4.08656,
4.58656,
5.08656,
5.58656,
]
xs = np.sqrt(np.array(ms))
ys = [62.1,
85.0,
101.7,
117.5,
130.9,
143.2,
154.6,
165.9,
175.6,
184.9,
193.7]

yerr = 0.1

n = len(ys)




def liniowa(x,a,):
    return a*x

p0 = [193]
popt, pcov = scipy.optimize.curve_fit(liniowa, xs,ys,p0=p0)


a = popt[0]
da = np.sqrt(np.diag(pcov))[0]
print(a)
print(da)

basex = np.array(range(int(xs[-1]*100+50)))/100
fit = np.array([liniowa(z,*popt) for z in basex])

fig, ax = plt.subplots()

ax.errorbar(xs,ys,fmt='.',label='Wyznaczone punkty',yerr=yerr)
ax.set_ylim(50,250)
ax.set_xlim(50/a, 2.5)

ax.plot(basex, fit, label='Dopasowana prosta')
ax.grid(which='both')
ax.legend()

ax.set_xlabel('√m [√kg]')
ax.set_ylabel('$ν$ [Hz]')


plt.show()
plt.close(fig)
fig.savefig('nachylenie_m.pdf', bbox_inches='tight')

