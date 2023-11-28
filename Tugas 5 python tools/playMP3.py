import pygame
from tkinter import Tk, Button, Label, Scale
import threading
import time

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        pygame.init()
        pygame.mixer.init()

        self.playing = False
        self.duration = 0

        self.label_timer = Label(root, text="0:00")
        self.label_timer.pack(pady=10)

        self.scale_timer = Scale(root, from_=0, to=100, orient="horizontal", length=300, showvalue=0, command=self.set_timer)
        self.scale_timer.pack(pady=10)

        self.button_play = Button(root, text="Play", command=self.play_pause)
        self.button_play.pack(side="left", padx=5)

        self.button_pause = Button(root, text="Pause", state="disabled", command=self.play_pause)
        self.button_pause.pack(side="left", padx=5)

        # Ganti path file musik dengan path yang sesuai di komputer Anda
        self.music_path = "jsong.mp3"

        # Thread untuk mengupdate timer secara real-time
        self.timer_thread = threading.Thread(target=self.update_timer, daemon=True)
        self.timer_thread.start()

    def play_pause(self):
        if not self.playing:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play()
            self.duration = pygame.mixer.Sound(self.music_path).get_length()
            self.button_play.config(state="disabled")
            self.button_pause.config(state="active")
        else:
            pygame.mixer.music.pause()
            self.button_play.config(state="active")
            self.button_pause.config(state="disabled")

        self.playing = not self.playing

    def set_timer(self, value):
        if not self.playing:
            pygame.mixer.music.set_pos(float(value) / 100)

    def update_timer(self):
        while True:
            if self.playing:
                elapsed_time = pygame.mixer.music.get_pos() / 1000
                minutes = int(elapsed_time // 60)
                seconds = int(elapsed_time % 60)
                self.label_timer.config(text=f"{minutes}:{seconds:02}")
            time.sleep(1)

# Membuat jendela Tkinter
root = Tk()
root.geometry("400x200")

# Membuat objek MusicPlayer
music_player = MusicPlayer(root)

# Menjalankan jendela Tkinter
root.mainloop()
