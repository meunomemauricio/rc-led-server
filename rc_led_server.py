"""Main Server Application."""

import base64
import os
import pyqrcode

from datetime import datetime
from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)
MAIN_TMPL = 'main_page.html'
GNRT_KEY_TMPL = 'generate_key.html'


@app.route('/')
@app.route('/rcled')
def main_page():
    return render_template(MAIN_TMPL)


@app.route('/rcled/api/0.1/action', methods=['PUT'])
def control_led():
    """Execute an action to the LED."""

    if not request.json:
        abort(400)

    return jsonify(request.json), 202


@app.route('/rcled/generate_key')
def generate_qr_code():
    """Generate a random key QA Code and display it.

    Image is encoded in a Base64.
    """
    key = base64.b64encode(os.urandom(32))
    image = pyqrcode.create(key).png_as_base64_str(scale=4)
    gen_time = datetime.now()

    return render_template(GNRT_KEY_TMPL, image=image, gen_time=gen_time)
    

@app.route('/about')
def about():
    return 'The about page.'
