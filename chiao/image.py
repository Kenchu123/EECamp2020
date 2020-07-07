'''
  This file implement a Command Line Interface(CLI) for a image processer.
  This is for 2020 eecamp.

  Author: yingchiaochen
'''

import numpy as np
# import colorama
from PIL import Image
# from colorama import Fore, Back, Style


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
        self.files = {}
        self.temp_image = {}

    def main(self):
        while True:
            self.main_menu()
            m = input(">> Please choose an option: ")
            print()
            if m == '0':
                Image.fromarray(self.im).show()
            elif m == '1':
                try: 
                    while True:
                        self.read_menu()
                        msg = input(">> Please choose an option: ")
                        if msg == '1':
                            path = input(">> Please enter your image path: ")
                            if path == '':
                                path = 'eecamp.jpg'
                            print()
                            name = path[:path.find('.')]
                            self.read(name, path)
                            print()
                        elif msg == '2':
                            path = input(">> Please enter your image name: ")
                            print()
                            name = path[:path.find('.')]
                            self.read_other(name, path)
                            print("This image is saved in the backup list!!\n")
                        elif msg == '3':
                            print()
                            break
                        else:
                            print()
                            print("Wrong option! Please enter again! \n")
                except: 
                    print("Something wrong!!!\n")
                
            elif m == '2':
                try: 
                    while True:
                        self.color_menu()
                        choice = input(">> Please choose and option: ")
                        if choice == '1':
                            self.red()
                            print()
                        elif choice == '2':
                            self.green()
                            print()
                        elif choice == '3':
                            self.blue()
                            print()
                        elif choice == '4':
                            self.rgb()
                            print()
                        elif choice == '5':
                            seq = input(">> Please enter a color sequence(RGB or RBG ...): ")
                            self.reorder(seq)
                            print()
                        elif choice == '6':
                            val = input(">> Please enter a brightness value(1 ~ 2): ")
                            self.brighten(float(val))
                            print()
                        elif choice == '7':
                            val = input(">> Please enter a darkness value(1 ~ 10): ")
                            self.darken(float(val))
                            print()
                        elif choice == '8':
                            self.invert()
                            print()
                        elif choice == '9':
                            print()
                            break
                        else:
                            print("Wrong option! Please enter again! \n")
                except:
                    print("Something wrong!")

            elif m == '3':
                try: 
                    while True:
                        self.manipulate_menu()
                        choice = input(">> Please choose an option: ")
                        if choice == '1':
                            direction = input(">> Please enter the direction(right, left, down): ")
                            self.rotate(direction)
                            print()
                        elif choice == '2':
                            direction = input(">> Please enter the direction(ud or lr): ")
                            self.flip(direction)
                            print()
                        elif choice == '3':
                            x, y, w, h = input(">> Please enter the trimming area(x, y, w, h): ")
                            x, y, w, h = int(x), int(y), int(w), int(h)
                            self.trimming(x, y, w, h)
                            print()
                        elif choice == '4':
                            x, y, w, h = input(">> Please enter the cutting area(x, y, w, h): ")
                            x, y, w, h = int(x), int(y), int(w), int(h)
                            self.cut(x, y, w, h)
                            print()
                        elif choice == '5':
                            w, h = input(">> Please enter the resize area(w, h): ")
                            w, h = int(w), int(h)
                            self.resize(w, h)
                            print()
                        elif choice == '6':
                            print()
                            break
                        else:
                            print("Wrong option! Please enter again! \n")
                except:
                    print("Something wrong!")
                        
            elif m == '4':
                try: 
                    path = input('>> Please enter the save path: ')
                    if path == '': 
                        path = 'test'     
                    print()
                    self.save(path + '.png')
                    print()
                except:
                    print("Something wrong!")

            elif m == '5':
                try: 
                    while True:
                        self.advanced_menu()
                        choice = input(">> Please choose an option: ")
                        if choice == '1':
                            th = input(">> Please enter a threshold value(0 ~ 255): ")
                            self.black_binarize(int(th))
                            print()
                        elif choice == '2':
                            val = input(">> Please enter a gamma vale: ")
                            self.gamma(float(val))
                            print()
                        elif choice == '3':
                            print()
                            break
                        else: 
                            print("Wrong option! Please enter again! \n")
                except:
                    print("Something wrong!")
                    
            elif m == '6':
                try: 
                    self.recover()
                    print("\nYour image is recovered back to the original one.\n")
                except:
                    print("Something wrong!")

            elif m == '7':
                try: 
                    while True:
                        self.configuration_menu()
                        choice = input('>> Please choose an option: ')
                        if choice == '1':
                            x, y = print(">> Please enter the position you want to look (x, y), separate by a space: ").split(' ')
                            x, y = int(x), int(y)
                            self.rgb_value(x, y)
                            print()
                        elif choice == '2':
                            print()
                            self.get_size()
                            print()
                        elif choice == '3':
                            print()
                            break
                        else:
                            print("Wrong option! Please enter again! \n")
                except:
                    print("Something wrong!")

            elif m == '8':
                break
            else:
                print("Wrong option!!!") 

    def main_menu(self):
        print("================================================")
        print("0. Show the image.")
        print("1. Read a file.")
        print("2. Change image color.")
        print("3. Manipulate the image.")
        print("4. Save the image.")
        print("5. Advanced operations.")
        print("6. Recover the image.")
        print("7. Configurations.")
        print("8. Exit.")
        print("================================================")

    def read_menu(self):
        print("================================================")
        print("1. Read an image.")
        print("2. Read anther image.")
        print("3. Exit.")
        print("================================================")

    def color_menu(self):
        print("================================================")
        print("1. Get red part of the image.")
        print("2. Get green part of the image.")
        print("3. Get blue part of the image.")
        print("4. Get RGB of the image.")
        print("5. Reorder the RGB value.")
        print("6. Brighten the image.")
        print("7. Darken the image.")
        print("8. Invert an image.")
        print("9. Exit.")
        print("================================================")

    def manipulate_menu(self):
        print("================================================")
        print("1. Rotate the image.")
        print("2. Flip the image.")
        print("3. Trim the image.")
        print("4. Cut the image.")
        # print("5. Paste the image.")
        # print("6. Plus the image.")
        print("5. Resize the iamge.")
        print("6. Exit.")
        print("================================================")

    def advanced_menu(self):
        print("================================================")
        print("1. black binarization")
        # print("2. color binarization")
        print("2. gamma correction")
        print("3. Exit.")
        # print("4. alpha blending")
        print("================================================")
        

    def configuration_menu(self):
        print("================================================")
        print("1. Get the RGB value.")
        print("2. Get the image size.")
        print("3. Exit.")
        print("================================================")


    ###########################################################################
    '''
      This area is for functions that read or change images into the program. 
      Functions:
      Note: Only the read and read_other functions are written in the main functon.
            If you want to use the other functions, please write your own code into
            the main function or just import it.
        - read: 
            Read an image into the program. This function will save the image
            as the main image. All functions in this class will only operate 
            on the main image. 
        - read_other: 
            Read another image into the program. We only save the image as a 
            path into a dictionary. Only when we do some specific operation will
            the image fetched from the dictionary.
        - retrive:  
            Change the main image to another image from the dictionary. This 
            function will not save the main you read before. So please be careful
            if you want to save the image. 
        - save_temp_image:
            Save the image temporarily if you may mess up the next operation.
        - change:
            Change the main image to another image you specify. This function will 
            save the main image in the temporary image dictionary. The name is the
            filename without the file extension. (Ex. test.png -> test is the name)
    '''
    ###########################################################################
    # read an image into the class and print some information
    def read(self, name, path):
        self.im = np.array(Image.open(path))
        self.files[name] = path
        self.temp_im = self.im.copy()
        self.path = path
        self.get_size()

    def read_other(self, name, path):
        self.files[name] = path

    def save_temp_image(self, name):
        self.temp_image[name] = self.im.copy()

    def retrieve(self, name):
        self.im = np.array(Image.open(self.files[name]))
        self.temp_im = self.im.copy()

    def change(self, save_name, get_name):
        self.files[save_name] = self.path
        self.temp_image[save_name] = self.im.copy()
        self.im = np.array(Image.open(self.files[get_name]))
        self.temp_im = self.im.copy()

    ###########################################################################
    '''
      This area is for manipulating the image RGB value.
        
        red:
            save the red part of the iamge into self.im_R
        green:
            save the green part of the iamge into self.im_G
        blue:
            save the blue part of the iamge into self.im_B
        rgb:
            execute the red, green, and blue functions above simultaneously
        reorder:
            reorder the image's RGB value, which can be specified as 'RGB' or 'GRB', and so on.
        brighten:
            enhance each RGB value in the iamge simultaneously
        darken: 
            decrease each RGB value in the iamge simultaneously
        invert:
            invert each pixel RGB value from x to 255 - x.
        shift:
            shift each pixel RGB value. This operation is a modulo operation.
        
    '''
    ###########################################################################
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

    def brighten(self, val):
        h, w, dim = self.im.shape
        print("Brightening your image...")
        for i in range(h):
            for j in range(w):
                for k in range(3):
                    self.im[i, j, k] = min(255, self.im[i, j, k] * val)

    def darken(self, val):
        print("Darkening your image...")
        val = round(val)
        self.im //= val

    def invert(self):
        self.im = 255 - self.im
    
    def shift(self, val):
        self.im += val

    ###########################################################################
    '''
      This area is for manipulating the image without changing the RGB valuse.
      
        rotate: 
            rotate an image by 90, 180, 270 degrees
        flip:
            flip an image upside-down or left-right
        trimming:
            trimming out the image outside the selected range
        cut:
            cut a part of the image in the given range
        paste:
            paste a part of the image into another image in a given range
        plus:
            add a part of the image to another image in a given range
        resize:
            resize the image into a given width and height
        
    '''
    ###########################################################################
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

    def trimming(self, x, y, w, h):
        self.im = self.im[y:y + h, x:x + w]

    def cut(self, x, y, w, h):
        self.im[y:y + h, x:x + w] = 0

    def paste(self, name, x, y, w, h):
        src = np.array(Image.open(self.files[name]))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im[y:y + h, x:x + w] = src[y:y + h, x:x + w]

    def plus(self, name, x, y, w, h):
        src = np.array(Image.open(self.files[name]))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im[y:y + h, x:x + w] += src[y:y + h, x:x + w]

    def resize(self, width, height):
        self.im = np.array(Image.open(self.path).resize((width, height)))

    ###########################################################################
    '''
      This is the comment for save function. The save function is just to save
      the file.
      type:
            normal: 
                save the main image.
            red:
                save the red part of the image.
            green:
                save the green part of the image.
            blue:
                save the blue part of the image.
            black:
                save the black binarization of the image.
            color:
                save the color binarization of the image.
            gamma:
                save the gamma correction of the image.
            alpha:
                save the alpha blending of the image.
            all:
                save all images
    '''
    ###########################################################################
    def save(self, path, type = 'normal'):
        type = type.lower()
        try: 
            if type == 'normal':
                Image.fromarray(self.im).save(path)
            elif type == 'red':
                Image.fromarray(self.im_R).save(path)
            elif type == 'green':
                Image.fromarray(self.im_G).save(path)
            elif type == 'blue':
                Image.fromarray(self.im_B).save(path)
            elif type == 'black':
                Image.fromarray(self.im_black).save(path)
            elif type == 'color':
                Image.fromarray(self.im_color).save(path)
            elif type == 'gamma':
                Image.fromarray(self.im_gamma).save(path)
            elif type == 'alpha':
                Image.fromarray(self.im_alpha).save(path)
            elif type == 'all':
                if self.im != None:
                    Image.fromarray(self.im).save(path)
                if self.im_R != None:
                    Image.fromarray(self.im_R).save(path + '_red')
                if self.im_G != None:
                    Image.fromarray(self.im_G).save(path + '_green')
                if self.im_B != None:
                    Image.fromarray(self.im_B).save(path + '_blue')
                if self.im_black != None:
                    Image.fromarray(self.im_black).save(path + '_black')
                if self.im_color != None:
                    Image.fromarray(self.im_color).save(path + '_color')
                if self.im_gamma != None:
                    Image.fromarray(self.im_gamma).save(path + '_gamma')
                if self.im_alpha != None:
                    Image.fromarray(self.im_alpha).save(path + '_alpha')
            else:
                print('Wrong parameter!')

            print(f"save file in {path}")
        except:
            print("Something wrong!")

    ###########################################################################
    '''
      This area is for advanced operations.
      
        black_binarize: 
            change an image into and binarized image based on a threshold
        color_binarize:
            change an image into and binarized image based on thresholds of three colors
        gamma:
            do gamma correction on the image
        alpha:
            do alpha blending of two images
    '''
    ###########################################################################

    def black_binarize(self, th):
        self.im_black = np.array(Image.open(self.path).convert('L'))
        self.im_black = (self.im_black > th) * 255
        self.im_black = np.uint8(self.im_black)

    def color_binarize(self, th, r, g, b):
        im_bool = self.im > th
        h, w, dim = self.im.shape
        self.im_color = np.empty((h, w, 3))
        self.im_color[:, :, 0] = im_bool[:, :, 0] * r
        self.im_color[:, :, 1] = im_bool[:, :, 1] * g
        self.im_color[:, :, 2] = im_bool[:, :, 2] * b
        self.im_color = np.uint8(self.im_color)

    def alpha(self, name, ratio):
        src = np.array(Image.open(self.files[name]).resize(self.im.shape[1::-1], Image.BILINEAR))
        dim = src.shape[2]
        if dim == 4:
            src = src[:, :, :-1]
        self.im_alpha = self.im * (1 - ratio) + src * (ratio)
        self.im_alpha = np.uint8(self.im_alpha)

    def gamma(self, val):
        im = np.array(Image.open(self.path), 'f')
        self.im_gamma = 255.0 * (im / 255.0) ** val
        self.im_gamma = np.uint8(self.im_gamma)

    ################################################################
    '''
      This is the recover function. This function will recover the main
      image back to the clean original image.
    '''
    ################################################################
    def recover(self):
        self.im = self.temp_im.copy()

    ################################################################
    '''
      This area is for configuration functions.

        rgb_value: 
            Return the rgb value at the specified location.
        get_size: 
            Return the image size, including width and height.
        get_ndim: 
            Return the dimension of the image.
        get_dtype:
            Return the data type of the image.
        resize:
            Resize the main image.
        recover:
            Recover the main image to the saved temp image.
    '''
    ################################################################
    def rgb_value(self, x, y):
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
    
        
if __name__ == "__main__":
    pic = Picture()
    pic.read("eecamp", "eecamp.jpg")
    pic.main()
    


