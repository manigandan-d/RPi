import pigpio
from time import sleep
import subprocess

for _ in range(3):
    p = subprocess.Popen('sudo pigpiod', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p.poll() == 0:
        break
    sleep(0.2)

class Servo:
    _PWM_FREQ_HZ = 50
    _PWM_RANGE   = 10000
    _PULSE_MIN   = 250 
    _PULSE_MAX   = 1250  

    def __init__(self, gpio_pin, min_angle=-90, max_angle=90):
        self.pi = pigpio.pi()
        self.gpio_pin   = gpio_pin
        self.min_angle  = min_angle
        self.max_angle  = max_angle
        self.current_deg = 0

        self.pi.set_PWM_frequency(gpio_pin, self._PWM_FREQ_HZ)
        self.pi.set_PWM_range(gpio_pin, self._PWM_RANGE)
        self.pi.set_PWM_dutycycle(gpio_pin, 0)

    def set_angle(self, degrees):
        if degrees > self.max_angle:  degrees = self.max_angle
        if degrees < self.min_angle:  degrees = self.min_angle
        self.current_deg = degrees
        pulse = self._map(degrees, -90, 90, self._PULSE_MIN, self._PULSE_MAX)
        self.pi.set_PWM_dutycycle(self.gpio_pin, pulse)

    def get_angle(self):
        return self.current_deg

    @staticmethod
    def _map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == '__main__':
    from vilib import Vilib
    Vilib.camera_start(vflip=True, hflip=True)
    Vilib.display(local=True, web=True)

    pan_servo  = Servo(gpio_pin=13, max_angle=90,  min_angle=-90)
    tilt_servo = Servo(gpio_pin=12, max_angle=30, min_angle=-90)

    pan_deg  = 0
    tilt_deg = 0
    pan_servo.set_angle(pan_deg)
    tilt_servo.set_angle(tilt_deg)
    sleep(1)

    while True:
        for deg in range(0, 90, 1):
            pan_servo.set_angle(deg)
            tilt_servo.set_angle(deg)
            sleep(0.01)
        sleep(0.5)

        for deg in range(90, -90, -1):
            pan_servo.set_angle(deg)
            tilt_servo.set_angle(deg)
            sleep(0.01)
        sleep(0.5)

        for deg in range(-90, 0, 1):
            pan_servo.set_angle(deg)
            tilt_servo.set_angle(deg)
            sleep(0.01)
        sleep(0.5)
