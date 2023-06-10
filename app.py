"""Run pythod web app using Flask."""
import random
import os
from PIL import Image
from PIL import UnidentifiedImageError
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


def download_image(url, tmp_req_img_path):
    """Download a image from url and save to temp folder."""
    response = requests.get(url, stream=True)
    img_from_url = Image.open(response.raw)
    os_path_basename = os.path.basename(url)
    tmp_img_path = os.path.join(tmp_req_img_path, os_path_basename)
    img_from_url.save(tmp_img_path)
    return tmp_img_path


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    tmp_req_img_path = './tmp/'
    try:
        tmp_img_path = download_image(image_url, tmp_req_img_path)
    except requests.exceptions.ConnectionError:
        print("It looks like the image url is invalid")
        return render_template('meme_error.html')
    except UnidentifiedImageError:
        print("It looks like the image url is invalid")
        return render_template('meme_error.html')
    except requests.exceptions.MissingSchema:
        print("It looks like the image url is invalid")
        return render_template('meme_error.html')
    path = meme.make_meme(tmp_img_path, body, author)
    if os.path.exists(tmp_img_path):
        os.remove(tmp_img_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
