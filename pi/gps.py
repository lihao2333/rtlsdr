import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
while True:
    datas = ser.readline().decode()
    datas = datas.strip("\r\n").split(",")
    if datas[0] == "$GNGGA":
        print(datas)
        break
    
