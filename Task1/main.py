from Crypto.Cipher import AES
import hashlib
from io import BytesIO
from PIL import Image


def read_from_file():
    with open('Task1/msg_encrypt_12', 'rb') as f:
        ciphertext = f.read()
    return ciphertext


def write_to_txt(password, salt, key):
    with open('Task1/pass_and_salt.txt', 'w') as f:
        f.write('{}{}\n{}{}\n{}{}'.format("Password:", password, "Salt:", salt, "Key:", key))
        f.close()


def AES_Decrypt():
    ciphertext = read_from_file()
    work = False
    for p1 in range(ord('u'), ord('z')+1):
        print(p1)
        for p2 in range(ord('m'), ord('z')+1):
            for p3 in range(ord('t'), ord('z')+1):
                for s1 in range(ord('A'), ord('Z')+1):
                    for s2 in range(ord('A'), ord('Z')+1):
                        if work:
                            exit()
                        password = chr(p1) + chr(p2) + chr(p3)
                        salt = chr(s1) + chr(s2)
                        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 1000, 32)
                        cipher = AES.new(key, AES.MODE_ECB)
                        decrypted_message = cipher.decrypt(ciphertext)
                        try:
                            img = Image.open(BytesIO(decrypted_message))
                            print(p1,p2,p3,s1,s2)
                            img.save("Task1/msg_decrypt.png")
                            write_to_txt(password, salt, key.hex())
                            work = True
                        except:
                            pass


if __name__ == '__main__':
    AES_Decrypt()

