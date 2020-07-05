from removebg import RemoveBg
rmbg = RemoveBg("XnmshQaJeQpt4WbNC6NDzeXb", "error.log")


def remove_bg(img_path):
    rmbg.remove_background_from_img_file(img_path)
