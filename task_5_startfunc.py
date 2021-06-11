def world():
    return "Hello World"


def kyrgyzstan():
    return "Hello Kyrgyzstan"


def bishkek():
    return "Hello Bishkek"


user_tip = """Введите одну из функций:
world()
kyrgyzstan()
bishkek()
-> 
"""
func = input(user_tip)
eval(f'print({func})')
