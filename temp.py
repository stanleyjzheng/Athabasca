# Stanley Zheng - PCA for Codefy

import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sklearn.decomposition
import pandas as pd
import matplotlib.cm as cm

data = tf.keras.datasets.mnist.load_data()

data = np.asarray(data)

x = data[0][0]
y = data[0][1]

x = x.reshape(-1, 784)

comp = sklearn.decomposition.PCA(n_components=2)
comp = comp.fit_transform(x)

comp = pd.DataFrame(data = comp, columns = ['principal component 1', 'principal component 2'])
y = pd.DataFrame(data=y, columns = ['target'])
comp = pd.concat([comp, y], axis = 1)

fig = plt.figure(figsize = (6, 4))

ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA for MNIST', fontsize = 20)

targets = list(range(0, 10))
colors = cm.rainbow(np.linspace(0, 1, 10))

for target, color in zip(targets,colors):
    idx = comp['target'] == target
    ax.scatter(comp.loc[idx, 'principal component 1'], comp.loc[idx, 'principal component 2'], c = color, s = 50)

ax.legend(targets)

plt.show()