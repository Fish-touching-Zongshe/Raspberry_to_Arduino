import serial    #import serial module
ser = serial.Serial("/dev/ttyACM0", 9600,timeout=1);   #open named port at 9600,1s timeot
print("Open door.")
while True:
    send = 'o'  # 发送给arduino的数据
    ser.write(send.encode())
    str = ser.readline().decode()  # 获取arduino发送的数据
    if(str != ""):
        print(str)
        if(str == "Close."): # 发送一次便退出
            print("Door Closed!")
            break

ser.close()
