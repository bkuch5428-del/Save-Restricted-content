# Minimal compatibility shim for Python 3.14 where imghdr was removed.
# Telethon 1.28.5 imports imghdr; this file restores the expected API for the bot runtime.

import pathlib
import mimetypes


def what(file, h=None):
    if h is None:
        with open(file, 'rb') as f:
            h = f.read(32)

    if h.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    if h.startswith(b'\xff\xd8'):
        return 'jpeg'
    if h.startswith(b'GIF87a') or h.startswith(b'GIF89a'):
        return 'gif'
    if h.startswith(b'RIFF') and h[8:12] == b'WEBP':
        return 'webp'
    if h.startswith(b'BM'):
        return 'bmp'
    if h.startswith(b'P7'):
        return 'ppm'

    # Fallback to mimetypes based on extension.
    suffix = pathlib.Path(file).suffix.lower()
    if suffix:
        guess = mimetypes.guess_type(file)[0]
        if guess and guess.startswith('image/'):
            return guess.split('/')[-1]

    return None
