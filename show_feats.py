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

x = plt.imshow(np.array(image_d))   
plt.axis('off')
x.axes.get_xaxis().set_visible(False)
x.axes.get_yaxis().set_visible(False)    
plt.subplots_adjust(wspace=None, hspace=None)
plt.savefig('./featmaps_generated/plt{}_feats.png'.format(1), bbox_inches='tight',pad_inches = 0)  


import matplotlib.pyplot as plt
import numpy as np

# 生成一个随机的灰度图像
gray_image = np.random.random((100, 100))

# 将灰度图转换为红黄热图
heatmap = plt.cm.hot(gray_image)

# 显示热图
plt.imshow(heatmap)
plt.colorbar()
plt.show()