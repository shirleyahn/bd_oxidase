import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab
from matplotlib.ticker import AutoMinorLocator
params = {'font.family': 'sans-serif',
          'font.sans-serif': 'Helvetica',
         'legend.fontsize': '36',
         'figure.figsize': (24,12),
         'axes.labelsize': '36',
         'axes.titlesize': '36',
         'xtick.labelsize': '36',
         'ytick.labelsize': '36'}
pylab.rcParams.update(params)

dist = np.loadtxt('POVME_run/example_volumes.tabbed.txt')
dist = dist[:, 1]

fig = plt.figure(figsize=(24,12))
ax = fig.add_subplot(111)
numBins = 50
print(np.max(dist), np.min(dist), np.mean(dist))
n, bins, patches = plt.hist(dist, numBins, label='Mtb (with disulfide bond) MQ9 binding site', color='dodgerblue', alpha=0.8, rwidth=0.9, density=False, range=(2900.0, 9300.0))
print(n, bins, patches)
ax.set_xlabel('Volume ($\AA^3$)',labelpad=20)
ax.set_ylabel('# of Structures',labelpad=20)
plt.legend(loc=0)
fig.savefig('Figure.png', bbox_inches='tight')

