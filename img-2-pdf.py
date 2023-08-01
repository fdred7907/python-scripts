import os
import img2pdf
from pathlib import Path
import imageio as iio


path_to_img_str = input("Enter image to convert file path :")
path_to_img = os.path.join(os.getcwd(),Path(path_to_img_str))
with open('output.pdf','wb') as file:
    file.write(img2pdf.convert([i for i in os.listdir(path_to_img) if i.endswith(".jpg")]))

    