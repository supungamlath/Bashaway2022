from PIL import Image, ImageOps, ImageDraw
import glob
import numpy as np

def get_masked(img):
    # create grayscale image with white circle (255) on black background (0)
    mask = Image.new('L', img.size)
    mask_draw = ImageDraw.Draw(mask)
    width, height = img.size
    mask_draw.ellipse((0, 0, width, height), fill=255)
    img.putalpha(mask)
    # img.show()
    return img

def get_round_images():
    image_list = []
    for filename in glob.glob('images/*.png'): 
        img = Image.open(filename)
        image_list.append(get_masked(img))
    return image_list

def create_sheet():
    return Image.new('RGB',
                 (595, 842),   # A4 at 72dpi
                 (255, 255, 255))  # White

def task():
    sheet = create_sheet()
    imgs = get_round_images()
    initial_pos = (45, 5)
    x_pos, y_pos = initial_pos
    incr_x, incr_y = (sheet.size[0]//2, sheet.size[1]//4)

    sheets = []
    for i, img in enumerate(imgs): 
        if (i>0):
            x_pos += incr_x
            if (i%2==0):
                x_pos = initial_pos[0]
                y_pos += incr_y
            if ((i>0) and (i%8==0)):
                y_pos = initial_pos[1]
                sheets.append(sheet.copy())
                # sheet.show()
                sheet = create_sheet()

        sheet.paste(img, (x_pos,y_pos), img)

    else:
        # sheet.show()
        sheet.save("output.pdf", save_all=True, append_images=sheets)

## Main function
if __name__ == "__main__":
    task()