import tensorflow as tf
import random
import numpy as np

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn import cluster




'''用tf.data.Dataset.from_tensor_slices只會將第一層的嵌套結構變成可迭代資料結構'''
array = np.random.random([3,3])
ds = tf.data.Dataset.from_tensor_slices(array) #batch=3
array2 = np.arange(1,10)
ds = tf.data.Dataset.from_tensor_slices(array2) #batch=10

for i in iter(ds):
    print(i)


dataset = tf.data.Dataset.range(20)
dataset = dataset.batch(3)
dataset = dataset.batch(2)
list(dataset.as_numpy_iterator())

array2 = np.arange(1,10)
array2[2]

batch_size = 1
num_classes = 1000
array3 = tf.zeros((batch_size,num_classes))
# 從每個batch_size取出1個元素的index
array3 = tf.random.categorical(array3,1) # shape = (1,1)
gen_sparse_class = tf.squeeze(array3)

assert len(array3.get_shape()) == 2
gen_class_ints = tf.squeeze(array3,axis=0)
# gen_class_ints = tf.squeeze(gen_class_ints, axis=0)
assert len(gen_class_ints.get_shape()) == 1
gen_class_vector = tf.one_hot(gen_class_ints, num_classes)
gen_class_vector.shape
assert len(gen_class_vector.get_shape()) == 2
assert gen_class_vector.dtype == tf.float32


# assert宣告變數在程式某一段必須為某值
a = 0
assert a == 1
print(1)
assert a == 0
print(0)

# 實作k-means
try:  # SciPy >= 0.16 have face in misc
    from scipy.misc import face
    face = face(gray=True)
except ImportError:
    face = sp.face(gray=True) # face是一張圖片，大小為768*1024

n_clusters = 5
np.random.seed(0)

X = face.reshape((-1,1)) # 拉成一維向量 (n_sample, n_feature) array
k_means = cluster.KMeans(n_clusters=n_clusters,n_init=4) # K_means分類，num_cluster=5
k_means.fit(X)
values = k_means.cluster_centers_.squeeze() # 使用不同 centroid seeds 運行 k-means 算法的時間
labels = k_means.labels_


face_compressed = np.choose(labels,values) #labels範圍0~4，長度768*1024，values代表五個k_keans值
face_compressed.shape = face.shape

v_min = face.min()
v_max = face.max()

plt.figure(1,figsize=(3,2.2))
plt.imshow(face,cmap=plt.gray()) #原始影像

plt.figure(1,figsize=(3,2.2))
plt.imshow(face_compressed.reshape(768,1024),cmap=plt.gray()) #壓縮後影像

regular_values = np.linspace(0,256,n_clusters+1)
# 在regular_values(升冪)插入數組face，返回對應位置
regular_labels = np.searchsorted(regular_values, face) - 1
regular_values = 0.5*(regular_values[1:]+regular_values[:-1]) #mean
regular_face = np.choose(regular_labels.ravel(),regular_values,mode='clip')
regular_face.shape = face.shape
plt.figure(1,figsize=(3,2.2))
plt.imshow(regular_face,cmap=plt.gray())

plt.figure(4, figsize=(3,2.2))
plt.clf() # 清除當前圖形
plt.axes([.01,.01,.98,.98]) # 創建軸(axes)，分別為左、底、寬、高
plt.hist(X, bins=256, color='.5', edgecolor='.5')
plt.yticks()
plt.xticks(regular_values)
values = np.sort(values)
for center_1,center_2 in zip(values[:-1],values[1:]):
    plt.axvline(.5*(center_1+center_2),color='b') # 繪製垂直線
for center_1,center_2 in zip(regular_values[:-1],regular_values[1:]):
    plt.axvline(.5*(center_1+center_2),color='b',linestyle='--')

plt.show()

'''============================================================================'''
print('x'*50)

import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img_path = r'D:\new_data_of_ML\testesttest\img1.png'
img = Image.open(img_path,'r')

img_shape = img.shape
img = np.array(img)
img_1 = img[:,:,0]
img_2 = img[:,:,1]
img_3 = img[:,:,2]
img_4 = img[:,:,3]
imgs = [img_1,img_2,img_3,img_4]

fig,ax = plt.subplots(4,1) #同時顯示4張圖片
ax[0].imshow(img_1)
ax[1].imshow(img_2)
ax[2].imshow(img_3)
ax[3].imshow(img_4) # 這個是空白圖層


