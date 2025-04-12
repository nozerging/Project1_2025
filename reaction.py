from gpiozero import LED,Button
from time import sleep
from random import uniform

led=LED(4)
right_button=Button(15)
left_button=Button(14)
left_name=input('left player name is ')
right_name=input('right player name is ')

def pressed(button):
    if button.pin.number==14:
        print(left_name+' won the game')
    elif button.pin.number==15:
        print(right_name+' won the game')
    right_button.when_pressed=None
    left_button.when_pressed=None
def scanner():
    while(True):
        right_button.wait_for_press(timeout=0.1)
        left_button.wait_for_press(timeout=0.1)
        if(left_button.is_pressed):
            break
        if(right_button.is_pressed):
            break

while(True):
    led.on()
    sleep(uniform(1,2))
    led.off()
    right_button.when_pressed=pressed 
    left_button.when_pressed=pressed
    scanner()
    temp=input("Do you want to continue?(y/n)")
    if(temp=='n' or temp=='no'):
        exit()
