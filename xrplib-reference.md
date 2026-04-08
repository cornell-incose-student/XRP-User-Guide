# XRPLib Quick Reference

When you write `from XRPLib.defaults import *`, you get a set of pre-built objects — one for each component on the robot. This page documents what those objects are and what you can do with them.

---

## Available Objects

| Object | Type | What it controls |
|--------|------|-----------------|
| `drivetrain` | DifferentialDrive | Both drive motors together |
| `left_motor` | EncodedMotor | Left drive motor individually |
| `right_motor` | EncodedMotor | Right drive motor individually |
| `servo_one` | Servo | Servo port 1 (the arm) |
| `servo_two` | Servo | Servo port 2 |
| `reflectance` | Reflectance | Built-in line sensor (two IR sensors) |
| `rangefinder` | Rangefinder | Ultrasonic distance sensor |
| `imu` | IMU | Built-in accelerometer + gyroscope |
| `board` | Board | Onboard LED, button, RGB LED |

---

## `drivetrain` — Driving the Robot

The high-level interface for moving the robot. These commands **block** (pause your program) until the movement is complete or the timeout is reached.

| Method | Description |
|--------|-------------|
| `drivetrain.straight(distance, max_effort=0.5, timeout=None)` | Drive forward `distance` cm. Negative distance goes backward. Returns `True` if completed, `False` if timed out. |
| `drivetrain.turn(degrees, max_effort=0.5, timeout=None)` | Turn clockwise by `degrees`. Negative turns counterclockwise. Returns `True` if completed, `False` if timed out. |
| `drivetrain.stop()` | Stop both motors immediately. |
| `drivetrain.arcade(straight, turn)` | Set motor effort directly using arcade-style inputs. Both bounded `-1` to `1`. Does not block — runs continuously until you call something else. |
| `drivetrain.set_effort(left, right)` | Set raw effort for each motor independently. Bounded `-1` to `1`. Does not block. |
| `drivetrain.set_speed(left_cm_s, right_cm_s)` | Set speed in cm/s for each motor. Does not block. |
| `drivetrain.get_left_encoder_position()` | Returns distance traveled by the left wheel since last reset, in cm. |
| `drivetrain.get_right_encoder_position()` | Returns distance traveled by the right wheel since last reset, in cm. |
| `drivetrain.reset_encoder_position()` | Reset both encoder positions to 0. |

**Notes:**
- `straight()` and `turn()` handle their own stopping — you don't need to call `stop()` after them.
- Adding a `timeout` (in seconds) to `straight()` or `turn()` prevents the robot from getting stuck if it can't reach the target (e.g., blocked by an obstacle).
- `arcade()`, `set_effort()`, and `set_speed()` don't have a target — they run continuously until you call something else. These are used for manual/controller-driven movement.
- `arcade()` is what the PestoLink example code uses under the hood: `straight=1` is full speed forward, `turn=1` turns left.

---

## `left_motor` / `right_motor` — Individual Motor Control

Use these when you want direct control over each motor without the drivetrain abstraction. `motor_three` and `motor_four` work the same way if you have additional motors attached.

| Method | Description |
|--------|-------------|
| `left_motor.set_effort(effort)` | Set motor power. `-1` to `1`. Does not block. |
| `left_motor.set_speed(rpm)` | Set motor speed in RPM. Call with no argument or `0` to stop. |
| `left_motor.get_speed()` | Returns current speed in RPM. |
| `left_motor.get_position()` | Returns position in revolutions since last reset. |
| `left_motor.reset_encoder_position()` | Reset encoder to 0. |
| `left_motor.brake()` | Actively resist rotation (hold position). |
| `left_motor.coast()` | Allow motor to spin freely. |

---

## `servo_one` / `servo_two` — Servo Control

| Method | Description |
|--------|-------------|
| `servo_one.set_angle(degrees)` | Move servo to a position. Range is `0` to `200` degrees. |
| `servo_one.free()` | Release the servo so it can spin freely (no position hold). |

**Notes:**
- The servo holds its position after `set_angle()` — no need to call it repeatedly.
- The usable range depends on what's attached. Test with nothing connected before attaching mechanisms.
- Moving the servo to a known angle at startup (e.g., `servo_one.set_angle(90)`) is a useful visual indicator that your program is running.

---

## `reflectance` — Line Sensor

The built-in sensor reads reflected infrared light from the ground. Returns a value from `0.0` (bright/white) to `1.0` (dark/black).

| Method | Description |
|--------|-------------|
| `reflectance.get_left()` | Read the left IR sensor. Returns `0.0` (white) to `1.0` (black). |
| `reflectance.get_right()` | Read the right IR sensor. Returns `0.0` (white) to `1.0` (black). |

**Notes:**
- Values vary depending on ambient light and surface material — calibrate thresholds for your specific setup.
- For line following, compare left vs. right values to determine which side is over the line.

---

## `rangefinder` — Distance Sensor

Ultrasonic sensor that measures how far away the nearest object is.

| Method | Description |
|--------|-------------|
| `rangefinder.distance()` | Returns distance to nearest object in cm. |

**Notes:**
- Returns `65535` when nothing is in range (or the sensor times out). Check for this in your code — don't treat it as a real distance.
- Effective range is approximately 2 cm to 400 cm.
- Results are cached for ~3ms to avoid hammering the sensor in tight loops.

---

## `imu` — Inertial Measurement Unit

The built-in gyroscope and accelerometer. Tracks how the robot has rotated since startup (or since last reset).

| Method | Description |
|--------|-------------|
| `imu.get_roll()` | Returns accumulated rotation in degrees. **This is the heading axis for the upright board.** |
| `imu.get_yaw()` | Returns accumulated yaw (unbounded). Not the primary heading axis for the upright board. |
| `imu.get_pitch()` | Returns accumulated pitch (unbounded). |
| `imu.get_heading()` | Returns yaw bounded to `[0, 360)`. |
| `imu.reset_roll()` | Reset roll to 0. |
| `imu.reset_yaw()` | Reset yaw to 0. |
| `imu.reset_pitch()` | Reset pitch to 0. |
| `imu.get_acc_x/y/z()` | Read accelerometer on one axis, in mg (milli-g). |
| `imu.temperature()` | Read board temperature in °C (useful for debugging, not competition). |

**Important — board orientation:** Because the controller board on the Lego XRP is mounted **upright (vertical)** rather than flat, the roll axis tracks the robot's turning. The `drivetrain` commands (`straight()`, `turn()`) use `get_roll()` internally for heading. If you read the IMU directly in your own code, use `get_roll()` for heading.

**Drift warning:** The gyroscope accumulates small errors over time. For long programs, reset the IMU before movements where heading matters, or use encoder-based navigation instead.

---

## `board` — Onboard LED and Button

| Method | Description |
|--------|-------------|
| `board.is_button_pressed()` | Returns `True` if the user button is currently pressed. |
| `board.wait_for_button()` | **Pauses the program** until the button is pressed and released. Useful for starting programs on demand. |
| `board.led_on()` | Turn the onboard LED on. |
| `board.led_off()` | Turn the onboard LED off. |
| `board.led_blink(frequency)` | Blink the LED at `frequency` Hz. Pass `0` to stop blinking. |
| `board.set_rgb_led(r, g, b)` | Set the RGB LED color. Each value is `0–255`. (Not available on XRP Beta boards.) |
| `board.are_motors_powered()` | Returns `True` if the battery is connected and powering the motors. |

**Tip:** `board.wait_for_button()` at the start of your program is a clean way to let the robot sit still while you position it, then start the autonomous sequence on a button press.

---

## What's Not Covered Here

- **`webserver`** — Enables a web-based control interface over Wi-Fi. Useful for advanced projects, but not needed for the competition challenge.
- **`PID` / `Controller`** — The library's built-in PID controller, used internally by `straight()` and `turn()`. You can pass custom controllers to those functions if you want to tune behavior.
- **`Timeout`** — Internal utility used by `straight()` and `turn()`. You generally don't need to use it directly.
