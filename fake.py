import os, pty, serial, time

master, slave = pty.openpty()
s_name = os.ttyname(slave)

ser = serial.Serial(s_name)

while True:
    ser.write('askldjf')
    time.sleep(1)