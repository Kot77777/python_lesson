from PIL import Image
import numpy as np

for i in range(1, 4):
    img = Image.open(f'lunar0{i}_raw.jpg')
    data = np.array(img)

    larg = np.max(data)
    small = np.min(data)

    updated_data = (data - small) * (255 / (larg - small))
    updated_data = updated_data.astype(np.uint8)

    res_img = Image.fromarray(updated_data)
    res_img.save(f'lunar_image_0{i}_update.jpg')