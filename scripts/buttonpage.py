import socket
import machine
import time


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>LED ON/OFF</title> </head>
<form>
<table border ="1">
<tr>
<td bgcolor="red">RED</td>
<td><button name="LED" value="ON0" type="submit">On</button></td>
<td><button name="LED" value="OFF0" type="submit">Off</button></td>
</tr>
<tr>
<td bgcolor="orange">ORANGE</td>
<td><button name="LED" value="ON2" type="submit">On</button></td>
<td><button name="LED" value="OFF2" type="submit">Off</button></td>
</tr>
<tr>
<td bgcolor="blue">BLUE</td>
<td><button name="LED" value="ON3" type="submit">On</button></td>
<td><button name="LED" value="OFF3" type="submit">Off</button></td>
</tr>
</table>
</form>
</html>
"""

#Setup PINS
LED0 = machine.Pin(16, machine.Pin.OUT)
LED2 = machine.Pin(14, machine.Pin.OUT)
LED3 = machine.Pin(13, machine.Pin.OUT)
LED0.off()
LED2.off()
LED3.off()

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
        conn, addr = s.accept()
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        print("Content = %s" % str(request))
        request = str(request)
        LEDON0 = request.find('/?LED=ON0')
        LEDOFF0 = request.find('/?LED=OFF0')
        LEDON2 = request.find('/?LED=ON2')
        LEDOFF2 = request.find('/?LED=OFF2')
        LEDON3 = request.find('/?LED=ON3')
        LEDOFF3 = request.find('/?LED=OFF3')
        if LEDON0 == 6:
            print('TURN LED0 ON')
            LED0.on()
        if LEDOFF0 == 6:
            print('TURN LED0 OFF')
            LED0.off()
        if LEDON2 == 6:
            print('TURN LED2 ON')
            LED2.on()
        if LEDOFF2 == 6:
            print('TURN LED2 OFF')
            LED2.off()
        if LEDON3 == 6:
            print('TURN LED3 ON')
            LED3.on()
        if LEDOFF3 == 6:
            print('TURN LED3 OFF')
            LED3.off()
        if SENSOR == 6:
            print('SENSOR TOUCHED')
            LED3.on()
            LED2.on()
            LED0.on()
        response = html
        conn.send(response)
