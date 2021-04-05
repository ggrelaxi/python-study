from PIL import Image, ImageDraw, ImageFont
import os
from fileScanner import fileScanner

def imgFormatConverter(sourceExtension, DestinationExtension):
    correctImages = fileScanner(sourceExtension)

    for i in range(len(correctImages)):
        f, e = os.path.splitext(correctImages[i])
        outImg = f + '.' + DestinationExtension

        with Image.open(correctImages[i]) as img:
            rgb_img = img.convert('RGB')
            draw = ImageDraw.Draw(rgb_img)

            width, height = rgb_img.size

            topX = (width / 2) - 100
            topY = (height / 2) + 100
            bottomX = (width / 2) + 100
            bottomY = (height / 2) - 100

            draw.rectangle([topX, topY, bottomX, bottomY], None, 'red', 5)

            font = ImageFont.truetype("arial.ttf", 50)
            draw.multiline_text((width / 2 - 75, height / 2 - 50), 'Hello,\nWorld!', font=font)

            rgb_img.save(outImg)
            os.remove(correctImages[i])
        
imgFormatConverter('png', 'jpg')