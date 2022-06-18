import time
import traceback
import winsound
import matplotlib.pyplot as plt
import pyautogui as pag
import matplotlib.animation as animation
previous_ticks = 0
s = 1000
counter = 0
li =[]
string1 = ""
result = ""
result1 = ""
stock_file = open("stock.txt", "w")
stock_file.close()


######## GRAPHIC ########

plt.style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#######################
def sound_up():
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 60  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def sound_down():
    frequency = 700  # Set Frequency To 2500 Hertz
    duration = 60  # Set Duration To 1000 ms == 1 second
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


while counter < 1000:
    # ani = animation.FuncAnimation(fig, animate, interval=100)
    # plt.show()
    try:
        time.sleep(0.01)
        with open('Ticks_1\R_50.dat') as fd:
                lines = fd.read().split("&")
                digit = int(float(lines[4])*10000)
                if digit != previous_ticks:
                        if digit % 2 == 0: # Если число оканчивается на четное
                                direction = 1 # Записываем 1
                                sound_up()
                        else:
                            direction = 0 # Если число оканчивается на нечетное записываем 0
                            sound_down()

                        previous_ticks = digit
                        counter +=1
                        s += direction
                        li.append(s)
                        string1 += str(direction)
                        str_to_thr_stock = str(counter) + "," + str(s) +"\n"
                        stock_file = open("stock.txt", "a+")
                        stock_file.write(str_to_thr_stock)
                        stock_file.close()

                        if len(string1) >=5:
                            if (string1[-3] == "1" and string1[-2] == "1") and direction == 1 :
                                stock_file = open("click_direction.txt", "w")
                                stock_file.write("up")
                                stock_file.close()
                                # click_up()
                            elif (string1[-3] == "0" and string1[-2] == "0" and direction == 0):
                                stock_file = open("click_direction.txt", "w")
                                stock_file.write("down")
                                stock_file.close()
                                # click_down()
                            else:
                                stock_file = open("click_direction.txt", "w")
                                stock_file.write("wait")
                                stock_file.close()
                                # click_down()

                        if len(string1) >=5:
                            if (string1[-4] == "1" and string1[-3] == "1" and string1[-2] == "1" and string1[-1] == "1") or (string1[-4] == "0" and string1[-3] == "0" and string1[-2] == "0" and string1[-1] == "0"):

                                result +="+"
                                print(result)
                                # print(result1)
                                # winrate_plus = result.count("+")
                                # winrate_minus = result.count("-")
                                                #winrate = float(result.count("+")*0,95  - result.count("-"))*100/len(result)
                                # print(f'Плюсов =  {result.count("+")}    Минусов=  {result.count("-")}')
                            elif (string1[-3] == "1" and string1[-3] == "1" and string1[-2] == "1" and string1[-1] == "0") or (string1[-4] == "0" and string1[-3] == "0" and string1[-2] == "0" and string1[-1] == "1"):

                                result +="-"
                                print(result)
                                # print(result1)
                                # winrate_plus = result.count("+")
                                # winrate_minus = result.count("-")
                                                #winrate = float(result.count("+")*0,95  - result.count("-"))*100/len(result)
                                # print(f'Плюсов =  {result.count("+")}    Минусов=  {result.count("-")}')

    except Exception:
        print(traceback.format_exc())

print(li)
print(string1)
print("".join(str(li)))
print(string1[-3],string1[-2],string1[-1])
new_ticks_file = open("new_ticks.txt", "w")
new_ticks_file.write(string1)
new_ticks_file.close()
