from PIL import Image
from io import BytesIO
from django.core.files import File


def resize_photo(image):
    im = Image.open(image)
    if im.height <= 350 and im.width <= 350:
        return None
    im.convert('RGB')
    im.thumbnail((350, 350))
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=85)
    return File(thumb_io, name=image.name)
