from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Unichar:
    def __init__(self, char:str):
        self.char = char


    @property
    def char(self) -> str:
        return self._char


    @char.setter
    def char(self, char:str):
        if len(char) != 1: raise Exception("There must be just 1 character")
        self._char = char


    def ord(self) -> int:
        return ord(self.char)


    def is_ascii(self) -> bool:
        return self.ord() < 128


    def get_blackness(self, img_dim:tuple=(100,100), font_family:str="Helvetica.ttc", font_size:int=100, initial_pos:tuple=(0, 0)) -> int:
        img = Image.new('RGB', img_dim, color='black')

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size) # /System/Library/Fonts

        d.text(initial_pos, self.char, font=font, fill=(255, 255, 255))

        return np.sum(np.array(img))/(np.prod(img_dim)*765)


    def get_size(self, img_dim:tuple=(140,140), font_family:str="Helvetica.ttc", font_size:int=100, initial_pos:tuple=(20, 20)) -> int:
        img = Image.new('RGB', img_dim, color='black')

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=(255, 255, 255))

        # Get the non-black pixel that is more to the left, to the right, to the top and to the bottom
        first_left = -1
        first_top = -1
        first_right = -1
        first_bottom = -1
        
        for i in range(img_dim[0]):
            for j in range(img_dim[1]):
                if img.getpixel((i,j)) != (0,0,0):
                    first_left = i
                    break
            if first_left != -1: break

        for i in range(img_dim[1]):
            for j in range(img_dim[0]):
                if img.getpixel((j,i)) != (0,0,0):
                    first_top = i
                    break
            if first_top != -1: break
        
        for i in range(img_dim[0]-1, -1, -1):
            for j in range(img_dim[1]):
                if img.getpixel((i,j)) != (0,0,0):
                    first_right = i
                    break
            if first_right != -1: break
        
        for i in range(img_dim[1]-1, -1, -1):
            for j in range(img_dim[0]):
                if img.getpixel((j,i)) != (0,0,0):
                    first_bottom = i
                    break
            if first_bottom != -1: break

        print(first_left, first_right, first_top, first_bottom)
        return ((first_right-first_left+1)/font_size, (first_bottom-first_top+1)/font_size)


    def draw(self, img_dim:tuple=(100,100), font_family:str="Helvetica.ttc", font_size:int=100, initial_pos:tuple=(0, 0), background:str="black", font_color:tuple=(255,255,255)):
        img = Image.new('RGB', img_dim, color=background)

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=font_color)

        img.show()


    def __str__(self) -> str:
        return self.char
