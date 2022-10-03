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


    def get_blackness(self, font_family:str="Helvetica.ttc", img_dim:tuple=(100,100), font_size:int=100, initial_pos:tuple=(0, 0)) -> int:
        img = Image.new('RGB', img_dim, color='black')

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size) # /System/Library/Fonts

        d.text(initial_pos, self.char, font=font, fill=(255, 255, 255))

        return np.sum(np.array(img))/(np.prod(img_dim)*765)


    def get_size(self, font_family:str="Helvetica.ttc", img_dim:tuple=(140,140), font_size:int=100, initial_pos:tuple=(20, 20)) -> int:
        img = Image.new('RGB', img_dim, color='black')

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=(255, 255, 255))

        # Get the non-black pixel that is more to the top, to the bottom, to the left and to the right
        first = {"l": -1, "t": -1, "r": -1, "b": -1}
        ranges = {
            "l": (range(img_dim[0]), range(img_dim[1]), lambda i, j: (i, j)),
            "t": (range(img_dim[1]), range(img_dim[0]), lambda i, j: (j, i)),
            "r": (range(img_dim[0]-1, -1, -1), range(img_dim[1]), lambda i, j: (i, j)),
            "b": (range(img_dim[1]-1, -1, -1), range(img_dim[0]), lambda i, j: (j, i))
        }

        for k in first.keys():
            for i in ranges[k][0]:
                for j in ranges[k][1]:
                    if img.getpixel(ranges[k][2](i,j)) != (0,0,0):
                        first[k] = i
                        break
                if first[k] != -1: break
        
        return ((first["r"]-first["l"]+1)/font_size, (first["b"]-first["t"]+1)/font_size)


    def draw(self, font_family:str="Helvetica.ttc", img_dim:tuple=(140,140), font_size:int=100, initial_pos:tuple=(20, 20), background:str="black", font_color:tuple=(255,255,255)):
        img = Image.new('RGB', img_dim, color=background)

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=font_color)

        img.show()


    def __str__(self) -> str:
        return self.char
