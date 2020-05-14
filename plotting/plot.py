import matplotlib
# matplotlib.use('Agg')
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
rc('font', **{'family': 'CMU Serif', 'style': 'normal'})
rc('text', usetex=False)
matplotlib.rcParams['text.latex.unicode']=True
fig = plt.figure()
plt.subplot(1, 1, 1)
plt.scatter([1,2,3,4],[5.5,7.6,11.1,6.5])
ax=plt.gca()
ax.annotate('p0', xy=(1.1, 5.6))
rc('font', **{'family': 'CMU Serif', 'style': 'italic', 'weight': 'normal'})
ax=plt.gca()
ax.annotate('p1', xy=(2.1, 7.699999999999999))
plt.savefig('test_colour.png', format='png', transparent=False)
plt.show()