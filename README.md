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
1. Visit the official [MicroPython website](https://micropython.org/download/STM32F4DISC/)
2. Download the **latest stable MicroPython firmware** for STM32F407 (usually in **.hex format**).  

---

### **Step 2: Flash MicroPython to STM32F407**  

1. Visit the official [STM32CubeProgrammer Website](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Download the Software according to you System Requirements (Windows/Linux/Mac)
3. Open **STM32CubeProgrammer** and connect the STM32 board.  
4. Select the correct **ST-Link Interface**.  
5. Click **"Open File"**, browse for the downloaded **MicroPython .hex file**, and select it.  
6. Click **"Download"** to flash MicroPython to the STM32 board.  
7. Once the process completes, restart the board.  

---

### **Step 3: Open Serial Communication**  
1. **Install Tera Term** (if not installed already).  
2. Open **Tera Term** and select the correct **COM port**.  
3. Set the **Baud rate** to **115200**.  
4. Click **"OK"** to establish a connection.  
5. Press **Enter**, and you should see a `>>>` MicroPython REPL prompt.  

---

### **Step 4: LED Blinking with MicroPython**  
Save the following script as `led_blink1.py` and run it on the STM32 board.  

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

# **STM32 F411RE LED Blinking using MicroPython**  

## **Overview**  
This project demonstrates how to set up **MicroPython** on an **STM32 F411RE** microcontroller and execute a basic **LED blinking program** using Python. The tutorial includes steps to **flash MicroPython**, **set up serial communication**, and **run the code**.  

---

## **Hardware Requirements**  

- **STM32F411RE Nucleo Board**  
- **ST-Link V2 (if required for flashing)**  
- **Micro-USB cable** for power and communication  

---

## **Software Requirements**  

- **STM32CubeProgrammer** (for flashing the MicroPython firmware)  
- **MicroPython firmware (.hex file) for STM32**  
- **Tera Term** (for serial communication)  

---

## **Step-by-Step Instructions**  

### **Step 1: Download MicroPython for STM32**  

- Visit the official [MicroPython website](https://micropython.org/download/NUCLEO_F411RE/)  
- Download the **latest stable MicroPython firmware** for **STM32F411RE** (usually in **.hex format**).  

---

### **Step 2: Flash MicroPython to STM32F411RE**  

- Visit the official [STM32CubeProgrammer Website](https://www.st.com/en/development-tools/stm32cubeprog.html)  
- Download the software according to your **system requirements** (Windows/Linux/Mac).  
- Open **STM32CubeProgrammer** and connect the STM32 board.  
- Select the correct **ST-Link Interface**.  
- Click **"Open File"**, browse for the downloaded **MicroPython .hex file**, and select it.  
- Click **"Download"** to flash MicroPython to the STM32 board.  
- Once the process completes, restart the board.  

---

### **Step 3: Open Serial Communication**  

- Install **Tera Term** (if not installed already).  
- Open **Tera Term** and select the correct **COM port**.  
- Set the **Baud rate** to **115200**.  
- Click **"OK"** to establish a connection.  
- Press **Enter**, and you should see a `>>>` MicroPython REPL prompt.  

---

### **Step 4: LED Blinking with MicroPython**  

Since the **STM32F411RE** board has only **one onboard LED**, we will use **LED1**, which is connected to **pin PA5**.  

Save the following script as `led_blink.py` and run it on the STM32 board.  

```python
import machine
import time

led = machine.Pin("PA5", machine.Pin.OUT)  # Define PA5 as an output pin

while True:
    led.on()   # Turn LED on
    time.sleep(1)  # Wait for 1 second
    led.off()  # Turn LED off
    time.sleep(1)  # Wait for 1 second
```

---

### **Step 5: Running the Script**  

- Open **Tera Term** and connect to the STM32 board.  
- Enter `>>>` to access the **MicroPython REPL**.  
- Type:  

  ```python
  exec(open("led_blink1.py").read())  
  ```  

  (or) **right-click** and select **"Paste"**, then press **Enter**.  

  This will execute the script and blink the **onboard LED** in a loop.  

---

## **Expected Output**  

- The **onboard LED (PA5)** will **blink ON and OFF every 1 second**.  
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

This project successfully sets up **MicroPython** on **STM32F411RE** and demonstrates a **basic LED blinking program** using Python. With MicroPython, STM32 boards can be programmed **quickly and easily** without needing traditional **C-based** firmware development.  

---
