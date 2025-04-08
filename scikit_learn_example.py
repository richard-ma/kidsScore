import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
# 创建一些数据点
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])
 
# 指定簇的数量
k = 2
 
# 创建 KMeans 实例
kmeans = KMeans(n_clusters=k, random_state=0)
 
# 对数据进行拟合
kmeans.fit(X)
 
# 预测簇标签
labels = kmeans.predict(X)
 
# 获取簇中心点
centroids = kmeans.cluster_centers_
 
# 打印结果
print("Labels:", labels)
print("Centroids:", centroids)
 
# 可视化结果
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.5)  # 绘制中心点
plt.savefig('kmeans_result.png')