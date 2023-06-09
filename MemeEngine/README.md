# MemeEngine Module

The MemeEngine module is for creating memes based on images and quotes.

The `make_meme` method creates the meme image and
saves it in the provided output directory and returns a path to the created meme.
It uses the `pillow` library to resize thumbnails and draw text on them.

## Dependencies

[pillow](https://pillow.readthedocs.io/en/stable/) => This package is used to
create thumbnails and draw text over images.
