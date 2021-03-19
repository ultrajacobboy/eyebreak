from plyer import notification
import time
notifcation_count = (0)
def eyebreak():
    delay=(float(minutes)*60)
    while True:
        global notifcation_count
        notifcation_count=notifcation_count+1
        if(notifcation_count==1):
            notification.notify(title='Eye Break', message='Eye Break has been activated.', app_icon=None, timeout=1)
            print("Eye Break is active." )
            print("We will send you a notifcation every", minutes, "minutes  when it is time for an eye break!")
            print("If you want to stop Eye Break, close this window.")
        else:
            notification.notify(title='Eye Break', message='Time for an eye break! Look at a faraway wall for 20 seconds!', app_icon=None, timeout=20)
        time.sleep(delay)
print('''Eye Break 
Made by Jacob 2021''')
minutes = input("How long of a delay in minutes do you want in between each eye break (recommended is 20 minutes)?:")
if(float(minutes) < 1):
    warning=input("WARNING! PUTTING YOUR DELAY LOWER THAN 1 MAY LAG YOUR COMPUTER. DO YOU WISH TO CONTINUE? yes OR no:")
    if(warning=="yes"):
        eyebreak()
    else:
        print("Ok goodbye")
else:
    eyebreak()
        
