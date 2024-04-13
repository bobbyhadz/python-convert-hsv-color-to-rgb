# How to convert an HSV color to RGB in Python

import colorsys

rgb = colorsys.hsv_to_rgb(0.2, 0.3, 0.5)
print(rgb)  # 👉️ (0.47, 0.5, 0.35)
