from pathlib import Path
import aiopytesseract

async def scan_image(path:str) -> str:

    return await aiopytesseract.image_to_string(
        path,
        dpi=300,
        lang='rus+eng'
    )


