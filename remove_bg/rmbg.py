from removebg import RemoveBg
import os

rmbg = RemoveBg("XnmshQaJeQpt4WbNC6NDzeXb", "error.log")
path = 'image/removebg'
for pic in os.listdir(path):
    img_path = os.path.join(path, pic)
    rmbg.remove_background_from_img_file(img_path)
    print(f'{img_path} is done')
