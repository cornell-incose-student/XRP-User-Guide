# Troubleshooting & FAQ

## Connection Issues

| Problem | Solution |
|---|---|
| XRP won't connect via USB | Try a different USB cable. Check that the power switch is on. Press the reset button. Try a different USB port on your computer. |
| XRP doesn't respond after connecting | Press reset. Make sure batteries are fresh. Check that no other tab/program is using the serial connection. |

---

## Bluetooth Issues

| Problem | Solution |
|---|---|
| Robot name doesn't appear in pairing list | Turn the robot off, close the PestoLink tab, turn the robot back on, reopen the tab, and try again. This is common on first connection. |
| Bluetooth connects but can't drive | Ensure `pestolink.py` is in `/lib/` and `pestolink_example.py` was the last file you ran. Try pressing reset on the XRP. |
| Connection drops when USB is removed | Ensure batteries are fresh (voltage > 5.1V). Some computers have weaker Bluetooth — try moving closer to the robot. |
| "Error connecting to the XRP" message | Refresh the PestoLink page. Press reset on the XRP. Ensure only one Chrome tab is trying to connect. |
| PestoLink doesn't work in Edge/Firefox/Safari | Web Bluetooth is a Chrome-specific feature. You must use Chrome. |
| Robot was previously paired but won't reconnect | Go to your computer's Bluetooth settings and "Forget" the device, then pair again from PestoLink. |

---

## Sensor Issues

| Problem | Solution |
|---|---|
| Ultrasonic reads 65535 constantly | Swap the blue and yellow data wires at the sensor end. |
| Sensors return unexpected values | Verify cables are in the correct ports: reflectance → "Line", ultrasonic → "Dist." Check for loose connections. |
| Robot doesn't drive straight | This is normal! See the IMU section. Use encoders and sensor feedback rather than relying on open-loop driving. |
| Robot handheld and wheels won't stop spinning | The IMU-based turn commands expect a heading change that can't happen when held. Put the robot on the ground. |

---

## Software Issues

| Problem | Solution |
|---|---|
| Robot won't stop or just spinning | Turn off the XRP, then reload the web editor page. |
| Really weird robot behavior | Change batteries first. If still weird, check your code for infinite loops without exit conditions. |
| Program too long / hard to manage | Split into modules. See Skill 7 in the [Programming](programming.md) section. |

---

## Factory Reset (Last Resort)

> **Warning:** This erases everything on the XRP. Save a local copy of your code first!

1. **Enter storage mode:** Connect XRP via USB. Hold the **BOOT** button (blue), then press **RESET** (green), then release BOOT. A file explorer window should appear.
2. **Flash nuke:** Download `universal_flash_nuke.uf2` from [this repo](https://github.com/Gadgetoid/pico-universal-flash-nuke/releases/tag/v1.0.1) and copy it into the XRP storage device. It will auto-restart.
3. **Re-enter storage mode:** Hold **BOOT**, press **RESET**, release BOOT again.
4. **Reinstall MicroPython:** Download the MicroPython `.uf2` for **RP2 — Raspberry Pi Pico 2 — V1.25.0** from [micropython.org](https://micropython.org/download/RPI_PICO2/) and copy it into the XRP storage device. It will auto-restart.
5. **Reconnect:** Go back to the XRP Code Editor and follow prompts to update firmware and libraries.
