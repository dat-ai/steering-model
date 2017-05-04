'''
Usage:

This script is used to generate pickle file from Udacity car simulator.
It will allow me to reuse dataset easier.

Change LOG_PATH and IMG_PATH to generate new file
'''
from FLAGS import *
from utils.DataSet import DataSet

import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grid
plt.interactive(False)

LOG_PATH = './data/driving_log.csv'
IMG_PATH = './data/IMG/'
FILE_NAME = './data/4_good_laps.p'

data = DataSet(LOG_PATH, IMG_PATH, sequence=TIME_STEPS)

features, labels = data.build_train_data()
pickle.dump({'features': features, 'labels': labels}, open(FILE_NAME, 'wb'), protocol=2)

fig = plt.figure(figsize=(50, 50))
idx = 6
gs = grid.GridSpec(idx, idx)

# VISUALIZE FRAME + STEER VALUES for i in range():
for i in range(idx):
    for j in range(idx):
        r = np.random.choice(len(features))
        img = features[r]
        ax = fig.add_subplot(gs[i*idx + j])
        title = "ID: {} Steer {:5.3f}  Speed {:5.3f} ".format(r, labels[r][0], labels[r][1])
        ax.set_title(title)
        ax.axis('off')
        ax.imshow(img)
gs.tight_layout(fig)
plt.show()