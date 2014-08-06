import os
import sys
import PIL

from optparse import OptionParser
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def draw(img_path, font_path, font_color, text):
    #fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    
    print "fonts:",font_path
    font = ImageFont.truetype(font_path, 24)
    if img_path:
        img = Image.open(img_path)
    else:
        img=Image.new("RGBA", (200,200),(120,20,20))
    
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text ,font_color, font=font)
    draw = ImageDraw.Draw(img)
    draw = ImageDraw.Draw(img)
    img.save("a_test.png")


if __name__ == '__main__':
    optparser = OptionParser()
    optparser.add_option("-t", "--text",
                         type="string", dest="text")
    optparser.add_option("-s", "--source",
                         type="string", dest="source")
    optparser.add_option("-f", "--font",
                         type="string", dest="font")
    optparser.add_option("-c", "--color",
                         type="string", dest="font_color")
    (options, args) = optparser.parse_args()

    text = options.text or search_word
    src_img = options.source or ''
    font_path = options.font or '/static/fonts/FreeMono.ttf'
    font_color = (44, 53, 57)

  
    print src_img,text,font_path
    draw(src_img, font_path, font_color, text)
