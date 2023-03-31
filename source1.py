import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mohr_circle3d import plot_mohr3d
import numpy as np
from scipy.optimize import least_squares
from strain_gauge import strain_compnents

# URL figma: https://www.figma.com/file/zOSuTfi1Pf2l7rV5Bk04Et/Untitled?node-id=0-1&t=A059ape0zbHBo8oi-0
# Token figma: figd_oN7HbUvmsw2XHDzfjYYRioKOpwN3I9nNJlMwU4fy
# Calculate strain in strain gauge rosette, stress tensor, eigenvalues and eigenvectors

# # Hằng số vật liệu
# E = 200E9  # Module đàn hồi
# v = 0.3  # Hệ số Poisson

# # Các giá trị đo được từ hệ strain gauge
# ea = 0.01
# eb = 0.02
# ec = 0.04
# theta_a = 30
# theta_b = 90
# theta_c = 150

# Chỉnh in ra 4 chữ số sau dấu phẩy
np.set_printoptions(precision=4, suppress=True)

def source1_calc(ea, eb, ec, theta_a, theta_b, theta_c, E, v):
    # Đổi đơn vị độ sang radian
    theta_a = np.radians(theta_a)
    theta_b = np.radians(theta_b)
    theta_c = np.radians(theta_c)

    # Tính các giá trị biến dạng trong hệ trục x-y
    x0 = [1, 1, 1]

    res_lsq = least_squares(strain_compnents, x0, args=([theta_a, theta_b, theta_c], [ea, eb, ec]))

    ex, ey, e_xy = res_lsq.x
    gamma_xy = 2*e_xy

    # Tính các giá trị của tensor ứng suất
    o11 = E / (1 - v ** 2) * (ex + v * ey)
    o22 = E / (1 - v ** 2) * (ey + v * ex)
    t12 = E / (1 + v) * gamma_xy
    t21 = t12
    oij = np.array([[o11, t12, 0], [t21, o22, 0], [0, 0, 0]])

    # Tìm các ứng suất chính
    eig_vals, eig_vecs = np.linalg.eig(oij)
    o1, o2, o3 = eig_vals

    # Các phương chính ứng suất
    p1, p2, p3 = eig_vecs[:, 0], eig_vecs[:, 1], eig_vecs[:, 2]
    p1, p2, p3 = np.round(p1, 4), np.round(p2, 4), np.round(p3, 4)
    
    return ex, ey, gamma_xy, oij, o1, o2, o3, p1, p2, p3

# In kết quả
# print('a. Các giá trị biến dạng trong hệ trục x-y: e_x =', f"{ex:.4f}", ', e_y =', f"{ey:.4f}", ', gamma_xy =', f"{gamma_xy:.4f}")
# print('\nb. Tensor ứng suất: \n', oij)
# print("\nc. Các ứng suất chính:")
# print("o1 =", f"{o1:.4f}")
# print("o2 =", f"{o2:.4f}")
# print("o3 =", f"{o3:.4f}")
# print("\nCác phương chính ứng suất:")
# print("p1 =", p1)
# print("p2 =", p2)
# print("p3 =", p3)

# plt.figure()
# plot_mohr3d(oij)
