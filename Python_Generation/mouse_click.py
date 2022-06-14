import pyautogui as pag

def move_and_click(x,y):
    pag.moveTo(x, y, 0.1)
    pag.click()
def close_all():
    move_and_click(1336, 158)
    move_and_click(883, 192)
    move_and_click(1138, 161)
    move_and_click(611, 191)
    move_and_click(854, 165)

def active_all():
    move_and_click(778,190)
    move_and_click(1069, 190)
    move_and_click(1267, 190)

a = 0
while a < 10:
    active_all()
    pag.moveTo(1313, 163, 1)
    close_all()
    pag.moveTo(1313, 163, 1)
    a += 1



# a = 0
# while a < 5:
#     print(pag.size())
#     pag.moveTo(1233, 188, 1)
#     pag.click()  # щелчок мыши
#     pag.moveTo(1313, 163, 5)
#     pag.click()  # щелчок мыши
#     # pag.moveTo(1521, 277, 2)
#     # pag.click()    #  щелчок мыши
#     # pag.typewrite("2")
#     # pag.click(x=100, y=200)  # перемещение на 100, 200, а затем нажатие левой кнопкой
#     a += 1
#
# #pag.click(button='right')  # щелчок правой кнопкой мыши
