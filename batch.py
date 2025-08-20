from PIL import Image
import os
from multiprocessing import Pool
import time

def get_png_images(folder):
    png_images = []
    for file in os.listdir(folder):
        if file.lower().endswith('.png'):
            png_images.append(os.path.join(folder, file))
    return png_images

# Takes a list of image paths and overlays them onto Background1.jpg
def compose_png_image(image):
    try:
        img = Image.open(image)
        if img.size[0] != 2500 or img.size[1] != 2000:
            img = img.resize((2000, int((img.size[1] / img.size[0]) * 2000)))
        bg = Image.open(background_image)
        bg.paste(img, (0, 0), img)
        bg.save(os.path.join(temp_folder, os.path.basename(image)))
    except Exception as e:
        print(f"Error processing {image}: {e}")


if __name__ == "__main__":
    start = time.time()
    source_folder = "./MISC_2"
    temp_folder = "./MISC_2/temp"
    global background_image
    background_image = "./background1.jpg"

    if not os.path.isdir(temp_folder):
        os.mkdir(temp_folder)

    images = get_png_images(source_folder)

    with Pool(processes=12) as pool:
        pool.map(compose_png_image, images)

    end = time.time()
    print(end - start)


