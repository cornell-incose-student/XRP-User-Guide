# Programming

## Getting Started with XRP Code

The XRP is programmed using the web-based **XRP Code Editor**. Use **Google Chrome** for best compatibility.

### Connecting for the First Time

1.  Plug in your XRP via USB-C and turn it on (small power switch on the board).
2.  Open the [XRP Code Editor](https://xrpcode.wpi.edu/) in Chrome.
3.  The editor may auto-connect. If not, click the connect icon and select your XRP.
4.  If the XRP doesn't connect within \~30 seconds, press the **reset button** (the button farthest from the power switch, among the three buttons near it).

### Tips for the Code Editor

-   **Save your code to your computer!** The editor does not save locally.
-   Your XRP may auto-connect after the first time — this varies by computer.
-   You likely won't need firmware updates, but follow on-screen instructions if prompted.
-   If your XRP won't stop running (spinning "XRP" image), turn off the XRP and reload the web editor page.

### Key Programming Videos

-   [**XRP Movement Guide Using The XRP Code Editor**](https://www.youtube.com/watch?v=jHKAQSRTRaM) — Programming basics of robot movement
-   [**XRP Delivery Challenge Guide Using Servo and Sensors**](https://www.youtube.com/watch?v=DH_uv6ndZF0) — Combining sensors, servos, and movement

------------------------------------------------------------------------

## Choosing a Programming Mode

### Blockly (Beginner-Friendly)

Blockly provides a drag-and-drop visual interface for building programs. It's a great starting point for anyone new to programming.

> **Note:** There are no Blockly blocks for the color sensor or the touch sensor button. You will need Python for those features.

### Python (Recommended for the Challenge)

Python gives you full control and access to all XRP features. You'll eventually want to use Python, but Blockly is a perfectly fine starting point.

### Transitioning from Blockly to Python

-   **View Python equivalent:** In the editor, go to **View → View Python**. This shows the Python code for your Blockly program without changing anything.
-   **Convert permanently:** Go to **View → Convert to Python**. This cannot be undone — make a copy of your code first!
-   **Learn-by-doing tip:** Build something in Blockly, view the generated Python, then copy that code into your main Python program. It's a great way to learn Python syntax.

### Python Basics: Reading and Modifying Code

Full API reference: [XRP Code Documentation](https://xrpusersguide.readthedocs.io/en/latest/)

For example, see [Motors Documentation](https://xrpusersguide.readthedocs.io/en/latest/course/driving.html) for all motor control commands.

------------------------------------------------------------------------

## A Note on Using AI

When programming an XRP robot, it can be tempting to lean entirely on generative AI tools for writing and debugging code — but doing so carries real risks:

-   AI models may not have up-to-date knowledge of the XRP's specific hardware, motor controllers, or sensor configurations.
-   AI-generated code can compile and appear to run correctly but behave unpredictably on physical hardware due to sensor noise, latency, or power constraints.
-   AI can introduce deprecated functions or libraries incompatible with the MicroPython environments used on XRP.
-   Over-reliance stunts your own growth as a robotics programmer, leaving you unable to independently diagnose issues.

**Use AI as a helpful collaborator, but take full ownership of every line of code you deploy.**

------------------------------------------------------------------------

## Skill 1: Driving with PestoLink

If you've completed the [Quick Start Guide](quick-start.md), you've done this! If not, refer to the Quick Start Guide for how to connect your robot to a game controller via PestoLink.

------------------------------------------------------------------------

## Skill 2: Programmatically Controlling the Drive Motors

The `differential_drive` class controls the robot's drive motors for autonomous movement.

Reference: <https://xrpusersguide.readthedocs.io/en/latest/course/driving.html>

### An Aside about the IMU & Driving Straight

The XRP has a built-in **Inertial Measurement Unit (IMU)** — a 3-axis accelerometer and 3-axis gyroscope (the same type of sensor in your smartphone). On the XRP, the IMU measures how much the robot has turned (yaw).

**Important:** If the robot is handheld when asked to turn, it will spin its wheels indefinitely because the IMU never detects the expected heading change. Always test turning commands with the robot on the ground.

No small robot drives perfectly straight. The IMU's gyroscope experiences **yaw drift** (approximately 1° per minute, often more during movement). This means: - Heading measurements will slowly accumulate error over time. - The robot may veer slightly during long straight runs. - The `Drivetrain` commands attempt to correct for this, but are not perfect.

> <span style="color: red;">**REVIEW NOTE:**</span> Review and confirm yaw drift rates for the specific IMU (LSM6DSOX) on the red board. Verify whether the prototype drivetrain library on Canvas has been updated.

**All competition challenges have been completed by teams whose robots could not drive perfectly straight.** Focus on using encoders, sensors, and iterative adjustments rather than relying on precise IMU-based navigation. The IMU is a bonus — not a requirement for success.

### Board Orientation Matters

Your Lego-compatible XRP has the controller board mounted **upright (vertical)**, while many tutorials show it flat (horizontal). This affects IMU-based Drivetrain commands:

-   The default Drivetrain commands may not work correctly with the upright orientation.
-   A prototype XRP library with an updated drivetrain file is available on Canvas as: **`XRBLib_Drivetrain.zip`**. It contains the full XRPLib folder but only the drivetrain file has been modified.
-   Alternatively, use individual **`EncoderMotor`** commands to control your robot directly. This approach works regardless of board orientation and was used successfully for years of competition.

------------------------------------------------------------------------

## Skill 3: Programmatically Controlling the Servo

Reference: <https://xrpusersguide.readthedocs.io/en/latest/course/arm.html>

The servo motor is the **small black motor** (not the two larger drive motors). It can rotate to a specific position and hold it there.

### Important Warnings

-   The servo has a **limited rotation range**. Do not force it beyond its limits — this will permanently damage the motor.
-   Before attaching anything to the servo, test its range by sending different angle commands with only the Lego hub attached.
-   With power off, you can gently move the hub by hand to feel the range limits.
-   When building devices with the servo, plan your mechanical design around the servo's range before connecting it.

### Helpful Visual Indicator

It can be useful to move the servo to a known angle (e.g., 50°) at startup as a visual indicator that your program is running.

------------------------------------------------------------------------

## Skill 4: Following Lines with the Reflectance Sensor

Reference: <https://xrpusersguide.readthedocs.io/en/latest/course/sensors.html#following-lines>

------------------------------------------------------------------------

## Skill 5: Using the Distance Sensor

Reference: <https://xrpusersguide.readthedocs.io/en/latest/course/sensors.html#measuring-the-distance-to-an-object>

------------------------------------------------------------------------

## Skill 6: Using the Touch Sensor (Digital Push Button)

It's a simple button, but sometimes that's all you need! See [Sensor Wiring](sensor-wiring.md#touch-sensor--digital-button) for connection details.

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

-   **Pass robot instances as parameters.** The `drivetrain` and `pestolink` objects can only be created once. Pass them into your functions — do not create new instances in separate files, or your code will break.
-   **Always include an exit condition.** Use `pestolink.get_button()` inside your function's loop so the user can return to manual control.
-   **Store function files in `/lib/`.** This lets you import them cleanly with `from filename import *`.