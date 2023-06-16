# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/16 18:48

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig = plt.figure(figsize=(4, 3), facecolor='none', edgecolor='none')

# 准备数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 25, 40]

# 创建柱状图
ax = sns.barplot(x=categories, y=values)

# 添加数值标签
for i, v in enumerate(values):
    ax.text(i, v + 0.5, str(v), ha='center')

# 添加标题和标签
plt.title('柱状图示例')
plt.xlabel('类别')
plt.ylabel('数值')

# 保存图像
fig.patch.set_alpha(0.0)
plt.savefig('01.png', dpi=200, bbox_inches='tight')

# 显示图形
plt.show()
