from PIL import Image
from IPython.display import display
import os
import numpy as np
import torch.nn as nn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as image

# 打开并显示 PNG 图片
image_d = Image.open('./featmaps/1_feats.png')
#display(image)

# 将灰度图转换为红黄热图
heatmap = plt.cm.hot(image_d)

# 显示热图
#plt.imshow(heatmap)
#plt.colorbar()
#plt.show()

x = plt.imshow(image_d, cmap=plt.cm.hot_r)   
plt.axis('off')
x.axes.get_xaxis().set_visible(False)
x.axes.get_yaxis().set_visible(False)    
plt.subplots_adjust(wspace=None, hspace=None)
plt.colorbar()
plt.savefig('./featmaps_generated/plt{}_feats_colormap.png'.format(1), bbox_inches='tight',pad_inches = 0)  