from aiofiles import open as async_open
from pathlib import Path


async def to_bytes(path: str | Path) -> bytes:
	with await async_open(path, "rb") as f:
		return await f.read()
      
def bytes_sync(file_path: str) -> bytes:
    # Открываем изображение в бинарном режиме и читаем его содержимое как байты
    with open(file_path, "rb") as f:
        return f.read()