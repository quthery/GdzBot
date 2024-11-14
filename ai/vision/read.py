from aiofiles import open as async_open
from ai.prompts.vision import prompt
from pathlib import Path
import g4f

class Reader:
    async def from_bytes(image: bytes) -> str:
        return await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_4,
            provider=g4f.Provider.Bing,
            messages=[{"role": "user", "content": prompt}],
            image=image
        )
    
    async def to_bytes(path: str | Path) -> bytes:
        with await async_open(path, "rb") as f:
            return await f.read()
        
    def to_bytes_sync(file_path: str) -> bytes:
        with open(file_path, "rb") as f:
            return f.read()

class FromFile(Reader):
    @classmethod
    async def read(self, path: str) -> str:
        text = await self.from_bytes(self.to_bytes_sync(path))
        return text