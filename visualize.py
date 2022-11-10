import numpy as np
from matplotlib import pyplot as plt


# 可视化画出哈密顿回路和能量趋势
def draw_H_and_E(citys, names, H_path, energys):
   # fig = plt.figure(figsize=(80, 40))
    # 绘制哈密顿回路

    img = plt.imread("map.png")
    fig, ax1 = plt.subplots( figsize=(80, 40))
    plt.title('中国 一点不能少！', fontsize=25)
    plt.xlim(74, 136)
    plt.ylim(17.5, 53)
    ax1.imshow(img,extent=[73,135,19,56])

    for (from_, to_) in H_path:
        p1 = plt.Circle(citys[from_], 0.3, color='blue')
        p2 = plt.Circle(citys[to_], 0.3, color='blue')

        ax1.add_patch(p1)
        ax1.add_patch(p2)
        ax1.plot((citys[from_][0], citys[to_][0]), (citys[from_][1], citys[to_][1]), color='gray')
        plt.text(citys[from_][0], citys[from_][1], list(names[from_]))


        #ax1.annotate(text='香港', xy=citys[to_], xytext=(-8, -4), textcoords='offset points', fontsize=20)
    ax1.axis('equal')
    ax1.grid()
    # 绘制能量趋势图
    fig1,ax2 = plt.subplots( figsize=(80, 40))
    ax2.plot(np.arange(0, len(energys), 1), energys, color='black',linewidth=0.2)
    plt.show()
