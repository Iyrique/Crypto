from PIL import Image
import numpy as np


def open_image():
    image = Image.open("photo.png")
    return image


def creator():
    image = open_image()
    width, height = image.size
    qr_rb = [[0 for _ in range(height)] for _ in range(width)]
    qr_rg = [[0 for _ in range(height)] for _ in range(width)]
    qr_bg = [[0 for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            decoded_r = r & 1
            decoded_g = g & 1
            decoded_b = b & 1
            qr_rb[x][y] = (decoded_r % 2) * 255 + (decoded_b % 2) * 255
            qr_rg[x][y] = (decoded_r % 2) * 255 + (decoded_g % 2) * 255
            qr_bg[x][y] = (decoded_b % 2) * 255 + (decoded_g % 2) * 255
    Image.fromarray(np.asarray(qr_rb).astype('uint8'), mode="L").save('qr_rb.png')
    Image.fromarray(np.asarray(qr_rg).astype('uint8'), mode="L").save('qr_rg.png')
    Image.fromarray(np.asarray(qr_bg).astype('uint8'), mode="L").save('qr_bg.png')


if __name__ == '__main__':
    creator()

