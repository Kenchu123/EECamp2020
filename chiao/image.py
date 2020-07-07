import numpy as np
import colorama
from PIL import Image
from colorama import Fore, Back, Style


class Picture():
    def __init__(self):
        self.im = None
        self.temp_im = None
        self.im_R = None
        self.im_G = None
        self.im_B = None
        self.im_gamma = None
        self.im_black = None
        self.im_color = None
        self.path = ''
        self.other = {}
        self.temp_image = {}

    # read an image into the class and print some information
    def read(self, path):
        self.im = np.array(Image.open(path))
        self.temp_im = self.im.copy()
        self.path = path
        self.get_size()

    def read_other(self, name, path):
        self.other[name] = path

    def move(self, name):
        self.other[name] = self.path

    def retrieve(self, name):
        self.im = np.array(Image.open(self.other[name]))

    def change(self, save_name, get_name):
        self.other[save_name] = self.path
        self.im = np.array(Image.open(self.other[get_name]))

    def save_temp_image(self, name):
        self.temp_image[name] = self.im.copy()

    def position(self, x, y):
        print(f"RGB at position ({x}, {y}) = {self.im[x, y]}")
        return self.im[x, y]

    def get_size(self):
        print(f'image size (width, height) = {self.im.shape[1::-1]}')
        return self.im.shape[1::-1]

    def get_ndim(self):
        print(f'image ndim = {self.im.ndim}')
        return self.im.ndim

    def get_dtype(self):
        print(f'image dtype = {self.im.dtype}')
        return self.im.dtype

    def resize(self, width, height):
        self.im = np.array(Image.open(self.path).resize((width, height)))

    def recover(self):
        if self.rflag == True:
            self.im = self.temp_im.copy()

    def save(self, path, type = 'all'):
        type = type.lower()
        try: 
            if type == 'all':
                Image.fromarray(self.im).save(path)
            elif type == 'red':
                Image.fromarray(self.im_R).save(path)
            elif type == 'green':
                Image.fromarray(self.im_G).save(path)
            elif type == 'blue':
                Image.fromarray(self.im_B).save(path)
            elif type == 'black':
                Image.fromarray(np.uint8(self.im_black)).save(path)
            elif type == 'color':
                Image.fromarray(np.unit8(self.im_color)).save(path)
            elif type == 'gamma':
                Image.fromarray(np.uint8(self.im_gamma)).save(path)
            elif type == 'alpha':
                Image.fromarray(np.uint8(self.im_alpha)).save(path)
            else:
                print('Wrong parameter!')

            print(f"save file in {path}")
        except:
            print("Something wrong!")

    def rotate(self, type = 'left'):
        type = type.lower()
        if type == 'right':
            # self.im = np.rot90(self.im)
            h, w, dim = self.im.shape
            im = np.empty((w, h, 3))
            for i in range(w):
                for j in range(h):
                    im[i, j] = self.im[h - j - 1, i]
            self.im = np.uint8(im.copy())
        elif type == 'left':
            # self.im = np.rot90(self.im, 3)
            h, w, dim = self.im.shape
            im = np.empty((w, h, 3))
            for i in range(w):
                for j in range(h):
                    im[i, j] = self.im[j, w - i - 1]
            self.im = np.uint8(im.copy())
        elif type == 'down':
            # self.im = np.rot90(self.im, 2)
            h, w, dim = self.im.shape
            im = np.empty((h, w, 3))
            for i in range(w):
                for j in range(h):
                    im[j, i] = self.im[h - j - 1, w - i - 1]
            self.im = np.uint8(im.copy())

    def flip(self, type = 'ud'):
        type = type.lower()
        if type == 'ud': # upside-down
            # self.im = np.flipud(self.im)
            h, w, dim = self.im.shape
            im = np.empty((h, w, 3))
            for i in range(w):
                for j in range(h):
                    im[j, i] = self.im[h - j - 1, i]
            self.im = np.uint8(im.copy())
        elif type == 'lr': # left-right
            # self.im = np.fliplr(self.im)
            h, w, dim = self.im.shape
            im = np.empty((h, w, 3))
            for i in range(w):
                for j in range(h):
                    im[j, i] = self.im[j, w - i - 1]
            self.im = np.uint8(im.copy())

    def red(self):
        self.im_R = self.im.copy()
        self.im_R[:, :, (1, 2)] = 0
        return self.im_R

    def green(self):
        self.im_G = self.im.copy()
        self.im_G[:, :, (0, 2)] = 0
        return self.im_G

    def blue(self):
        self.im_B = self.im.copy()
        self.im_B[:, :, (0, 1)] = 0
        return self.im_B

    def rgb(self):
        self.red()
        self.green()
        self.blue()

    def reorder(self, type = 'RGB'):
        temp = self.im.copy()
        type = type.upper()
        if type == 'RGB':
            return
        elif type == 'RBG':
            self.im[:, :, 1] = temp[:, :, 2]
            self.im[:, :, 2] = temp[:, :, 1]
        elif type == 'GRB':
            self.im[:, :, 0] = temp[:, :, 1]
            self.im[:, :, 1] = temp[:, :, 0]
        elif type == 'GBR':
            self.im[:, :, 0] = temp[:, :, 1]
            self.im[:, :, 1] = temp[:, :, 2]
            self.im[:, :, 2] = temp[:, :, 0]
        elif type == 'BRG':
            self.im[:, :, 0] = temp[:, :, 2]
            self.im[:, :, 1] = temp[:, :, 0]
            self.im[:, :, 2] = temp[:, :, 1]
        elif type == 'BGR':
            self.im[:, :, 0] = temp[:, :, 2]
            self.im[:, :, 2] = temp[:, :, 0]

    def black_binarize(self, th):
        self.im_black = np.array(Image.open(self.path).convert('L'))
        self.im_black = (self.im_black > th) * 255

    def color_binarize(self, th, r, g, b):
        im_bool = self.im > th
        h, w, dim = self.im.shape
        self.im_color = np.empty((h, w, 3))
        self.im_color[:, :, 0] = im_bool[:, :, 0] * r
        self.im_color[:, :, 1] = im_bool[:, :, 1] * g
        self.im_color[:, :, 2] = im_bool[:, :, 2] * b

    def alpha(self, name, ratio):
        src = np.array(Image.open(self.other[name]).resize(self.im.shape[1::-1], Image.BILINEAR))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im_alpha = self.im * (1 - ratio) + src * (ratio)

    def invert(self):
        self.im = 255 - self.im
    
    def shift(self, val):
        self.im += val

    def darken(self, val):
        val = round(val)
        self.im //= val

    def gamma(self, val):
        im = np.array(Image.open(self.path), 'f')
        self.im_gamma = 255.0 * (im / 255.0) ** val

    def trimming(self, x, y, w, h):
        self.im = self.im[y:y + h, x:x + w]

    def cut(self, x, y, w, h):
        self.im[y:y + h, x:x + w] = 0

    def paste(self, name, x, y, w, h):
        src = np.array(Image.open(self.other[name]))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im[y:y + h, x:x + w] = src[y:y + h, x:x + w]

    def plus(self, name, x, y, w, h):
        src = np.array(Image.open(self.other[name]))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im[y:y + h, x:x + w] += src[y:y + h, x:x + w]
        
    def main(self):
        while True:
            self.main_menu()
            m = input("Please choose an option: ")
            print()
            if m == '1':
                self.read('eecamp_top.jpg')
            elif m == '2':
                pass 
            elif m == '3':
                pass 
            elif m == '4':
                # self.rotate('left')
                self.flip('ud')
            elif m == '5':
                self.save('test.png')
            elif m == '6':
                pass 
            elif m == '7':
                pass 
            elif m == '8':
                pass 
            else:
                print("Wrong options!!!") 

            print()

    def main_menu(self):
        print("================================================")
        print("1. Read a file.")
        print("2. Read other files.")
        print("3. Change color.")
        print("4. Manipulate the image.")
        print("5. Save the image.")
        print("6. Advanced operations.")
        print("7. Other options.")
        print("8. Quit.")
        print("================================================")
   




if __name__ == "__main__":
    pic = Picture()
    pic.main()
    


