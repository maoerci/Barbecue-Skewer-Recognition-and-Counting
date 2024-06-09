import cv2
import numpy as np

# 读取图像
img = cv2.imread('bbq.jpg')
if img is None:
    print("Could not open or find the image!")
    exit()

# 将图像转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 对图像进行高斯模糊以去除噪声
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 使用Hough圆变换进行圆形检测
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                           param1=50, param2=30, minRadius=5, maxRadius=15)

# 确保至少检测到一个圆
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # 计数圆的数量
    numSkewers = len(circles)
    print(f"Number of skewers: {numSkewers}")

    # 在图像上绘制检测到的圆
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
else:
    print("No skewers detected.")

# 显示结果图像
cv2.imshow("Detected Skewers", img)
cv2.waitKey(0)
cv2.destroyAllWindows()