""">>> 2.1 Блок подсчета процентного перевеса четных тиков над нечетными и наоборот"""

# создадим простой генератор тиков

import time
import random
from collections import Counter
ticks_list = []
signal = 0
percent_over = None
percent_odd = None
CHECK_SIGN = None
with open("result.txt", "w") as file:
    file.write("")
while True:
    # здесь еще есть память о результате предыдущего сигнала сигнале
    # если сигнал был "up 1" : CHECK_SIGN = UP_1
    # если сигнал был "up 2" : CHECK_SIGN = UP_2
    # если сигнал был "down 1" : CHECK_SIGN = DOWN_1
    # если сигнал был "down 2" : CHECK_SIGN = DOWN_2
    # если сигнал был "wait signal" : CHECK_SIGN = None
    time.sleep(1)
    with open("click_direction.txt", "w") as file:
        file.write("wait signal")
    r_n = random.randint(0, 1)  # r_n - random number
    ticks_list.append(r_n)
    last_25 = ticks_list[-25:]
    print(last_25)
    c = Counter(last_25)
    if c[0] != 0 and c[1] != 0:
        percent_over = int(c[0]*100/(c[1] + c[0]))
        percent_odd = 100 - percent_over
        #print(f"{c}-----{c[0]}----{c[1]}----{percent_over}%----{percent_odd}%")

    ### Paterns ### last_25[] last_25[] last_25[] last_25[]

    if len(last_25) >= 25:
        if last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 1:
            signal = 1
            #print("UP 1")
        elif last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 0:
            signal = -1
            #print("DOWN 1")
        elif last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 0:
            signal = 2
            #print("UP 2")
        elif last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 1:
            signal = -2
            #print("DOWN 2")
######################### CHECK MODULE ###################################################
        if CHECK_SIGN == "UP 1":
            if last_25[-4] == 1 and last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 1:
                with open("result.txt", "a+") as file:
                    file.write("+")
            else:
                with open("result.txt", "a+") as file:
                    file.write("-")

        if CHECK_SIGN == "UP 2":
            if last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 1:
                with open("result.txt", "a+") as file:
                    file.write("+")
            else:
                with open("result.txt", "a+") as file:
                    file.write("-")

        if CHECK_SIGN == "DOWN 1":
            if last_25[-4] == 0 and last_25[-3] == 0 and last_25[-2] == 1 and last_25[-1] == 0:
                with open("result.txt", "a+") as file:
                    file.write("+")
            else:
                with open("result.txt", "a+") as file:
                    file.write("-")

        if CHECK_SIGN == "DOWN 2":
            if last_25[-3] == 1 and last_25[-2] == 0 and last_25[-1] == 0:
                with open("result.txt", "a+") as file:
                    file.write("+")
            else:
                with open("result.txt", "a+") as file:
                    file.write("-")

######################### END CHECK MODULE #################################################



        if signal == 1 and (last_25[-3] == 1 and last_25[-2] == 1 and last_25[-1] == 0) and percent_over > 53:
            CHECK_SIGN = "UP 1"
            with open("click_direction.txt", "w") as file:
                file.write("up")
            print("UP 1") # то следующим этапом нужно проверить был ли плюс или его не было и записать результат в отдельный файл
        elif signal == -1 and (last_25[-3] == 0 and last_25[-2] == 0 and last_25[-1] == 1) and percent_odd > 53:
            CHECK_SIGN = "DOWN 1"
            with open("click_direction.txt", "w") as file:
                file.write("down")
            print("DOWN 1")
        elif signal == 2 and (last_25[-2] == 0 and last_25[-1] == 1) and percent_over > 53:
            CHECK_SIGN = "UP 2"
            with open("click_direction.txt", "w") as file:
                file.write("up")
            print("UP 2")
        elif signal == -2 and (last_25[-2] == 1 and last_25[-1] == 0) and percent_odd > 53:
            CHECK_SIGN = "DOWN 2"
            with open("click_direction.txt", "w") as file:
                file.write("down")
            print("DOWN 2")
    print(f"signal = {signal}, percent_over = {percent_over}%, percent_odd = {percent_odd}%")



#########
