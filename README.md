# 🎯 Gesture-Controlled Presentation Navigation

**Gesture-Controlled Presentation Navigation** is a lightweight Python project that enables hands-free control of presentations using hand gestures tracked via **MediaPipe** and interpreted using **PyAutoGUI**.

This tool is ideal for presenters, educators, and accessibility advocates who want to navigate slides and zoom without touching a keyboard or mouse.

---

## ✨ Features

- ✋ **Zoom In**: Spread all fingers open 🖐️
- 🤏 **Zoom Out**: Show "L" shape (Thumb + Index)  
- ☝️ **Page Up**: Raise index finger only  
- ✌️ **Page Down**: Raise index + middle fingers (peace sign)  
- 📱 **Camera Input**: Uses your webcam (DroidCam optional for phone input)
- ⚡ **Real-time Detection**: Powered by MediaPipe with low latency
- 🪟 **Lightweight**: No GUI, minimal dependencies, terminal-based

---

## 🧠 How It Works

The system detects specific hand landmarks using **MediaPipe**, interprets gestures based on finger positions, and sends keyboard events via **PyAutoGUI**.

- Gesture → Interpreted Action → OS Keystroke  
  e.g. ✌️ → `'page_down'` → `pyautogui.press(' ')`

---




## 🚀 Installation

### 1. Clone this repository:
```bash
git clone https://github.com/its-tanwi/gesturecontrolledPresentations.git
cd gesturecontrolledPresentations

---

### 2. Install dependencies:
```bash
pip install -r requirements.txt

---

### 3. Run the application:
```bash
python GesturePresentationControl.py

---

## 🧰 Target Audience
🎙️ Presenters and Educators looking for seamless slide navigation

🤖 Tech Enthusiasts and Developers interested in gesture recognition

🧠 Accessibility Advocates building inclusive interfaces

🎮 Gamers and Researchers exploring HCI or hands-free control systems






