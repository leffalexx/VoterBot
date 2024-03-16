from datetime import datetime


def randomizer():
    result = int(str(datetime.now())[-1])
    if 0 <= result < 3:
        return (f'🦄 Даванков\n "Закончим сво но нА НаШиХ уСлОвИяХ ))0)"')
    elif 3 <= result < 6:
        return (f'👹 Харитонов \n "Поиграли в капитализм и хватит"')
    elif 6 <= result < 7:
        return (f'🔞 Слуцкий \n "Одна страна, один президент, одна победа"')
    else:
        return(f'Всех черкай 🦄👹🔞 ')


if __name__ == '__main__':
    print(randomizer())
