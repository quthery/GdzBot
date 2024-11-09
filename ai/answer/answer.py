import g4f
from ai.vision import FromFile
from ai.answer.models import InputData

class Answerer:
	async def answer(data: InputData):
		return await g4f.ChatCompletion.create_async(
				model=data.model,
				messages=[{"role": "user", "content": data.content}],
				image=FromFile.read(data.image)
		)
	

	
		