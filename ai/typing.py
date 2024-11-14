from ai.prompts import physics

types = {
    "Физика🌠" : physics,
    "Алгебра➗": "algebra",
    "Математика➕": "math",
    "Химия📈": "chemistry",
    "Информатика💻": "computer science",
}


async def get_type(text: str):
    for key in types.keys():
        if key == text:
            return key  # Возвращаем строку, а не модуль
    return None