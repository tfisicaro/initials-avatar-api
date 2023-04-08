from PIL import Image, ImageDraw, ImageFont


def get_initials(name):
    if len(name) == 0:
        raise ValueError('Name is required')

    xs = (name)
    name_list = xs.split()

    initials = ""
    lower = None

    if len(name_list) >= 4:
        name_list = name_list[:4]
        lower = [1, 2]
    if len(name_list) == 3:
        name_list = name_list[:3]
        lower = [1]

    for name in name_list:
        if lower and len(initials) in lower:
            initials += name[0].lower()
        else:
            initials += name[0].upper()

    return initials


def generate_avatar(text='', shape='square', size='128', background_color='lightgrey', text_color='#282828'):
    size = int(size)
    text_length = len(text)

    if text_length >= 4:
        scale_factor = 2.8
        height_adjustment = 2.1
    elif text_length == 3:
        scale_factor = 2.4
        height_adjustment = 2.2
    else:
        scale_factor = 2
        height_adjustment = 2.23

    text_size = int(size / scale_factor)
    try:
        font = ImageFont.truetype('C:\Windows\Fonts\SegoeUI.ttf', text_size)
    except OSError:
        font = ImageFont.truetype('Arial.ttf', text_size)

    # Define our base
    base_background_color = background_color
    if shape == 'circle':
            base_background_color = (255, 255, 255, 0)
    img = Image.new('RGBA', (size, size), color=base_background_color)
    d = ImageDraw.Draw(img)

    # Draw a circle on the base
    if shape == 'circle':
        w, h = img.size
        d.pieslice([(0,0), (w, h)], 0, 360, fill=background_color)

    # Check how big the text will be
    w, h = d.textsize(text, font=font)

    # Draw text in the center of our base image
    d.text(((size-w)/2, (size-h)/height_adjustment), text, font=font, fill=text_color)

    return img
