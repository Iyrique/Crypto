from PIL import Image
from pyzbar.pyzbar import decode


def open_image():
    image = Image.open("photo.png")
    return image


def creator_qr():
    image = open_image()
    width, height = image.size
    qr_rb = Image.new("1", (width, height))
    qr_rg = Image.new("1", (width, height))
    qr_bg = Image.new("1", (width, height))
    qr_rb_p = qr_rb.load()
    qr_rg_p = qr_rg.load()
    qr_bg_p = qr_bg.load()
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            decoded_r = r & 1
            decoded_g = g & 1
            decoded_b = b & 1
            qr_rb_p[x, y] = decoded_r ^ decoded_b
            qr_rg_p[x, y] = decoded_r ^ decoded_g
            qr_bg_p[x, y] = decoded_b ^ decoded_g
    qr_rb.save('qr_rb.png')
    qr_rg.save('qr_rg.png')
    qr_bg.save('qr_bg.png')


def qr_reader(file_name):
    img = Image.open(file_name)
    qr_code = decode(img)
    if qr_code:
        return qr_code[0].data.decode('utf-8')
    return None


if __name__ == '__main__':
    creator_qr()
    if qr_reader("qr_rg.png") is not None:
        print(qr_reader("qr_rg.png"))
    elif qr_reader("qr_bg.png") is not None:
        print(qr_reader("qr_bg.png"))
    else:
        print(qr_reader("qr_rb.png"))

