import g4f
import g4f.Provider
from ai.vision import FromFile
from ai.answer.models import InputData, OutputData
from ai.typing import types
from typing import Optional 

class Answerer:
    @staticmethod
    async def answer(data: OutputData):
        text = await FromFile.read(path=data.image)
        prompt_ph = """
Answer strictly in Russian for a Russian-speaking audience, following this concise structure in four blocks. Format your response in a table as follows:
Block	Description
Given	List the conditions of the problem.
SI System	Convert values to SI units if needed; leave blank if not necessary.
Formulas	State formulas for solving the problem, without extra words.
Solution	Write a short and clear solution in steps, with a final answer.

Provide the answer in grammatically correct Russian language, without extra explanations, and replace 'cdot' with '×' for multiplication and create table for markdown.
"""
        answer = await g4f.ChatCompletion.create_async(
                model=g4f.models.gpt_4o,
                messages=[{"role": "user", "content": prompt_ph + text}],
        )
        print(answer)
        return answer
    @staticmethod
    async def create_output(data: InputData) -> Optional[OutputData]:
        if data.type not in types.keys():
            return None  

        prompt = types[data.type]
        print(str(prompt))
        return OutputData(
            model=g4f.models.gpt_4o,
            type=str(data.type),
            image=data.image,
            prompt=str(prompt)
        )


    
      

    

    
        