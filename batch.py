from PIL import Image
import os
import shutil
from multiprocessing import Pool
import time

def get_png_images(folder):
    png_images = []
    for file in os.listdir(folder):
        if file.lower().endswith('.png'):
            png_images.append(os.path.join(folder, file))
    return png_images

def get_jpg_images(folder):
    png_images = []
    for file in os.listdir(folder):
        if file.lower().endswith('.jpg'):
            png_images.append(os.path.join(folder, file))
    return png_images

def compose_png_image(image):
    try:
        img = Image.open(image)
        img_name = os.path.basename(os.path.splitext(image)[0])
        if img.size[0] != 2500 or img.size[1] != 2000:
            img = img.resize((2000, int((img.size[1] / img.size[0]) * 2000)))
        bg = Image.open(background_image)
        bg.paste(img, (0, 0), img)
        save_path = os.path.join(temp_folder, img_name + ".jpg")
        bg.save(save_path, format="JPEG", quality=95)
    except Exception as e:
        print(f"Error processing {image}: {e}")
    


if __name__ == "__main__":
    source_folder = "./MISC_2"
    destination_folder = "./MISC_1"
    temp_folder = "./MISC_2/temp"
    verified_folder, ver_size = "./VERIFIED_IMAGES", (320, 400)
    verified_large_folder, verl_size = "./VERIFIED_IMAGES_LARGE", (640, 800)
    thumbnails_folder, thum_size = "./THUMBNAILS", (140, 175)
    composite_folder, comp_size = "./COMPOSITE_IMAGES", (640, 800)

    global background_image
    background_image = "./background1.jpg"


    if not os.path.isdir(temp_folder):
        os.mkdir(temp_folder)

    images = get_png_images(source_folder)

    with Pool(processes=12) as pool:
        pool.map(compose_png_image, images)

    for image in get_jpg_images(temp_folder):
        img = Image.open(image)
        small_image = img.resize(thum_size)
        normal_image = img.resize(ver_size)
        large_image = img.resize(comp_size)
        
        small_image.save(os.path.join(thumbnails_folder, os.path.basename(image)), format="JPEG", quality=95)
        normal_image.save(os.path.join(verified_folder, os.path.basename(image)), format="JPEG", quality=95)
        large_image.save(os.path.join(verified_large_folder, os.path.basename(image)), format="JPEG", quality=95)
        large_image.save(os.path.join(composite_folder, os.path.basename(image)), format="JPEG", quality=95)

    for image in get_png_images(source_folder):
        shutil.move(image, os.path.join(destination_folder, os.path.basename(image)))

    shutil.rmtree(temp_folder)