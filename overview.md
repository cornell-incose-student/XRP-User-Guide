# Overview of the XRP Robot

The XRP is a small and inexpensive robot designed for learning about programming FIRST Robotics Competition (FRC) robots. All the same tools used for programming full-sized FRC robots can be used to program the XRP.

**XRP** stands for **Experiential Robotics Platform**, developed by FIRST, DEKA, SparkFun, Raspberry Pi, STMicroelectronics, DigiKey, WPI, and Cornell. Costing about the same as a K-12 textbook, the XRP is used in 180+ countries.

The XRP comes with two drive motors with integrated wheel encoders, and an IMU sensor for measuring headings and accelerations. Programming it is as simple as writing a robot program and running it from your computer.

------------------------------------------------------------------------

## Rationale: Why an XRP Robot Competition?

-   **Systems engineering in practice** — Students experience the full engineering cycle: defining problems, designing solutions, building prototypes, testing, and refining.
-   **Teamwork and project management** — Collaborate in teams, divide responsibilities, communicate ideas, and coordinate tasks.
-   **Multidisciplinary experience** — Work with electronics, mechanical components, and programming. Learn how hardware and software integrate into a complete system.
-   **Customer-focused design** — Listen to requirements, translate needs into technical solutions, and make design decisions based on constraints (cost, performance, reliability).
-   **Problem-solving and creativity** — Learn from challenges, improve through iteration, and build confidence.
-   **Engaging and fun** — Combines rigorous learning with hands-on excitement.

------------------------------------------------------------------------

## Key Resources

-   [Experiential Inc. — Get Started](https://www.experiential.inc/get-started)
-   [SparkFun XRP Page](https://www.sparkfun.com/products/22230)
-   [XRP Users Guide (Full Documentation)](https://xrpusersguide.readthedocs.io/en/latest/)
-   [XRP Code Editor](https://xrpcode.wpi.edu/)
-   [XRP Community Forum](https://xrpforum.wpi.edu/)
-   [Experiential Robotics Platform (XRP)](https://xrp.wpi.edu/)
-   [WPILib FRC Guide](https://docs.wpilib.org/en/stable/)
-   [XRP Board Guide](https://docs.sparkfun.com/SparkFun_XRP_Controller/)

------------------------------------------------------------------------

## Kit Components

Your XRP kit includes:

| Component | Description |
|------------------------|------------------------------------------------|
| **XRP Controller Board** | Raspberry Pi Pico W, built-in 6-axis IMU (accelerometer + gyroscope), Qwiic connector, user push-button, RGB indicator LED |
| **Chassis Set** | Snap-together plastic frame (tool-free). Lego-compatible. |
| **2 Motors with Encoders** | Drive left and right wheels. Encoders measure rotation. Spin CW or CCW at various speeds. |
| **1 Servo Motor** | Controls position within a limited range. Lego-compatible hub. |
| **Ultrasonic Distance Sensor** | Measures distance using sound waves. Mounts on front to detect obstacles. |
| **IR Reflectance Sensor Board** | Two infrared sensors for line-following. |
| **Color Sensor (TCS-34725)** | Detects and reports RGB color values via Qwiic connector. |
| **Touch Sensor / Button** | Large push-button for user input or bump detection. |
| **Battery Holder** | 4 AA battery pack with barrel plug connector. |

![Labeled diagram of the XRP Controller Board](images/image18.png)

------------------------------------------------------------------------

## Assembly

Watch the **XRP Assembly and Software Starter Guide** (video) for the standard chassis build. Start at \~1:15 for the "Hardware Assembly" section.

> <span style="color: red;">**REVIEW NOTE:**</span> Add or link to Lego-compatible assembly instructions specific to this kit version. Check if there are updated assembly photos for the red robot.

**Tip:** Watch the full video first, then go back and assemble along with it. The segments are short and you'll feel more comfortable knowing what comes next.

------------------------------------------------------------------------

## A Note on Robot Versions

You may see references to two different XRP versions online: the **older grey/beta version** and the **newer red version** (which you have). Key differences:

-   The red version uses a **SparkFun XRP Controller with RP2350B dual-core processor** (upgraded from the beta's RP2040).
-   The board orientation is **upright** in the Lego-compatible version (vs. flat/horizontal in older versions). This affects IMU-based commands — see the [IMU section in Programming](programming.md#an-aside-about-the-imu--driving-straight).
-   The red version has a **full-color RGB LED** (not just a green indicator), additional Qwiic connectors, and four servo headers.

Many online tutorials and the XRP Users Guide may show the grey robot. The core programming concepts are the same, but board labels and some pin configurations may differ.

> <span style="color: red;">**REVIEW NOTE:**</span> Manually verify the exact hardware differences between the grey beta and red release version. Confirm RP2350B vs RP2040 for the specific kits being used.
