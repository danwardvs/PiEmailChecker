
import RPi.GPIO as GPIO, feedparser, time, os.path

USERNAME = "username"   
PASSWORD = "password"     

GPIO.setmode(GPIO.BCM)
LIGHTS = 18
GPIO.setup(LIGHTS, GPIO.OUT)

while True:

        cur_mails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
       
        print("You have: ")
        print(cur_mails)
        print(" emails in your inbox.")

        if os.path.isfile("emails.txt") == False: #create the file if it doesnt exist
                f = open('emails.txt', 'w')
                f.write('1'); #The interpreter doesn't like reading from an empty file
                f.close

        f = open('emails.txt', 'r')
        last_mails = int(f.read())
        f.close()

        print("Last known number of emails: ")
        print(last_mails)

        if  cur_mails < last_mails:
            last_mails = cur_mails
            f = open('emails.txt', 'w')
            f.write(str(last_mails))

        if  cur_mails > last_mails:
            last_mails = cur_mails
            f = open('emails.txt', 'w')
            f.write(str(last_mails))

            GPIO.output(LIGHTS, True) #flash the leds a couple times
            time.sleep(0.4) #in seconds
            GPIO.output(LIGHTS, False)
            time.sleep(0.1)
            GPIO.output(LIGHTS, True)
            time.sleep(0.4)
            GPIO.output(LIGHTS, False)

        f.close()
        time.sleep(60)
