print("Джонни мать его Сильверхенд: привет, Ви. Чего тебе?")

while True:
    answer = input("Ви: ").lower()

    if "привет" in answer:
        print("Джонни: Привет, Ви. Давно не виделись.")

    elif "как дела" in answer:
        print("Джонни: Всё также. Ненависть к корпоратам и желание покурить.")

    elif "паша техник" in answer:
        print("Джонни: Конечно блять знаю, это мой пахан.")

    elif "ссылку" in answer and "паша" in answer:
        print("Джонни: Держи: https://vt.tiktok.com/ZSVoFd5Pb/")

    elif "лето" in answer and "не учусь" in answer:
        print("Джонни: Вот это я понимаю. Теперь больше свободного времени, чтобы дальше нихуя не делать.")

    elif "пока" in answer:
        print("Джонни: Давай, Ви.")
        break

    else:
        print("Джонни: Что ты блять несёшь?")