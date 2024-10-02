import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.rcParams['font.sans-serif'] = ['SimSun']  # 用黑体显示中文
plt.rcParams['font.family']='Times New Roman ,SimSun '# 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['font.size'] = 18

from PIL import Image

# 设置题目与坐标轴名称  
font2 = {'family' : 'SimSun',
'weight' : 'normal',
'size'   : 15,
}

def calculate_brightness_histogram(image_path):
    # 读取图像
    image = Image.open(image_path)
    # 将图像转换为灰度图
    gray_image = image.convert('L')
    # 将图像转换为 NumPy 数组
    gray_array = np.array(gray_image)
    # 计算直方图
    hist, _ = np.histogram(gray_array, bins=256, range=(0, 255), density=True)
    return hist


def plot_histogram(hist, label, pixel_range=None):
    if pixel_range:
        plt.plot(range(pixel_range[0], pixel_range[1] + 1), hist[pixel_range[0]:pixel_range[1] + 1], label=label)
    else:
        plt.plot(hist, label=label)  # 使用默认的彩色线条绘制直方图
    plt.xlabel('像素值')
    plt.ylabel('归一化频率')
    # plt.title('Brightness Histogram')
    plt.legend(fontsize=14)

def plot_histogram_right(hist, label, pixel_range=None):
    if pixel_range:
        plt.plot(range(pixel_range[0], pixel_range[1] + 1), hist[pixel_range[0]:pixel_range[1] + 1], label=label)
    else:
        plt.plot(hist, label=label)  # 使用默认的彩色线条绘制直方图
    plt.xlabel('像素值')
    # plt.title('Brightness Histogram')
    #plt.legend(fontsize=12)


def save_histogram_as_txt(hist, save_path):
    np.savetxt(save_path, hist)


def main(folder_paths, labels, save_path):
    plt.figure(figsize=(12, 6))

    for folder_path, label in zip(folder_paths, labels):
        # 初始化亮度直方图
        brightness_histogram = np.zeros((256,))

        # 遍历文件夹下所有图片文件
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                # 获取图像路径
                image_path = os.path.join(folder_path, filename)
                # 计算图像亮度直方图
                hist = calculate_brightness_histogram(image_path)
                # 累加到总的亮度直方图中
                brightness_histogram += hist

        # 归一化总的亮度直方图
        brightness_histogram /= len(os.listdir(folder_path))

        # 保存亮度直方图到txt文件
        save_histogram_as_txt(brightness_histogram, os.path.join(folder_path, "brightness_histogram.txt"))

        # 绘制亮度直方图
        plt.subplot(1, 2, 1)  # 创建一个1x2的子图，当前为第1个子图
        plot_histogram(brightness_histogram, label=label)

        # 绘制特定像素值范围的亮度直方图
        plt.subplot(1, 2, 2)  # 当前为第2个子图
        plot_histogram_right(brightness_histogram, label=label, pixel_range=(200, 255))
        plt.xlim(200, 255)

    plt.savefig(save_path, facecolor='white')  # 设置背景为白色
    plt.show()


if __name__ == "__main__":
    folder_paths = [
        "E:/科研项目/SAM低光增强/TMM_Response/Datasets/LOLv1/Test/input",
        "E:/科研项目/SAM低光增强/TMM_Response/原始数据集/LOL-v2/Synthetic/Test/Low",
        "E:/科研项目/SAM低光增强/TMM_Response/Datasets/LOL-v2/Real_captured/Test/Low",
        "E:/科研项目/SAM低光增强/TMM_Response/Datasets/SID_rgb/SID/test/low"
    ]
    labels = ['LOL-v1数据集', 'LOL-v2-syn数据集', 'LOL-v2-real数据集', 'SID(Snoy)数据集']
    save_path = "histogram_plot.png"
    main(folder_paths, labels, save_path)
