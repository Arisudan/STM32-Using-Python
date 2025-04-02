import pyb
import time
  
while true:

	pyb.LED(1).on()   
	time.sleep(1)   
	pyb.LED(1).off() 

	pyb.LED(4).on()  
	time.sleep(1)
	pyb.LED(4).off()

	pyb.LED(2).on()   
	time.sleep(1)
	pyb.LED(2).off()  

	pyb.LED(3).on()  
	time.sleep(1)
	pyb.LED(3).off()  

	pyb.LED(2).on()  
	time.sleep(1)
	pyb.LED(2).off()

	pyb.LED(4).on()   
	time.sleep(1)
	pyb.LED(4).off()  

	pyb.LED(1).on()  
	time.sleep(1)
	pyb.LED(1).off()

	pyb.LED(3).on()   
	time.sleep(1)
	pyb.LED(3).off() 
	pyb.LED(3).off() 
