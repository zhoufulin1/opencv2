import cv2 
import numpy as np
# 交互式前景提取
img = cv2.imread('hehua.jpg')
cv2.imshow('img', img)

# 定义与图像同形状的掩膜
mask =np.zeros(img.shape[:2], np.uint8) 
bg = np.zeros((1, 65), np.float64) # 背景模型的临时数组
fg = np.zeros((1, 65), np.float64) # 前景模型的临时数组

rect = (50, 50, 400, 500) # 用矩形框标注前景区域 (x,y,w,h)
# 第一次提取掩膜
cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT) # 5为迭代次数
# 读取已经标注的掩膜图像
img_mask = cv2.imread('hehua2.jpg')
# 转化为灰度图
mask_gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
mask[mask_gray == 0] = 0 # 背景
mask[mask_gray == 255] = 1 # 前景
# 第二次提取掩膜
cv2.grabCut(img, mask, None, bg, fg, 5, cv2.GC_INIT_WITH_MASK)
mask_gray = np.where((mask==2)|(mask==0), 0, 1).astype('uint8') # 0和2做背景

# 使用蒙板来获取前景区域
imgs= img*mask_gray[:,:,np.newaxis]

cv2.imshow('imgss', imgs)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


