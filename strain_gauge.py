import numpy as np
from scipy.optimize import least_squares

# Inputs
# theta1 = np.radians(30)
# theta2 = np.radians(90)
# theta3 = np.radians(150)
# measured_strain1 = 0.01
# measured_strain2 = 0.02
# measured_strain3 = 0.04

# Define the objective function to minimize
def strain_compnents(x, theta, measured_strain):
    normal_strain_x, normal_strain_y, shear_strain_xy = x
    return measured_strain - (normal_strain_x * np.cos(theta)**2 + normal_strain_y * np.sin(theta)**2 + 2 * shear_strain_xy * np.sin(theta) * np.cos(theta))

# Define the initial guess for the parameters
# x0 = [1, 1, 1]

# Solve the optimization problem using the Least Squares method
# res_lsq = least_squares(strain_compnents, x0, args=([theta1, theta2, theta3], [measured_strain1, measured_strain2, measured_strain3]))

# Extract the solution
# normal_strain_x, normal_strain_y, shear_strain_xy = res_lsq.x


# Display the results
# print("$\sigma$_x =", normal_strain_x)
# print("$\sigma$_y =", normal_strain_y)
# print("$\sigma$_xy =", shear_strain_xy)