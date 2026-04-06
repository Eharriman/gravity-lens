from core.lens_equation import image_positions
from core.deflection import point_lens_deflection
from core.lens_mapping import map_theta_to_beta
import numpy as np

theta_E = 1.0
beta_test = 0.5

tp, tm = image_positions(beta_test, theta_E)

theta_vec = np.array([tp, 0.0])
beta_vec = map_theta_to_beta(theta_vec, theta_E)

print(f"The scalar beta is : {beta_test}")
print(f"The mapped vector beta X: {beta_vec[0]}")