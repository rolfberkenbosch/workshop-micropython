def do_connect():
    import network
    import time
    import machine
    from machine import Pin

    yellow = Pin(14, Pin.OUT)
    blue = Pin(13, Pin.OUT)
    red = Pin(16, Pin.OUT)

    red.off()
    yellow.off()

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ssid', 'password')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    blue.on()

do_connect()
