from PIL import Image, ImageDraw, ImageFont
import numpy as np
import unicodedata # https://docs.python.org/3/library/unicodedata.html

from utils.folders import create_folders

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

    # Returns the code point
    def ord(self) -> int:
        return ord(self.char)

    # Returns the name assigned
    def name(self) -> str:
        return unicodedata.name(self.char)

    # Look up character by name and return the character
    def lookup(name:str) -> str:
        return unicodedata.lookup(name)



    # Returns whether the character is a an ASCII character
    def is_ascii(self) -> bool:
        return self.ord() < 128

    # Returns whether the character is a an extended ASCII character
    def is_extended_ascii(self) -> bool:
        return self.ord() < 256

    # Returns whether the character is printable
    def is_printable(self) -> bool:
        return self.char.isprintable()



    def create_img(self, font_family:str="Helvetica.ttc", img_dim:tuple=(140,140), font_size:int=100, initial_pos:tuple=(20, 20), background:str="black", font_color:tuple=(255,255,255)):
        img = Image.new('RGB', img_dim, color=background)

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=font_color)
        return img



    # Returns the quantity of blackness of the character
    def get_blackness(self, font_family:str="Helvetica.ttc", img_dim:tuple=(100,100), font_size:int=100, initial_pos:tuple=(0, 0)) -> int:
        img = self.create_img(font_family, img_dim, font_size, initial_pos)

        return np.sum(np.array(img))/(np.prod(img_dim)*765)


    # Returns the size of the character
    def get_size(self, font_family:str="Helvetica.ttc", img_dim:tuple=(140,140), font_size:int=100, initial_pos:tuple=(20, 20)) -> int:
        img = self.create_img(font_family, img_dim, font_size, initial_pos)

        first = {"l": -1, "t": -1, "r": -1, "b": -1}
        ranges = {
            "l": (range(img_dim[0]), range(img_dim[1]), lambda i, j: (i, j)),
            "t": (range(img_dim[1]), range(img_dim[0]), lambda i, j: (j, i)),
            "r": (range(img_dim[0]-1, -1, -1), range(img_dim[1]), lambda i, j: (i, j)),
            "b": (range(img_dim[1]-1, -1, -1), range(img_dim[0]), lambda i, j: (j, i))
        }

        # Get the non-black pixel that is more to the top, to the bottom, to the left and to the right
        for k in first.keys():
            for i in ranges[k][0]:
                for j in ranges[k][1]:
                    if img.getpixel(ranges[k][2](i,j)) != (0,0,0):
                        first[k] = i
                        break
                if first[k] != -1: break
        
        return ((first["r"]-first["l"]+1)/font_size, (first["b"]-first["t"]+1)/font_size)


    # Draws the character
    def draw(self, font_family:str="Helvetica.ttc", img_dim:tuple=(140,140), font_size:int=100, initial_pos:tuple=(20, 20), background:str="black", font_color:tuple=(255,255,255)):
        img = self.create_img(font_family, img_dim, font_size, initial_pos)

        img.show()



    def save(self, filename="img.png", font_family:str="Helvetica.ttc", img_dim:tuple=(100,100), font_size:int=100, initial_pos:tuple=(0, 0), background:str="black", font_color:tuple=(255,255,255)):
        create_folders(["output"])
        img = self.create_img(font_family, img_dim, font_size, initial_pos, background, font_color)
        img.save(f"output/{filename}")


    # Returns the character as a string
    def __str__(self) -> str:
        return self.char
