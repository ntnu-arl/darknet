import numpy  as np
import matplotlib.pyplot as plt
with open('loss.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]
    for i in range (len(x)):
        length = len(x[i])
        x[i] = float(x[i][0:length-1])

        y[i] = float(y[i])

    print(y)


plt.plot(x, y,'b--')
plt.ylim([0,5])
plt.savefig('loss.png')
plt.show()
