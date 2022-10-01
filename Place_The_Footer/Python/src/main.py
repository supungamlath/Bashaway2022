from PIL import Image
import glob

def get_images():
    image_list = []
    for filename in glob.glob('input/*.jpeg'): 
        img = Image.open(filename)
        image_list.append(img)
    return image_list


def task():
    imgs = get_images()
    footer = Image.open("footer.png")
    
    for img in imgs:
        x,y = img.size
        img.paste(footer,(0, img.size[1] - footer.size[1]))
        filename = img.filename.split('/')[-1]
        img.save("output/" + filename)

if __name__ == "__main__":
    task()
