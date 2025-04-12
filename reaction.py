from gpiozero import LED, Button
from time import sleep
from random import uniform
import time

led = LED(4)
right_button = Button(15)
left_button = Button(14)
left_name = input('left player name is ')
right_name = input('right player name is ')
left_points = 0
right_points = 0
def pressed(button):
    global left_points,right_points
    if button.pin.number == 14:
        print(left_name + ' won the game.')
        left_points =left_points +1
    elif button.pin.number == 15:
        print(right_name + ' won the game.')
        right_points = right_points +1


    right_button.when_pressed = None
    left_button.when_pressed = None


def scanner():
    while (True):
        right_button.wait_for_press(timeout=0.1)
        left_button.wait_for_press(timeout=0.1)
        if (left_button.is_pressed):
            break
        if (right_button.is_pressed):
            break

while (True):
    led.on()
    sleep(uniform(5, 10))
    led.off()
    start_time = time.time()
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    scanner()
    end_time = time.time()
    time_used = end_time - start_time
    print(f"takes {time_used} s")
    temp = input("Do you want to continue?(y/n)")
    if (temp == 'n' or temp == 'no'):
        print(f'{left_name} player win {left_points} score,{right_name} player {right_points} score. ')
        exit()
