# -*- coding: utf-8 -*-


import os
import sys
#import PIL
import textwrap

from optparse import OptionParser
from PIL import ImageFont
from PIL import Image,ImageOps
from PIL import ImageDraw


FOREGROUND = (255, 255, 255)


def draw(img_path, font_path, font_color, text):
    #fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    
    #print "fonts:",font_path
    FOREGROUND = 129
    font = ImageFont.truetype(font_path, 24)
    if img_path:
        img = Image.open(img_path)
    else:
        img=Image.new("RGBA", (1000,600),(205, 181, 205))

    #img = ImageOps.expand(img,border=2,fill='white')
    #img = ImageOps.expand(img,border=2,fill='black')
    draw = ImageDraw.Draw(img)
    W, H = img.size
    w, h = draw.textsize(text)
    center_width, center_height = ((w-W)/2,(H-h)/2)
    draw_to_text = unicode(text,'utf-8')
    #draw_to_text = text
    lines = textwrap.wrap(draw_to_text, width = 20)
    width, height = font.getsize(lines[0])
    last_line_height = len(lines) * height + h
    print "Last line height:",last_line_height
    
    if last_line_height > H - 70:
        img=Image.new("RGBA", (1000,last_line_height + 20),(205, 181, 205))
        FOREGROUND = '#030303'

    y_text = 50
    
    print W,H,":",w,h
    #print lines
    for line in lines:
        draw = ImageDraw.Draw(img)
        width, height = font.getsize(line)
        print width,height
        draw_to_text = line
        #print line
        draw.text((100 + 30, y_text), line, font = font, fill=FOREGROUND)
        y_text += height

   

    #draw.text((center_width, y_text), draw_to_text, font = font, fill=128)
    draw = ImageDraw.Draw(img)
    img.save('static/images/output.png')
   
    #text_to_draw = unicode(text,'utf-8')
    #print text, text_to_draw
    #w, h = draw.textsize(text)
    #draw.text(((W-w)/2,(H-h)/2), text_to_draw, font_color, font=font)
    #draw = ImageDraw.Draw(img)
    #bg.save("a_test_new.png")


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
    font_path = options.font or '/static/fonts/DejaVuSans.ttf'
    font_color = (44, 53, 57)

  
    #print src_img,text,font_path
    draw(src_img, font_path, font_color, text)
