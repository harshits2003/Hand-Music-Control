import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading
from tkinter import Tk, Canvas

class WaveformGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Hand Music Control")
        self.canvas = Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()
        self.running = True
        threading.Thread(target=self.update_waveform, daemon=True).start()

    def update_waveform(self):
        while self.running:
            data = sd.rec(1024, samplerate=44100, channels=1, dtype='float32', blocking=True)
            self.after(10, self.draw_waveform, data)  # ✅ Schedule UI update on the main thread
            self.root.after(10, self.update_waveform)
            self.canvas.delete("all")
            for i in range(len(data) - 1):
                self.canvas.create_line(i, 200 + data[i][0] * 100, i + 1, 200 + data[i + 1][0] * 100, fill="cyan")
            self.root.update_idletasks()
            self.root.update()

    def stop(self):
        self.running = False
        self.root.destroy()
