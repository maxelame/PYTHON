import pyautogui as pag

def new_stavka(a):
    pag.moveTo(1233, 188, 0.5)
    pag.click()
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.typewrite(a, interval=0.25)

new_stavka("7.45")
new_stavka("5.t5")
new_stavka("0.35")
new_stavka("8.11")


# a =
# while a < 1:
#     print(pag.size())
#     pag.moveTo(1233, 188, 0.5)
#     pag.click()  # щелчок мыши
#     pag.moveTo(1313, 163, 5)
#     pag.click()  # щелчок мыши
#     # pag.moveTo(1521, 277, 2)
#     # pag.click()    #  щелчок мыши
#     # pag.typewrite("2")
#     # pag.click(x=100, y=200)  # перемещение на 100, 200, а затем нажатие левой кнопкой
#     a += 1

#pag.click(button='right')  # щелчок правой кнопкой мыши
