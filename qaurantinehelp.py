#This is different from eyebreak.py because this tells you to stretch as well
from plyer import notification
import time
notifcation_count = (0)
def eyebreak():
    delay=(float(minutes)*60)
    while True:
        global notifcation_count
        notifcation_count=notifcation_count+1
        if(notifcation_count==1):
            notification.notify(title='Quarantine Help', message='Quarantine Help has been activated.', app_icon=None, timeout=1)
            print("Quarantine Help is active." )
            print("We will send you a notifcation every", minutes, "minutes  when it is time for a break!")
            print("If you want to stop Quarantine Help, close this window.")
        else:
            notification.notify(title='Quarantine Help', message='Time for a break! Look away from the screen for at least 20 seconds and if you want, get up and stretch!', app_icon=None, timeout=20)
        time.sleep(delay)
print('''Quarantine Help 
Made by Jacob 2021''')
minutes = input("How long of a delay in minutes do you want in between each break (recommended is 20 minutes)?: ")
if(float(minutes) < 1):
    warning=input("WARNING! PUTTING YOUR DELAY LOWER THAN 1 MAY LAG YOUR COMPUTER. DO YOU WISH TO CONTINUE? yes OR no:")
    if(warning=="yes"):
        eyebreak()
    else:
        print("Ok goodbye")
else:
    eyebreak()
