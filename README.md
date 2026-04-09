# 🔘 Raspberry Pi Push Button Interface

A beginner-friendly project demonstrating **4 different ways** to interface a push button with Raspberry Pi using Python and the `RPi.GPIO` library.

---

## 📌 About

Whether you're learning GPIO basics or brushing up on hardware interfacing concepts — this project covers everything from simple level triggering to edge detection techniques using a single push button on GPIO Pin 17.

---

## 🧠 Concepts Covered

| File | Concept | Description |
|------|---------|-------------|
| `PULL_UP_LEVEL_TRIGGERING.py` | Pull-Up Level Triggering | Button reads HIGH by default, LOW when pressed |
| `PULL_DOWN_LEVEL_TRIGGERING.py` | Pull-Down Level Triggering | Button reads LOW by default, HIGH when pressed |
| `FALLING_EDGE.py` | Falling Edge Detection | Detects the exact moment button is pressed (HIGH → LOW) |
| `RAISING_EDGE.py` | Rising Edge Detection | Detects the exact moment button is released (LOW → HIGH) |

---

## 🛠️ Hardware Required

- Raspberry Pi (any model with GPIO)
- Push Button (Tactile Switch)
- Jumper Wires
- Breadboard (optional)

### 📌 Pin Connection

```
Button  →  GPIO Pin 17 (BCM)
Button  →  GND
```

> Internal Pull-Up / Pull-Down resistors are used — no external resistors needed!

---

## 💻 Software Requirements

**Python 3** and the RPi.GPIO library:

```bash
pip install RPi.GPIO
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/raspberry-pi-button-interface.git
cd raspberry-pi-button-interface
```

Run any file:

```bash
python3 PULL_UP_LEVEL_TRIGGERING.py
python3 PULL_DOWN_LEVEL_TRIGGERING.py
python3 FALLING_EDGE.py
python3 RAISING_EDGE.py
```

> Press `Ctrl + C` to stop the program at any time.

---

## 📂 Project Structure

```
raspberry-pi-button-interface/
├── PULL_UP_LEVEL_TRIGGERING.py
├── PULL_DOWN_LEVEL_TRIGGERING.py
├── FALLING_EDGE.py
├── RAISING_EDGE.py
└── README.md
```

---

## 🔍 How It Works

### Pull-Up Level Triggering
The internal pull-up resistor keeps the pin HIGH. When the button is pressed, the pin goes LOW. The program continuously reads the pin state (polling).

### Pull-Down Level Triggering
The internal pull-down resistor keeps the pin LOW. When the button is pressed, the pin goes HIGH. The program continuously reads the pin state (polling).

### Falling Edge Detection
Uses a software flag to detect only the **transition** from HIGH to LOW (button press moment). Prevents repeated detection while the button is held down.

### Rising Edge Detection
Uses a software flag to detect only the **transition** from LOW to HIGH (button release moment). Prevents repeated detection while the button is held down.

---

## 📚 What You'll Learn

- GPIO input configuration in Raspberry Pi
- Difference between Pull-Up and Pull-Down resistors
- Level Triggering vs Edge Detection
- Debouncing concepts using software flags
- Graceful program exit with `KeyboardInterrupt` and `GPIO.cleanup()`

---

## 🧑‍💻 Author

Made with ❤️ using Raspberry Pi & Python

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
