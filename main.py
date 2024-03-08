from gpiozero import Button
import moviepy

#Relay Activated Auto Recording
#This program will start recording when Pin 11 GPIO 17 is grounded.
#This can be activated with a relay.

#Trigger
button = Button(17)
button.wait_for_press()
print("The button was pressed!")


#Record



#Logo Embeding




#Raspberry Pi Nas