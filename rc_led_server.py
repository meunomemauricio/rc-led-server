"""Main Server Application."""

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
MAIN_TMPL = 'main_page.html'


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


@app.route('/about')
def about():
    return 'The about page.'
