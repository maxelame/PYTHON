import pyautogui as pag
import traceback
import time

'''правление клавиатурой

Примечание: инструкции в данном разделе основаны на документации PyAutoGUI и содержат несколько примеров из нее.

typewrite() — самая главная команда для управления клавиатурой.

Например:

pag.typewrite("Hello world!")

Этот фрагмент кода работает, как при написании «Hello world!» вручную, однако выполняется без нажатия клавиш. Очень удобно!

Чтобы добавить задержку между нажатиями клавиш, можно использовать следующую команду:

pag.typewrite('Hello world!', interval=0.25)

Она печатает каждый символ с интервалом в четверть секунды.

Примечание: с помощью этой функции можно печатать только сообщения. Внутри функции typewrite() невозможно нажать enter или использовать shift. Список клавиш клавиатуры

Ниже приведен список клавиш клавиатуры, которые можно передать функциям press(), keyUp(), keyDown() или hotkey():

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', 
'+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
':', ';', '<', '=', '>', '?', '@', '[', '\', ']', '^', '_', '`', 'a', 'b', 
'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 
'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 
'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 
'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 
'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 
'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 
'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 
'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 
'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 
'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 
'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 
'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 
'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 
'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 
'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 
'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 
'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 
'optionleft', 'optionright']

Функции keyDown() и keyUp() имитируют нажатие и отпускание клавиши. Например:

pag.keyDown("enter")
pag.keyUp("enter")

Этот фрагмент кода нажимает и отпускает клавишу enter. Будьте осторожны и никогда не оставляйте клавишу нажатой 🙂

Функция press() объединяет две предыдущих. Клавиша, передаваемая функции, нажата и отпущена:

pag.press("enter")

Два предыдущих фрагмента кода выдают одинаковый результат!

Чтобы нажать несколько клавиш, аргументы передаются в виде списка:

pag.press(['enter', 'tab', 'enter'])

Последняя функция клавиатуры — это hotkey(), упрощающая использование сочетаний клавиш. Просто передайте ей несколько клавиш, которые будут нажаты по порядку, а затем отпущены в обратном порядке. Например:

pag.hotkey('ctrl', 'alt', 'delete')

Эквивалентно следующему коду:

pag.keyDown('ctrl')
pag.keyDown('alt')
pag.keyDown('delete')
pag.keyUp('delete')
pag.keyUp('alt')
pag.keyUp('ctrl')
'''

def new_stake(window,stake):   # window - кортеж из двух значений координат (x и y) это координаты кнопки закрыть ставку, ставку вводить в формате 3.56 (через точку)
    pag.moveTo(window[0] - 301, window[1] + 94, 0.2)
    pag.click()
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.press("backspace")
    pag.typewrite(str(stake))
    time.sleep(1)
#
window_1 = (856, 163)
window_2 = (1147, 163)
window_3 = (1344, 161)
window_4 = (857, 392)
window_5 = (1147, 392)
window_6 = (1345, 392)
window_7 = (856, 575)
window_8 = (1148, 573)
window_9 = (1341, 573)

# print(window_1[0])

def click_up(window): # на вход подаем кортеж из двух значений
    print(pag.size())
    pag.moveTo(window[0] - 72, window[1] + 26, 0.2)
    pag.click()  # щелчок мыши
    time.sleep(4)
    pag.moveTo(window[0], window[1], 0.2)
    pag.click()  # щелчок мыши
    pag.moveTo(window[0]-463, window[1]+3, 0.2)
    time.sleep(1)



def click_down(window): # на вход подаем кортеж из двух значений
    print(pag.size())
    pag.moveTo(window[0] - 76, window[1] + 109, 0.2)
    pag.click()  # щелчок мыши
    time.sleep(4)
    pag.moveTo(window[0], window[1], 0.2)
    pag.click()  # щелчок мыши
    pag.moveTo(window[0]-463, window[1]+3, 0.2)
    time.sleep(1)

# click_up(window_2)
# click_down(window_2)
# new_stake(window_2, 1.23)
# click_up(window_2)
# click_down(window_2)
# new_stake(window_2, 2.46)
# click_up(window_2)
# click_down(window_2)
# new_stake(window_2, 3.69)

# def click_up():
#     print(pag.size())
#     pag.moveTo(1233, 188, 0.2)
#     pag.click()  # щелчок мыши
#     time.sleep(4)
#     pag.moveTo(1313, 163, 0.2)
#     pag.click()  # щелчок мыши
# def click_down():
#     print(pag.size())
#     pag.moveTo(1220, 270, 0.2)
#     pag.click()  # щелчок мыши
#     time.sleep(4)
#     pag.moveTo(1313, 163, 0.2)
#     pag.click()  # щелчок мыши
#
#
while True:
    try:
        time.sleep(0.5)
        with open('click_direction.txt') as fd:
            direction = fd.read()
            if direction == "up":
                click_up(window_2)
            elif direction == "down":
                click_down(window_2)
    except Exception:
        print(traceback.format_exc())
