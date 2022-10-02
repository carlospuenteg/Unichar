from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Unichar:
    def __init__(self, char:str):
        if len(char) != 1: raise Exception("There must be just 1 character")
        self.char = char


    def ord(self) -> int:
        return ord(self.char)


    def is_ascii(self) -> bool:
        return self.ord() < 128


    def get_base_size(self, img_dim:tuple=(100,100), font_family:str="Helvetica.ttc", font_size:int=100, initial_pos:tuple=(0, 0)) -> int:
        img = Image.new('RGB', img_dim, color='black')

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size) # /System/Library/Fonts

        d.text(initial_pos, self.char, font=font, fill=(255, 255, 255))

        return np.sum(np.array(img))/(np.prod(img_dim)*765)


    def draw(self, img_dim:tuple=(100,100), font_family:str="Helvetica.ttc", font_size:int=100, initial_pos:tuple=(0, 0), background:str="black", font_color:tuple=(255,255,255)):
        img = Image.new('RGB', img_dim, color=background)

        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_family, font_size)

        d.text(initial_pos, self.char, font=font, fill=font_color)

        img.show()


    def __str__(self) -> str:
        return self.char
