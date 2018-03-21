import time
import RPi.GPIO as GPIO
import urllib2

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN) # for light sensor
GPIO.setup(13,GPIO.IN) # for methan gaz sensor
GPIO.setup(15,GPIO.OUT) # for light relay
GPIO.setup(16,GPIO.OUT) # for motor vibration relay

man = "Fadi"
url = "http://mahdi.massejli.com/telegram/?" # Massejli API service from codnloc.com 
safe_zone_notify = True # to prevent loop notify in the safe zone

def danger_alert(alert=True):
        "this function to vibrate the motor and the fire man know about the danger zone"

        if(alert==True):
                x=0
                while (x<5): # to prevent continues vibration, its vibrate 5 times only
                        GPIO.output(16,1) #vibrate
                        time.sleep(0.1)
                        GPIO.output(16,0) #stop vibrate
                        time.sleep(1)
                        x=x+1
                GPIO.output(16,0)
                        
        else:
                GPIO.output(16,0)#stop vibrate
        return;        

while True:
        
    if(GPIO.input(13)==False):
        print time.strftime("%c")+" : There is a GAZ here, Danger!"
        safe_zone_notify = True
		danger_alert(True)
 		url_responce = urllib2.urlopen(url + "man=" + man + "&danger=1")
	else:
            if(safe_zone_notify == True and GPIO.input(13)==True):
                print time.strftime("%c")+" : its now safe"
                danger_alert(False)
                safe_zone_notify = False
                url_responce = urllib2.urlopen(url+ "man=" + man)
                
        
	if(GPIO.input(11)==True):
		print time.strftime("%c")+" : There is a dark here, we well light !"
		GPIO.output(15,1)
	else:
		#print "its Sunny"
        GPIO.output(15,0)

        
	time.sleep(3)









