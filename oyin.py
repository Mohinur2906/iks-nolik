from random import choice


def bosh_doska_hosil_qil():
    """3x3 doska yaratadi: 1 dan 9 gacha raqamlar bilan."""
    doska = []
    raqam = 1
    for i in range(3):
        qator = []
        for j in range(3):
            qator.append(raqam)
            raqam += 1
        doska.append(qator)
    return doska


def doskani_korsat(doska):
    """Doskani misoldagi ko'rinishda chiqaradi."""
    chiziq = "+-------+-------+-------+"
    bosh = "|       |       |       |"
    for qator in doska:
        print(chiziq)
        print(bosh)
        print("|   {}   |   {}   |   {}   |".format(qator[0], qator[1], qator[2]))
        print(bosh)
    print(chiziq)


def bosh_maydonlar(doska):
    """Hali X yoki O qo'yilmagan raqamlar ro'yxatini qaytaradi."""
    bosh = []
    for qator in doska:
        for element in qator:
            if element != "X" and element != "O":
                bosh.append(element)
    return bosh


def foydalanuvchi_tanlasin(doska):
    """Foydalanuvchidan to'g'ri raqam so'raydi va doskaga O qo'yadi."""
    while True:
        javob = input("Sizni galingiz: ")

        try:
            raqam = int(javob)
        except ValueError:
            print("Iltimos, butun son kiriting!")
            continue

        if raqam < 1 or raqam > 9:
            print("Raqam 1 dan 9 gacha bo'lishi kerak!")
            continue

        if raqam not in bosh_maydonlar(doska):
            print("Bu maydon band, boshqasini tanlang!")
            continue

        qator = (raqam - 1) // 3
        ustun = (raqam - 1) % 3
        doska[qator][ustun] = "O"
        break


def golib_bormi(doska, belgi):
    """Berilgan belgi (X yoki O) yutganmi, tekshiradi."""
    for i in range(3):
        if doska[i][0] == doska[i][1] == doska[i][2] == belgi:
            return True
        if doska[0][i] == doska[1][i] == doska[2][i] == belgi:
            return True
    if doska[0][0] == doska[1][1] == doska[2][2] == belgi:
        return True
    if doska[0][2] == doska[1][1] == doska[2][0] == belgi:
        return True
    return False


def kompyuter_tanlasin(doska):
    """Kompyuter bo'sh maydonlardan tasodifiy birini tanlab X qo'yadi."""
    raqam = choice(bosh_maydonlar(doska))
    qator = (raqam - 1) // 3
    ustun = (raqam - 1) % 3
    doska[qator][ustun] = "X"


# ---------------- ASOSIY DASTUR ----------------
doska = bosh_doska_hosil_qil()
doska[1][1] = "X"
doskani_korsat(doska)

while True:
    foydalanuvchi_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, "O"):
        print("Yutdingiz!")
        break
    if not bosh_maydonlar(doska):
        print("Durang!")
        break

    kompyuter_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, "X"):
        print("Kompyuter yutdi!")
        break
    if not bosh_maydonlar(doska):
        print("Durang!")
        break