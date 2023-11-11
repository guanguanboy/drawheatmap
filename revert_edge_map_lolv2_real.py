from PIL import Image
from IPython.display import display
import os
import numpy as np
import torch.nn as nn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as image
import os

source_dir = '../../Comparision_Results/SMG-LLIE/LOLv2-real/results_edge_generation_LOL_real/edge_output'

save_dir = '../../Comparision_Results/SMG-LLIE/LOLv2-real/results_edge_generation_LOL_real/edge_output_reverted'

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

file_names = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    
    image_path = os.path.join(source_dir, image_name)
    image_d = Image.open(image_path).convert("L")
    save_path = os.path.join(save_dir, image_name)
    plt.imsave(save_path, image_d, cmap='binary')


# 打开并显示 PNG 图片
#image_d = Image.open('./00086.png').convert("L")

#save_path = './00086_reverted.png'
#plt.imsave(save_path, image_d, cmap='binary')
