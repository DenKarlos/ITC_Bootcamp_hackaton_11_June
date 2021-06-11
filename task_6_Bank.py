from datetime import datetime
from datetime import timedelta


def credit():
    str_dtm = input('Введите дату для оформления кредита в формате: ГГГГ-ММ-ДД ЧЧ:ММ -> ')
    # str_dtm = '1991-02-14 02:00'
    try:
        dtm = datetime.strptime(str_dtm, '%Y-%m-%d %H:%M')
        if dtm.weekday() == 4:
            dtm += timedelta(hours=60)
            result = f"В это время кредит оформить нельзя, т.к. это пятница. Приходите в {datetime.strftime(dtm, '%Y-%m-%d %H:%M')}"
        elif dtm.weekday() >= 5:
            result = f"Это будет выходной день, банк работать не будет!"
        else:
            result = 'Хорошо! В это время можно будет оформить кредит.'
    except Exception as ex:
        print(ex)
        result = 'Вы ввели неверный формат даты'

    return result

print(credit())