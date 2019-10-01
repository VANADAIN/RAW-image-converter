import rawpy
from PIL import Image
import os
import PIL

path_to_images = input("path : \n")

def convert(path):

    val_path = path.replace( "\\" , "/" )
    print("")
    save_dir = val_path + "/converted"
    print("Directory to save : " + val_path + "\n")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print(save_dir)

    images = os.listdir(val_path)
    print(images)

    for image in images: 

        try:
            
            if image == 'converted':
                continue
            raw = rawpy.imread(val_path + "/" + image)
            rgb = raw.postprocess(use_camera_wb=True)

            PIL.Image.fromarray(rgb).save( save_dir + "/" + image + ".png", quality=100, optimize=False)
            print(image + " --> saving image")
            raw.close()

        except: 
            print(image + " --> error")

convert(path_to_images)

