import numpy as np
import matplotlib.pyplot as pl

x = np.linspace(0,10,20)
y1 = x*x + 2*x
y2 = np.sqrt(x)

pl.figure()

pl.subplot(1,2,1)
pl.plot(x,y1,'g--', label='$y = x^2+2x$')
pl.legend(loc=0)

pl.subplot(1,2,2)
pl.plot(x,y2, 'r*-', label='$y = \sqrt{x}$')
pl.legend(loc=2)
pl.show()