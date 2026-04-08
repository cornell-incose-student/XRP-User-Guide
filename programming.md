# Programming

## Getting Started with XRP Code

The XRP is programmed using the web-based **XRP Code Editor**. Use **Google Chrome** for best compatibility.

### Connecting for the First Time

1.  Plug in your XRP via USB-C and turn it on (small power switch on the board).
2.  Open the [XRP Code Editor](https://xrpcode.wpi.edu/) in Chrome.
3.  The editor may auto-connect. If not, click the connect icon and select your XRP.
4.  If the XRP doesn't connect within \~30 seconds, press the **reset button** (the button farthest from the power switch, among the three buttons near it).

### Tips for the Code Editor

- **Save your code to your computer!** The editor does not save locally.
- Your XRP may auto-connect after the first time — this varies by computer.
- You likely won't need firmware updates, but follow on-screen instructions if prompted.
- If your XRP won't stop running (spinning "XRP" image), turn off the XRP and reload the web editor page.

### Key Programming Videos

- [**XRP Movement Guide Using The XRP Code Editor**](https://www.youtube.com/watch?v=jHKAQSRTRaM) — Programming basics of robot movement
- [**XRP Delivery Challenge Guide Using Servo and Sensors**](https://www.youtube.com/watch?v=DH_uv6ndZF0) — Combining sensors, servos, and movement

------------------------------------------------------------------------

## Programming in Python

The XRP is programmed in Python. All the skills in this guide use Python, and the XRP Code Editor supports it directly.

### Python Basics: Reading and Modifying Code

New to Python? Read the [**Python Basics guide**](python-basics.md) before diving into the skills. It covers variables, functions, loops, conditionals, imports, and the common mistakes that trip people up.

Want to know what the robot can actually do? See the [**XRPLib Quick Reference**](xrplib-reference.md) for a complete list of objects and functions available after `from XRPLib.defaults import *`.

------------------------------------------------------------------------

## A Note on Using AI

The XRP is a specific robot running MicroPython with a specific library. AI tools often don't know about it, and will confidently generate code using the wrong function names, wrong syntax, or libraries that don't exist on the XRP. Robotics involves a lot of trial and error: sensors behave differently on different surfaces, motors drift, things don't work on the first try. When something goes wrong (and it will), you need to understand your own code well enough to figure out why.

AI is a useful tool for explaining a concept, suggesting an approach, or helping you understand an error message. Use it as a resource the same way you'd use a search engine — not as a replacement for thinking through the problem yourself.

------------------------------------------------------------------------

## Skill 1: Driving with PestoLink

If you've completed the [Quick Start Guide](quick-start.md), you've done this! If not, refer to the Quick Start Guide for how to connect your robot to a game controller via PestoLink.

Reference: [XRPLib Quick Reference — drivetrain](xrplib-reference.md#drivetrain--driving-the-robot) (specifically `arcade()`, which PestoLink uses for movement)

------------------------------------------------------------------------

## Skill 2: Programmatically Controlling the Drive Motors

The `drivetrain` object controls the robot's drive motors for autonomous movement. For direct per-motor control, use `left_motor` and `right_motor` instead.

Reference: [XRPLib Quick Reference — drivetrain](xrplib-reference.md#drivetrain--driving-the-robot) · [XRPLib Quick Reference — left/right motor](xrplib-reference.md#left_motor--right_motor--individual-motor-control) · [XRP user guide](https://xrpusersguide.readthedocs.io/en/latest/course/driving.html)

### Basic Movement

`straight()` and `turn()` block until the movement is complete, then your program continues. `max_effort` controls speed (0 to 1).

``` python
from XRPLib.defaults import *

drivetrain.straight(30)          # forward 30 cm at default speed
drivetrain.straight(30, 0.75)    # forward 30 cm at 75% speed
drivetrain.straight(-20)         # backward 20 cm

drivetrain.turn(90)              # turn clockwise 90°
drivetrain.turn(-45)             # turn counterclockwise 45°
```

Add a `timeout` so the robot doesn't get stuck if it can't complete a movement (e.g., if it's blocked):

``` python
completed = drivetrain.straight(50, timeout=3)  # give up after 3 seconds
if not completed:
    print("Timed out!")
```

**Important:** If the robot is handheld when asked to turn, it will spin its wheels indefinitely because the IMU never detects the expected heading change. Always test turning commands with the robot on the ground.

**If your robot's turns are behaving strangely**, read [The IMU and Board Orientation](#the-imu-board-orientation-and-driving-straight) below. Make sure to use the updated library or pass `use_imu=False`, which uses the wheel encoders for turning instead and works regardless of board orientation:

``` python
drivetrain.turn(90, use_imu=False)
```

### Reading Encoders

Encoders track how far each wheel has traveled. This is useful for dead reckoning — estimating position based on distance driven.

``` python
from XRPLib.defaults import *

drivetrain.reset_encoder_position()
drivetrain.straight(30)

print(drivetrain.get_left_encoder_position())   # cm traveled by left wheel
print(drivetrain.get_right_encoder_position())  # cm traveled by right wheel
```

### Direct Motor Control

If `drivetrain.straight()` and `turn()` aren't giving you the behavior you need, you can control each motor directly using `left_motor` and `right_motor`. This bypasses IMU correction entirely.

``` python
from XRPLib.defaults import *
import time

left_motor.set_effort(0.5)    # left wheel forward at 50%
right_motor.set_effort(0.5)   # right wheel forward at 50%
time.sleep(2)                 # run for 2 seconds
left_motor.set_effort(0)
right_motor.set_effort(0)
```

### The IMU, Board Orientation, and Driving Straight.

The XRP has a built-in **Inertial Measurement Unit (IMU)** — a 3-axis accelerometer and 3-axis gyroscope (the same type of sensor in your smartphone). On the XRP, the IMU measures how much the robot has turned (yaw).

Your Lego-compatible XRP has the controller board mounted **upright (vertical)**, while many tutorials show it flat (horizontal). This affects IMU-based Drivetrain commands:

- The default Drivetrain commands may not work correctly with the upright orientation.
- The XRPLib in this repository (`code/XRPLib/`) includes an updated `differential_drive.py` modified for the upright board. Use the files from this repo rather than the default XRPLib that comes with the editor.
- Alternatively, pass `use_imu=False` to `drivetrain.turn()`, or use `left_motor`/`right_motor` directly. Both approaches bypass the IMU entirely and work regardless of board orientation.

**Driving perfectly straight is hard!** All competition challenges have been completed by teams whose robots could not drive perfectly straight. Focus on using encoders, sensors, and iterative adjustments rather than relying on precise IMU-based navigation. The IMU is a bonus — not a requirement for success.

------------------------------------------------------------------------

## Skill 3: Programmatically Controlling the Servo

Reference: [XRPLib Quick Reference — servo](xrplib-reference.md#servo_one--servo_two--servo-control) · [XRP user guide](https://xrpusersguide.readthedocs.io/en/latest/course/arm.html)

The servo motor is the **small black motor** (not the two larger drive motors). It can rotate to a specific position and hold it there.

### Important Warnings

- The servo has a **limited rotation range**. Do not force it beyond its limits — this will permanently damage the motor.
- Before attaching anything to the servo, test its range by sending different angle commands with only the Lego hub attached.
- With power off, you can gently move the hub by hand to feel the range limits.
- When building devices with the servo, plan your mechanical design around the servo's range before connecting it.

### Basic Code

Move the servo to a position and it holds there. The range is 0–200°, but the usable range depends on what's attached — test before connecting anything.

``` python
from XRPLib.defaults import *
import time

servo_one.set_angle(0)     # move to 0°
time.sleep(1)
servo_one.set_angle(90)    # move to 90°
time.sleep(1)
servo_one.set_angle(180)   # move to 180°
```

Moving the servo to a known angle at startup is a useful visual indicator that your program is running:

``` python
servo_one.set_angle(50)    # "I'm alive" indicator at startup
```

To release the servo so it can spin freely (no holding force):

``` python
servo_one.free()
```

------------------------------------------------------------------------

## Skill 4: Following Lines with the Reflectance Sensor

Reference: [XRPLib Quick Reference — reflectance](xrplib-reference.md#reflectance--line-sensor) · [XRP user guide](https://xrpusersguide.readthedocs.io/en/latest/course/sensors.html#following-lines)

The reflectance sensor has two IR sensors (left and right) that return a value from 0.0 (white/bright) to 1.0 (black/dark).

### Reading Values

Start by printing sensor values to understand what your specific surface and lighting conditions produce. The reflectance ranges from 0 (white) to 1 (black).

``` python
from XRPLib.defaults import *
import time

while True:
    print(reflectance.get_left(), reflectance.get_right())
    time.sleep(0.1)
```

### Line Following with Proportional Control

The example below is taken from [XRP user guide](https://xrpusersguide.readthedocs.io/en/latest/course/sensors.html#following-lines).

The following program uses proportional control with the line sensors to follow a black line across the driving surface for the robot. The Kp variable sets the gain for the controller.

``` python
from XRPLib.defaults import *

kP = 0.1      # proportional gain — increase for sharper corrections
speed = 0.25  # base forward speed

while not board.is_button_pressed():
    error = reflectance.get_right() - reflectance.get_left()
    drivetrain.set_effort(speed - error * kP, speed + error * kP)

drivetrain.stop()
```

How it works: `error` is positive when the right sensor sees more black (robot drifting left of the line), which reduces left motor effort and increases right, steering back. When centered, `error` is near 0 and both motors run at `speed`. This will need to be adjusted if your line is a lighter color than the robot's driving surface.

Tune `kP` and `speed` for your surface — start low and increase until the robot tracks reliably without oscillating.

------------------------------------------------------------------------

## Skill 5: Using the Distance Sensor

Reference: [XRPLib Quick Reference — rangefinder](xrplib-reference.md#rangefinder--distance-sensor) · [XRP user guide](https://xrpusersguide.readthedocs.io/en/latest/course/sensors.html#measuring-the-distance-to-an-object)

`rangefinder.distance()` returns the distance to the nearest object in centimeters. Effective range is roughly 2–400 cm.

### Reading Values

``` python
from XRPLib.defaults import *
import time

while True:
    print(rangefinder.distance())
    time.sleep(0.5)
```

**Important:** When nothing is in range, the sensor returns `65535` instead of raising an error. Always check for this in your code:

``` python
dist = rangefinder.distance()
if dist < 65535:
    print(f"Object at {dist} cm")
else:
    print("Nothing in range")
```

### Stopping Before an Obstacle

``` python
from XRPLib.defaults import *

while True:
    if rangefinder.distance() < 20:   # stop if something within 20 cm
        drivetrain.stop()
    else:
        drivetrain.arcade(0.4, 0)     # drive forward
```

------------------------------------------------------------------------

## Skill 6: Using the Touch Sensor (Digital Push Button)

It's a simple button, but sometimes that's all you need! See [Sensor Wiring](sensor-wiring.md#touch-sensor--digital-button) for connection details.

> **Note:** The code below uses the low-level `machine.Pin` interface because the touch sensor is an external button wired to a servo port — it's not part of XRPLib. The **onboard button** on the XRP board itself is handled by XRPLib: see [XRPLib Quick Reference — board](xrplib-reference.md#board--onboard-led-and-button) for `board.is_button_pressed()` and `board.wait_for_button()`.

### Basic Code

``` python
from machine import Pin
import time

digital_button = Pin(9, Pin.IN, Pin.PULL_DOWN)

while True:
    if digital_button.value() == 0:
        print("Not pressed")
    else:
        print("Pressed")
    time.sleep(0.1)
```

In this code: `9` = pin number (Servo 2), `Pin.IN` = input mode, `Pin.PULL_DOWN` = interprets press as 1, release as 0.

### Button Debouncing

The `time.sleep(0.1)` prevents reading the same press multiple times (buttons physically "bounce"). For more precise timing, use MicroPython's tick functions:

``` python
start = time.ticks_us()
if time.ticks_diff(time.ticks_us(), start) > 500:
    print("Enough time has passed")
```

Reference: [MicroPython time documentation](https://docs.micropython.org/en/latest/library/time.html)

------------------------------------------------------------------------

## Skill 7: Putting It All Together

By now you should have a good sense of how to write code to control the robot's motors and servos and read from its various sensors. This skill covers:

1.  Turning code snippets into **functions**
2.  **Importing** functions from other files into your main file
3.  **Mapping functions to buttons** so they trigger when you press a button on your game controller

The `pestolink_example.py` file has a main loop that constantly checks for controller input. You can add `if`-statements to detect specific button presses and call functions in response.

### Example: Rotate on Button Press

**Goal:** Press B (button 1) to make the robot spin continuously. Press A (button 0) to stop and return to manual control.

#### Step 1: Create the Function File

In the code editor, go to **File → New File → MicroPython**. Save as `/lib/rotate_function.py`:

``` python
def rotate_function(drivetrain, pestolink):
    while True:
        drivetrain.arcade(0, 1)  # Spin in place
        if pestolink.get_button(0):  # A button to stop
            return None
```

#### Step 2: Import and Call from Main Script

Add to the top of `pestolink_example.py`:

``` python
from rotate_function import *
```

#### Step 3: Map Function to Button Press

Inside the main loop of `pestolink_example.py`:

``` python
if pestolink.get_button(1):  # B button
    rotate_function(drivetrain, pestolink)
```

Now when you press B, the robot spins until you press A.

### Key Rules for Custom Functions

- **Pass robot instances as parameters.** The `drivetrain` and `pestolink` objects can only be created once. Pass them into your functions — do not create new instances in separate files, or your code will break.
- **Always include an exit condition.** Use `pestolink.get_button()` inside your function's loop so the user can return to manual control.
- **Store function files in `/lib/`.** This lets you import them cleanly with `from filename import *`.
- **Use pestol.ink to see which controller buttons map to which numerical pestolink buttons.** If you go to pestol.ink, connect your controller, and start hitting buttons (ensure Override axes/buttons is turned ON), you should be able to see which pestolink buttons (0-15) trigger when you hit A/B/X/Y, etc on the controller.
