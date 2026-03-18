from XRPLib.defaults import *
from machine import Pin, I2C, ADC
import time
from tcs3472 import tcs3472
import bluetooth
import math
from pestolink import PestoLinkAgent

imu.reset_pitch()
imu.reset_yaw()
imu.reset_roll()

def test_pestolink():
    print('Pestolink test. Press the user button to stop.')
    pestolink = PestoLinkAgent("XRProbot")
    # Start an infinite loop
    while not board.is_button_pressed():
        if pestolink.is_connected():  # Check if a BLE connection is established
            rotation = -1 * pestolink.get_axis(0)
            throttle = -1 * pestolink.get_axis(1)

            drivetrain.arcade(throttle, rotation)

            if(pestolink.get_button(0)):
                servo_one.set_angle(110)
            else:
                servo_one.set_angle(90)

            batteryVoltage = (ADC(Pin("BOARD_VIN_MEASURE")).read_u16())/(1024*64/14)
            pestolink.telemetryPrintBatteryVoltage(batteryVoltage)

        else: #default behavior when no BLE connection is open
            drivetrain.arcade(0, 0)
            servo_one.set_angle(70)

def test_turns():
    drivetrain.turn(45, 0.5, use_imu=False)
    time.sleep(1)
    drivetrain.turn(-45, 0.75, use_imu=False)
    time.sleep(1)

    drivetrain.turn(90, 0.5, use_imu=False)
    time.sleep(1)
    drivetrain.turn(-90, 0.75, use_imu=False)
    time.sleep(1)

def test_straight():
    drivetrain.straight(30, 0.5)

def test_servo():
    print('Servo test. Press the user button to stop.')
    servo_one.set_angle(0)
    time.sleep(1)
    servo_one.set_angle(90)
    time.sleep(1)
    servo_one.set_angle(0)
    time.sleep(1)
    servo_one.set_angle(90)
    time.sleep(1)
    servo_one.set_angle(180)
    time.sleep(1)
    servo_one.set_angle(90)
    time.sleep(1)
    servo_one.set_angle(0)
    time.sleep(1)

def test_rangefinder():
    print('Rangefinder test. Wave your hand in front of the rangefinder to change the distance. Press the user button to stop.')
    while not board.is_button_pressed():
        print(f"{rangefinder.distance()}")
        time.sleep(0.5)

def test_imu():
    print('IMU test. Rotate the robot to change its orientation. Press the user button to stop.')
    while not board.is_button_pressed():
        print(f"Pitch: {imu.get_pitch()}, Heading: {imu.get_heading()}, Roll: {imu.get_yaw()}, Accelerometer output: {imu.get_acc_rates()}")
        time.sleep(0.1)

def test_line():
    print('Line test. Press the user button to stop.')
    while not board.is_button_pressed():
        print(f"Left: {reflectance.get_left()}, Right: {reflectance.get_right()}")
        time.sleep(0.1)

def test_push_button():
    digital_button = Pin(9, Pin.IN, Pin.PULL_DOWN)
    print('Push botton test. Press the user button to stop.')
    while not board.is_button_pressed():
        print(f"Button state: {digital_button.value()}")
        time.sleep(0.1)

def test_rgb_sensor():
    i2c_bus = I2C(0, sda=Pin(4), scl=Pin(5))
    tcs = tcs3472(i2c_bus)
    print('RGB sensor test. Press the user button to stop.')
    while not board.is_button_pressed():
        print(f"RGB: {tcs.rgb()}")
        time.sleep(0.1)

#  Uncomment the test(s) you want to run

#test_pestolink()

#test_servo()

#test_turns()

#test_straight()

#test_rangefinder()

#test_imu()

#test_line()

#test_push_button()

#test_rgb_sensor()
