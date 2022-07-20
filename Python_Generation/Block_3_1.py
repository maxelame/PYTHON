""">>> 2.1 Блок подсчета процентного перевеса четных тиков над нечетными и наоборот"""

# создадим простой генератор тиков

import time
import random
from collections import Counter
import time
import traceback
import winsound
import matplotlib.pyplot as plt
import pyautogui as pag
import matplotlib.animation as animation

#######################
def sound_up():
    frequency = 1400  # Set Frequency To 2500 Hertz
    duration = 80  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def sound_down():
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 80  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def click_up():
    print(pag.size())
    pag.moveTo(1233, 188, 0.5)
    pag.click()  # щелчок мыши
    pag.moveTo(1313, 163, 5)
    pag.click()  # щелчок мыши


def click_down():
    print(pag.size())
    pag.moveTo(1220, 270, 0.5)
    pag.click()  # щелчок мыши
    pag.moveTo(1313, 163, 5)
    pag.click()  # щелчок мыши

def condition_1():
    if len(last_25) >= 25:
        if percent_over >= 68:
            flag = "+ON"
        if flag == "+ON" and last_25[-2] == 0 and last_25[-1] == 0:
            print("+")
            flag = "OFF"
        elif flag == "+ON" and last_25[-2] == 0 and last_25[-1] == 1:
            print("-")
        if percent_odd >= 68:
            flag = "-ON"
        if flag == "-ON" and last_25[-2] == 1 and last_25[-1] == 1:
            print("+")
            flag = "OFF"
        elif flag == "-ON" and last_25[-2] == 1 and last_25[-1] == 0:
            print("-")

ticks_list = []
signal = 0
percent_over = None
percent_odd = None
CHECK_SIGN = None
flag = None
line_1 = 0
predict_len_ticks_list = 0
while True:
    try:
        time.sleep(0.01)
        with open('Ticks_1\R_50.dat') as fd:
                lines = fd.read().split("&")
                digit = int(str(int(float(lines[4])*100000))[-2])
                if line_1 != lines[4]:
                    #print(lines[0], lines[4], digit, sep= '---')
                    line_1 = lines[4]
                    if digit % 2 == 0:
                        direction = 1
                        #sound_up()
                        ticks_list.append(direction)
                        #condition_1() # сюда поставить функцию проверки условия
                    else:
                        direction = 0
                        #sound_down()
                        ticks_list.append(direction)
                        #condition_1()  # сюда поставить функцию проверки условия
        # with open("result.txt", "w") as file:
        #     file.write("")
        #     # здесь еще есть память о результате предыдущего сигнала сигнале
        #     # если сигнал был "up 1" : CHECK_SIGN = UP_1
        #     # если сигнал был "up 2" : CHECK_SIGN = UP_2
        #     # если сигнал был "down 1" : CHECK_SIGN = DOWN_1
        #     # если сигнал был "down 2" : CHECK_SIGN = DOWN_2
        #     # если сигнал был "wait signal" : CHECK_SIGN = None
        # with open("click_direction.txt", "w") as file:
        #     file.write("wait signal")
        #     ####

            #r_n = random.randint(0, 1)  # r_n - random number

            #####
        #ticks_list.append(direction)
        last_25 = ticks_list[-25:]
        #print(last_25)
        c = Counter(last_25)
        if c[0] != 0 and c[1] != 0:
            percent_odd = int(c[0] * 100 / (c[1] + c[0]))
            percent_over = 100 - percent_odd
            #print(f"{c}-----{c[0]}----{c[1]}----{percent_over}%----{percent_odd}%")

            ### Paterns ### last_25[] last_25[] last_25[] last_25[]


        if len(last_25) >= 25 and len(ticks_list) != predict_len_ticks_list:
            if percent_over >= 68:
                flag = "+ON"
            if percent_odd >= 68:
                flag = "-ON"

            if flag == "+ON" and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 0:
                print("+", flag)
                flag = "OFF"
            elif flag == "+ON" and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 1:
                print("-", flag)

            if flag == "-ON" and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 1:
                print("+", flag)
                flag = "OFF"
            elif flag == "-ON" and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 0:
                print("-", flag)
            predict_len_ticks_list = len(ticks_list)




        # if len(last_25) >= 25:
        #     if last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 1:
        #         signal = 1
        #             # print("UP 1")
        #     elif last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 0:
        #         signal = -1
        #             # print("DOWN 1")
        #     elif last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 0:
        #         signal = 2
        #             # print("UP 2")
        #     elif last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 1:
        #         signal = -2
        #             # print("DOWN 2")
        #         ######################### CHECK MODULE ###################################################
        #     if CHECK_SIGN == "UP 1":
        #         if last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 1:
        #             with open("result.txt", "a+") as file:
        #                 file.write("+")
        #         else:
        #             with open("result.txt", "a+") as file:
        #                 file.write("-")
        #
        #     if CHECK_SIGN == "UP 2":
        #         if last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 1:
        #             with open("result.txt", "a+") as file:
        #                 file.write("+")
        #         else:
        #             with open("result.txt", "a+") as file:
        #                 file.write("-")
        #
        #     if CHECK_SIGN == "DOWN 1":
        #         if last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 0:
        #             with open("result.txt", "a+") as file:
        #                 file.write("+")
        #         else:
        #             with open("result.txt", "a+") as file:
        #                 file.write("-")
        #
        #     if CHECK_SIGN == "DOWN 2":
        #         if last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 0:
        #             with open("result.txt", "a+") as file:
        #                 file.write("+")
        #         else:
        #             with open("result.txt", "a+") as file:
        #                 file.write("-")
        #
        #         ######################### END CHECK MODULE #################################################
        #
        #     if signal == 1 and (last_25[-3] == 1 and last_25[-2] == 1 and last_25[-1] == 0) and percent_over > 53:
        #         CHECK_SIGN = "UP 1"
        #         with open("click_direction.txt", "w") as file:
        #             file.write("up")
        #         print("UP 1")  # то следующим этапом нужно проверить был ли плюс или его не было и записать результат в отдельный файл
        #     elif signal == -1 and (last_25[-3] == 0 and last_25[-2] == 0 and last_25[-1] == 1) and percent_odd > 53:
        #         CHECK_SIGN = "DOWN 1"
        #         with open("click_direction.txt", "w") as file:
        #             file.write("down")
        #         print("DOWN 1")
        #     elif signal == 2 and (last_25[-2] == 0 and last_25[-1] == 1) and percent_over > 53:
        #         CHECK_SIGN = "UP 2"
        #         with open("click_direction.txt", "w") as file:
        #             file.write("up")
        #         print("UP 2")
        #     elif signal == -2 and (last_25[-2] == 1 and last_25[-1] == 0) and percent_odd > 53:
        #         CHECK_SIGN = "DOWN 2"
        #         with open("click_direction.txt", "w") as file:
        #             file.write("down")
        #         print("DOWN 2")
        #print(f"signal = {signal}, percent_over = {percent_over}%, percent_odd = {percent_odd}%")
    except Exception:
        print(traceback.format_exc())














#########
