# 🤚🎵 Hand–Music Control

A Python-based real-time hand-gesture music controller that lets you play, pause, skip, and control music using just your webcam and hand movements.

---

## 🎯 Project Overview

This project uses **MediaPipe**, **OpenCV**, and **Pygame** to detect hand gestures and map them to music playback actions. Once a hand gesture is recognized, the corresponding command (like play/pause, next, previous, volume control) is executed in real-time — no touch required.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **MediaPipe** – for hand landmark detection  
- **OpenCV** – for webcam input and gesture visualization  
- **Pygame** – for audio playback  
- **Imutils** (optional) – for image utilities and hand counting

All dependencies are listed in `requirements.txt`.

---

## 🔧 Features

- Real-time hand gesture detection and classification  
- Gesture-to-music playback mapping:
  - **Play/Pause**
  - **Next Track / Previous Track**
  - **Volume Up / Volume Down**
  - **Stop**
- Visual feedback: landmarks and gesture name overlaid on video feed  
- Lightweight and easy-to-run on laptops/desktops  

---

## 🚀 Installation & Usage

 ### Clone the repo:  
   ```bash
   git clone https://github.com/harshits2003/Hand-Music-Control.git
   cd Hand-Music-Control
   ```
### Install Dependencies:
```bash
pip install -r requirements.txt
```
## 🗂️ Gesture-to-Action Mapping

| Gesture      | Action              |
|--------------|---------------------|
| 1 Finger     | Play / Resume       |
| 2 Fingers    | Pause               |
| 3 Fingers    | Next Track          |
| 4 Fingers    | Previous Track      |
| 5 Fingers    | Stop Track / Exit   |

> Feel free to customize these mappings in `main.py` as needed.

---

## 📈 Demo & Related Projects

This repo is inspired by and structured similar to other Python gesture-music controllers using **MediaPipe** and **Pygame**:

- [Control Music with Hand Gestures – YouTube Demo](https://www.youtube.com/watch?v=mIitdT-ZVxE)
- [Reddit: Gesture-controlled music player app for Mac](https://www.reddit.com/r/macapps/comments/i4w9o7/i_made_a_mac_app_that_lets_you_control_your_music/)
- [GitHub: Hand Gesture Music Player by @Sgvkamalakar](https://github.com/Sgvkamalakar/Hand-Gesture-Music-Player)
- [GitHub: Gesture Controlled Music Player by @AbdulBasit-MrRobo](https://github.com/AbdulBasit-MrRobo/Hand-Gesture-Controlled-Music-Player)

---

## 🔮 Future Enhancements

- Add **volume control** with pinch/open-hand gestures  
- Support **custom gesture-action mapping** via config file  
- Integrate with **Spotify**, **VLC**, and other media players  
- Build a **simple GUI** to display current song, gesture history, and logs  

---

## 📝 Contributing

Contributions, issue reports, and feature suggestions are welcome!  
Fork the repo and open a PR — I’d love to make this even more fun and reliable.

---

## 📜 License

This project is released under the **MIT License**.  


   
