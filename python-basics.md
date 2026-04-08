# Python Basics

This is a quick crash course in Python — enough to read and write XRP programs confidently. Use it as a reference as you work through the skills.

------------------------------------------------------------------------

## How Python Programs Run

Python runs your code **top to bottom**, one line at a time. When it hits a function call, it jumps into that function, runs it, then comes back and continues.

``` python
print("Step 1")   # runs first
print("Step 2")   # runs second
print("Step 3")   # runs third
```

------------------------------------------------------------------------

## Comments

A `#` makes the rest of the line a comment — Python ignores it. Use comments to explain what your code is doing.

``` python
# Move forward 20 cm at half speed
drivetrain.straight(20, 0.5)
```

------------------------------------------------------------------------

## Variables

A variable stores a value so you can use it later (or change it).

``` python
speed = 0.5
distance = 30

drivetrain.straight(distance, speed)
```

You can update a variable at any time:

``` python
speed = 0.5
speed = 0.8   # now speed is 0.8
```

Variable names are **case-sensitive**: `speed`, `Speed`, and `SPEED` are three different variables.

------------------------------------------------------------------------

## Functions

A function is a named block of code you can run by **calling** it. Most of the XRP code you write will involve calling functions from the XRP library.

``` python
drivetrain.straight(20)      # move forward 20 cm
drivetrain.turn(90)          # turn 90 degrees
time.sleep(1)                # wait 1 second
```

The values you pass in (like `20` or `90`) are called **arguments**. Functions can take zero, one, or multiple arguments separated by commas.

**Don't forget the parentheses.** `drivetrain.stop` doesn't do anything — it just references the function without running it. `drivetrain.stop()` actually calls it.

### Objects and Dot Notation

An **object** is a bundle of related data and functions. `drivetrain` is an object that represents the robot's wheels — it knows about the motors and has functions for controlling them. The dot (`.`) is how you access those functions:

```python
drivetrain.straight(20)    # call the straight function on the drivetrain object
reflectance.get_left()     # call get_left on the reflectance object
servo_one.set_angle(90)    # call set_angle on the servo_one object
```

You don't need to know how objects are built — when you write `from XRPLib.defaults import *`, all the XRP objects are created for you automatically. See the [XRPLib Quick Reference](xrplib-reference.md) for a full list of what's available and what each one can do.

### Defining Your Own Functions

You can write your own functions to group code you want to reuse:

``` python
def celebrate():
    drivetrain.turn(360)
    time.sleep(0.5)
    drivetrain.turn(-360)
```

Call it later with `celebrate()`.

Functions can take parameters (inputs) and return values (outputs):

``` python
def drive_and_stop(distance):
    drivetrain.straight(distance)
    drivetrain.stop()

drive_and_stop(30)   # drives 30 cm, then stops
drive_and_stop(10)   # drives 10 cm, then stops
```

------------------------------------------------------------------------

## Indentation

Python uses indentation (spaces or tabs at the start of a line) to define structure — instead of `{}` like many other languages.

``` python
def drive_and_stop(distance):
    drivetrain.straight(distance)   # inside the function
    drivetrain.stop()               # also inside the function

drivetrain.turn(90)                 # NOT inside the function
```

If your indentation is wrong, your code either crashes with a syntax error or does the wrong thing silently.

------------------------------------------------------------------------

## Conditionals

An `if` statement runs code only when a condition is true.

``` python
if distance_sensor.distance() < 10:
    drivetrain.stop()
```

Add `else` to handle the other case:

``` python
if distance_sensor.distance() < 10:
    drivetrain.stop()
else:
    drivetrain.straight(5)
```

Use `elif` for multiple cases:

``` python
value = reflectance_sensor.reflectance()

if value < 0.2:
    print("Dark surface")
elif value < 0.7:
    print("Medium surface")
else:
    print("Light surface")
```

### `=` vs `==`

- `=` **assigns** a value: `speed = 0.5`
- `==` **checks** if two things are equal: `if speed == 0.5`

------------------------------------------------------------------------

## Loops

### `while` Loop

Repeats as long as a condition is true.

``` python
while distance_sensor.distance() > 10:
    drivetrain.straight(5)
```

`while True` runs forever — useful for a main program loop that keeps checking sensors or buttons:

``` python
while True:
    if pestolink.get_button(0):
        drivetrain.stop()
```

**Make sure `while True` loops have a way out** (a `return`, `break`, or the robot turns off). It's easy to accidentally write a loop that locks up the robot.

### `for` Loop

Repeats a fixed number of times, or over a list of values.

``` python
for i in range(4):
    drivetrain.turn(90)    # turn 90 degrees, 4 times
```

`range(4)` produces the values 0, 1, 2, 3 — so this runs 4 times.

------------------------------------------------------------------------

## Imports

An import loads code from another file or library so you can use it.

``` python
from xrp import *
import time
```

`from xrp import *` loads everything in the XRP library — this gives you `drivetrain`, `reflectance_sensor`, etc.

`import time` loads Python's time module — required before you can use `time.sleep()`.

**Imports go at the top of your file**, before anything else. If you call a function without importing its library first, you'll get a `NameError`.

------------------------------------------------------------------------

## Types: Numbers and Strings

Python values have types. The most common ones you'll encounter:

| Type    | Example                | Notes                    |
|---------|------------------------|--------------------------|
| Integer | `10`, `0`, `-3`        | Whole numbers            |
| Float   | `0.5`, `1.0`, `3.14`   | Decimal numbers          |
| String  | `"hello"`, `"pressed"` | Text, in quotes          |
| Boolean | `True`, `False`        | Note the capital letters |

You can't mix strings and numbers in arithmetic — `"5" + 1` crashes. Convert first: `int("5") + 1` gives `6`.

------------------------------------------------------------------------

## Variable Scope

A variable defined **inside** a function only exists inside that function.

``` python
def my_function():
    x = 10      # x only exists here

print(x)        # ERROR: x is not defined here
```

If you need a value to persist between function calls, define it outside any function (at the "top level" of your file), or pass it in as a parameter and return it.

------------------------------------------------------------------------

## `time.sleep()` Blocks Everything

`time.sleep(1)` pauses your entire program for 1 second. While it's sleeping, nothing else runs — no sensor reads, no button checks, nothing.

This is usually fine for simple sequences, but it's something to be aware of when you want the robot to react to input while it's moving.

------------------------------------------------------------------------

## Common Errors and What They Mean

| Error | What it usually means |
|------------------|-----------------------------------------------------|
| `SyntaxError` | Typo, wrong indentation, or mismatched parentheses/quotes |
| `NameError: name 'x' is not defined` | You used a variable or function before defining/importing it |
| `TypeError` | You passed the wrong type (e.g., a string where a number is expected) |
| `IndentationError` | Your indentation is inconsistent |

When something goes wrong, read the error message and look at the line number it points to (or the line right before) — that's almost always where the problem is.