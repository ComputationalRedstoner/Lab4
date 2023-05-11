import time
import src.hal.hal_input_switch as input_switch
import src.hal.hal_led as led

def switch_read():
    input_switch.init()
    return input_switch.read_slide_switch()

def blink_led(delay):
    # Led Blink
    led.init()
    led.set_output(0, 1)
    time.sleep(delay)
    led.set_output(0, 0)
    time.sleep(delay)

def main():
    switch_val = switch_read()
    if switch_val == 1:
        blink_led(0.2)
    else:
        # 10Hz
        blink_led(0.1)

if __name__ == "__main__":
    while True:
        main()