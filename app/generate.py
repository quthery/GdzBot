import g4f


class Answer_gpt:
    def __init__(self, model): 
        self.model = model  

    async def answer_physics_test(self, image):
        text1 = "What is written on the picture? Solve the problem from the data you got by dividing the solution into 4 blocks. Write the answer only in Russian!!!"



        return await g4f.ChatCompletion.create_async(
            model=self.model,
            messages=[{"role": "user", "content": text1}],
            image = image
        )

    async def answer_physics(self, text):
        example = '''Дано:
        m = 125 кг, h = 70 см, t = 0,3 с

        В СИ:
        m = 125 кг, h = 0,7 м, t = 0,3 с

        Формулы:
        F = mg, W = Fh, P = W/t

        Решение:
        F = 125 кг × 9,8 м/с² = 1225 Н
        W = 1225 Н × 0,7 м = 858 Дж
        P = 858 Дж / 0,3 с = 2860 Вт
        '''
        text1 = ('''write without further explanation, also divide the answer into 4 blocks: 
                "Given, SI system (if necessary, convert values to it, if not, leave blank), 
                "The formulas you'll use to solve the problem, write them without extra words!, The solution in 
                The solution is so short and clear
                Structure, write the example I've provided.
    translate my request into English, and in the answer be sure to write everything in Russian!
    Замени cdot на привычные нам знак умножения и без каких либо лишних скобок

    ''' + example)



        return await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_4o,
            messages=[{"role": "user", "content": text + text1}],
        )

    async def answer_math(self, text:str):
        text1 = 'Solve an algebra problem, at the end of the solution explain how you did it. The most important request is to write the solution very briefly and in order without any explanations and the answer only the number or the value that you got in the end. One more important mention, write the answer completely in Russian!'
        return await g4f.ChatCompletion.create_async(
            model=self.model,
            messages=[{"role": "user", "content": text.strip() + text1}],
        )

