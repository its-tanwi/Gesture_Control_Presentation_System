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
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the application:

```bash
python GesturePresentationControl.py
```
# 📌 Requirements

- Python 3.7+
- Webcam (laptop camera or smartphone via DroidCam)
- Python Libraries:
  - `opencv-python`
  - `mediapipe`
  - `pyautogui`
  - `numpy`

> ✅ All dependencies are listed in `requirements.txt`

---

## 🧰 Target Audience

- 🎙️ **Presenters and Educators** for smooth slide control
- 🤖 **Tech Enthusiasts** exploring gesture interfaces
- 🧠 **Accessibility Advocates** building inclusive tools
- 💻 **Developers and Researchers** working on Human-Computer Interaction

---

## 💡 Commercial Potential

- ✋ **Touchless Interfaces**: Future-ready HCI design
- 🎮 **Gaming Integration**: Immersive, motion-based control
- 🧑‍🦼 **Assistive Technology**: Helps users with mobility challenges
- 🧑‍🏫 **Corporate Presentation Tools**: Hands-free control in meetings

---

## 👩‍💻 Author

**Tanwi Tejeswani**  
📫 [tanwitejeswani@gmail.com](mailto:tanwitejeswani@gmail.com)  
🔗 [GitHub](https://github.com/its-tanwi)  
🔗 [LinkedIn](https://www.linkedin.com/in/tanwi-tejeswani-73a456301/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it.

---

## 🌟 Like This Project?

If you found this project useful or inspiring,  
**don’t forget to give it a ⭐ on GitHub!**






