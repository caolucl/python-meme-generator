import random
import os
from PIL import Image
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

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
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            try:
                img_from_url = Image.open(response.raw)
                tmp_img_path = os.path.join(tmp_req_img_path, os.path.basename(url))
                img_from_url.save(tmp_img_path)
                return tmp_img_path
            except IOError as e:
                print("Error occurred while opening the image:", e)
            except Image.UnidentifiedImageError as e:
                print("Unknown file extension or corrupted image:", e)
        else:
            print("Failed to download image. Status code:", response.status_code)
            return None
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.RequestException as e:
        print("Error occurred while fetching the image:", e)
    except IOError as e:
        print("Error occurred while saving the image:", e)


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    tmp_req_img_path = './tmp/'
    tmp_img_path = download_image(image_url, tmp_req_img_path)
    path = meme.make_meme(tmp_img_path, body, author)
    if os.path.exists(tmp_img_path):
        os.remove(tmp_img_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
