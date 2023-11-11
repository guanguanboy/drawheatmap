import os
import shutil

folder_path = "../../Comparision_Results/Ours/SID/SID_SAM/Enhancement_SGIENetDyncEdge_SID_w_sam/net_g_latest"  # 替换为当前文件夹路径

# 获取当前文件夹下的所有子文件夹
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

save_folder_path = "../../Comparision_Results/Ours/SID/SID_SAM/Enhancement_SGIENetDyncEdge_SID_w_sam/output"
if not os.path.exists(save_folder_path):
    os.mkdir(save_folder_path)
    
count = 0
# 遍历子文件夹并复制文件
for index, subfolder in enumerate(subfolders, 1):
    files = os.listdir(subfolder)
    for file in files:
        source_path = os.path.join(subfolder, file)
        # 生成六位数字编号
        number_str = str(count).zfill(6)
        count = count + 1
        destination_path = os.path.join(save_folder_path, number_str+'.png')
        shutil.copy(source_path, destination_path)