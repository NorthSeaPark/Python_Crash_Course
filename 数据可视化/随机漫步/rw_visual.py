import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 不断地模拟随机漫步
while True:
    # 创建一个Random Walk实例
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    # 随机漫步从浅色变成深色
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

