import aiopytesseract
from pathlib import Path


async def scan_image(path:str):

    return await aiopytesseract.image_to_string(
        path,
        dpi=300,
        lang='rus+eng'
    )


