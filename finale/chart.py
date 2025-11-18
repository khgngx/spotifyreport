import matplotlib.pyplot as plt
import numpy as np

labels = ['Chi phí thấp', 'Yêu thích thể thao', 'Không gian hạn chế', 'Thích combo', 'Sử dụng ngắn hạn']
num_vars = len(labels)

# Giá trị từng nhóm
sinhvien = [5, 4, 5, 3, 4]
vanphong = [3, 3, 2, 4, 5]
theomua = [4, 4, 3, 4, 5]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
sinhvien += sinhvien[:1]
vanphong += vanphong[:1]
theomua += theomua[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

ax.plot(angles, sinhvien, label='Sinh viên')
ax.plot(angles, vanphong, label='NV văn phòng')
ax.plot(angles, theomua, label='Nhóm theo mùa')

ax.fill(angles, sinhvien, alpha=0.25)
ax.fill(angles, vanphong, alpha=0.25)
ax.fill(angles, theomua, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_title('So sánh nhu cầu theo nhóm khách hàng')
ax.legend(loc='upper right')
plt.show()
