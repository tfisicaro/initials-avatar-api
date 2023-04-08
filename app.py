import random
from io import BytesIO
from flask import Flask, request, send_file, make_response, send_from_directory
from application.avatars import get_initials, generate_avatar
from application.settings import SUPPORTED_SHAPES, BACKGROUND_COLORS, DEFAULT_BACKGROUND_COLOR, DEFAULT_TEXT_COLOR, \
    DEFAULT_SIZE, DEFAULT_SHAPE


app = Flask(__name__)


def serve_image(image):
    img_io = BytesIO()
    image.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')


def bad_request(errors=None):
    res = {"status": 400, "message": "Bad Request"}
    if errors:
        res['errors'] = errors
    
    return res


@app.route('/robots.txt')
def static_from_root():
    res = make_response(send_from_directory(app.static_folder, request.path[1:]))
    res.headers['Cache-Control'] = 'max-age=%d' % (60 * 60 * 24 * 30)
    return res


@app.route("/avatar/")
def index():
    errors = []

    name = request.args.get('name', None)
    if name:
        initials = get_initials(name)
    else:
        initials = ''

    size = request.args.get('size', DEFAULT_SIZE)
    if int(size) < 32 or int(size) > 512:
        errors.append('Size must be between 32 and 512')

    shape = request.args.get('shape', DEFAULT_SHAPE)
    if shape not in SUPPORTED_SHAPES:
        errors.append(f'Provided shape is not supported. Choose from: {SUPPORTED_SHAPES}')

    background_color = request.args.get('background', DEFAULT_BACKGROUND_COLOR)
    if background_color == 'random':
        background_color = random.choice(BACKGROUND_COLORS)

    text_color = request.args.get('text', DEFAULT_TEXT_COLOR)

    if len(errors) > 0:
        return bad_request(errors)

    return serve_image(
        generate_avatar(
            text=initials,
            shape=shape,
            size=size,
            background_color=background_color,
            text_color=text_color))
