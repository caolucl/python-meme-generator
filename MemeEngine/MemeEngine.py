"""Create MemeEngine class."""
# pylint: disable=too-few-public-methods
import os
import random
from PIL import Image, ImageFont, ImageDraw
import datetime
import random
import string


class MemeEngine:
    """Define MemeEngine class to create meme from images and text."""

    def __init__(self, output_dir):
        """Save and create the output directory path."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create meme based on image and text."""
        img = Image.open(img_path)
        basename = ".jpg"
        prefix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        letters = string.ascii_lowercase
        length = 10
        str = ''.join(random.choice(letters) for i in range(length))
        filename = "_".join([prefix, str, basename])
        outfile = os.path.join(self.output_dir, filename)
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img.thumbnail((width, height))
        path_font = './_data/font/LilitaOne-Regular.ttf'
        font = ImageFont.truetype(path_font, size=20)
        text_position = random.choice(range(30, height - 50))
        fill = 'white'
        stroke_fill = (255, 255, 255)
        # Draw the text on image
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, fill, font=font,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_position + 25), f"- {author}", fill, font,
                  stroke_width=1, stroke_fill=stroke_fill)
        img.save(outfile, "JPEG")
        return outfile
