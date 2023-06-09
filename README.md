# Meme Generator

A python web application that generates memes from random images or image from url link.

## Prerequisites

### Require 3 python libraries
* [Flask](https://github.com/pallets/flask): Simple web server interface
* [Pandas](https://github.com/pandas-dev/pandas): Easy processing meme text from csv files
* [Pillow](https://github.com/python-pillow/Pillow): Image processing to add text

### Install program to convert from PDF to TXT
Download and install the `pdftotext` command line tool from: https://www.xpdfreader.com/download.html

## Download source code and create virtual environment

### Clone this repo.
   ```sh
   git clone https://github.com/caolucl/python-meme-generator.git
   ```
### Create virtual environment 
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
### Install required python libraries
   ```sh
   pip install -r requirements.txt
  ```
  
## Usage

### Using the cli

```sh
$ python meme.py --help
usage: meme.py [-h] [-p PATH] [-b BODY] [-a AUTHOR]

optional arguments:
  --help            show this help message
  --path PATH  Path to and image file.
  --body BODY  Body or Content written to image.
  --author AUTHOR Author name written to image.
```

### Using Flask Web Development Server
Starting dev server
```sh
$ python app.py

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
Once started(using the default port) go to http://127.0.0.1:5000/
