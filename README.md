# **STM32 F407 LED Blinking using MicroPython**  

## **Overview**  
This project demonstrates how to set up **MicroPython** on an **STM32 F407** microcontroller and execute a basic **LED blinking program** using Python. The tutorial includes steps to **flash MicroPython**, **set up serial communication**, and **run the code**.  

## **Hardware Requirements**  
- **STM32F407** Discovery Board  
- **ST-Link V2 (if required for flashing)**  
- **Micro-USB cable** for power and communication  

## **Software Requirements**  
- **STM32CubeProgrammer** (for flashing the MicroPython firmware)  
- **MicroPython firmware (.hex file) for STM32**  
- **Tera Term** (for serial communication)  

---

## **Step-by-Step Instructions**  

### **Step 1: Download MicroPython for STM32**  
1. Visit the official [MicroPython website](https://micropython.org/download/stm32/)  
2. Download the **latest stable MicroPython firmware** for STM32F407 (usually in **.hex format**).  

---

### **Step 2: Flash MicroPython to STM32F407**  
1. Open **STM32CubeProgrammer** and connect the STM32 board.  
2. Select the correct **ST-Link Interface**.  
3. Click **"Open File"**, browse for the downloaded **MicroPython .hex file**, and select it.  
4. Click **"Download"** to flash MicroPython to the STM32 board.  
5. Once the process completes, restart the board.  

---

### **Step 3: Open Serial Communication**  
1. **Install Tera Term** (if not installed already).  
2. Open **Tera Term** and select the correct **COM port**.  
3. Set the **Baud rate** to **115200**.  
4. Click **"OK"** to establish a connection.  
5. Press **Enter**, and you should see a `>>>` MicroPython REPL prompt.  

---

### **Step 4: LED Blinking with MicroPython**  
Save the following script as `led_blink.py` and run it on the STM32 board.  

```python
import pyb
import time

while True:
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
```

---

### **Step 5: Running the Script**  
1. Open Tera Term and connect to the STM32 board.  
2. Enter `>>>` to access the MicroPython REPL.  
3. Type:  
   ```python
   exec(open("led_blink.py").read()) (or) click the right click of the mouse
   ```
   This will execute the script and blink the **onboard LEDs** in sequence.

---

## **Expected Output**  
- The STM32 **onboard LEDs** (LED1, LED2, LED3, LED4) will blink in a specific order.  
- The loop runs **indefinitely** until manually stopped.  

---

## **Troubleshooting**  

### **1. No Output in Tera Term**  
- Ensure STM32 is **properly connected**.  
- Restart the board and reattempt connection.  
- Select the correct **Baud Rate: 115200**.  

### **2. MicroPython Not Responding**  
- Try pressing **Reset Button** on STM32.  
- Use `CTRL + D` to soft reboot MicroPython.  

### **3. Flashing Issues**  
- Use **STM32CubeProgrammer** to verify the **MicroPython firmware** is correctly written.  
- If flashing fails, check the **ST-Link connection** and retry.  

---

## **Conclusion**  
This project **successfully sets up MicroPython** on STM32F407 and demonstrates a basic **LED blinking program** using **Python**. With MicroPython, STM32 boards can be programmed **quickly and easily** without needing traditional C-based firmware development.  

---
