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

## 📂 File Structure

