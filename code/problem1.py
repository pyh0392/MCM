import matplotlib.pyplot as plt
import numpy as np
import os

# --- 新增代码：确保results文件夹存在 ---
# 获取当前脚本文件所在的目录 (D:\MCM\code)
current_dir = os.path.dirname(__file__)
# 构建上一级目录 (D:\MCM)
parent_dir = os.path.dirname(current_dir)
# 构建results文件夹的完整路径 (D:\MCM\results)
results_dir = os.path.join(parent_dir, 'results')

# 如果results文件夹不存在，则创建它
os.makedirs(results_dir, exist_ok=True)
# --- 修改结束 ---

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一个常用的支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 1. 准备二维数据
# 创建一个10x10的随机数据矩阵作为示例
data = np.random.rand(10, 10) * 100

# 2. 创建图表
fig, ax = plt.subplots(figsize=(8, 6))

# 3. 绘制热力图
# cmap: 颜色映射方案, e.g., 'viridis', 'hot', 'coolwarm', etc.
heatmap = ax.imshow(data, cmap='viridis')

# 4. 添加颜色条
# 颜色条会显示数据值与颜色的对应关系
cbar = fig.colorbar(heatmap)
cbar.set_label('数值', rotation=-90, va="bottom")

# 5. 添加修饰元素
ax.set_title("热力图示例", fontsize=16)
ax.set_xlabel("X轴标签", fontsize=12)
ax.set_ylabel("Y轴标签", fontsize=12)

# 可选：设置刻度标签
# ax.set_xticks(np.arange(data.shape[1]))
# ax.set_yticks(np.arange(data.shape[0]))
# ax.set_xticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# ax.set_yticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# 可选：旋转X轴的刻度标签，以防重叠
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#          rotation_mode="anchor")

# 6. 保存图表到文件
# 构建完整的保存路径
output_path = os.path.join(results_dir, 'heatmap.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# 7. 显示图表
plt.show()