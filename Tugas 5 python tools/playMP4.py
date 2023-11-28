import cv2
from tkinter import Tk, Label, Button, Canvas
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root, video_source=0):
        self.root = root
        self.root.title("Video Player")

        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        self.canvas = Canvas(root)
        self.canvas.pack()

        self.label = Label(root, text="Press 'Play' to start the video")
        self.label.pack()

        self.play_button = Button(root, text="Play", command=self.play_video)
        self.play_button.pack(side="left", padx=5)

        self.pause_button = Button(root, text="Pause", state="disabled", command=self.pause_video)
        self.pause_button.pack(side="left", padx=5)

        self.update()
        self.root.mainloop()

    def play_video(self):
        self.cap = cv2.VideoCapture(self.video_source)
        self.play_button.config(state="disabled")
        self.pause_button.config(state="active")
        self.label.config(text="Playing...")

    def pause_video(self):
        self.cap.release()
        self.play_button.config(state="active")
        self.pause_button.config(state="disabled")
        self.label.config(text="Press 'Play' to resume")

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
        self.root.after(10, self.update)

# Ganti video_source dengan path file video atau 0 untuk menggunakan kamera
video_source = "PBO.mp4"
root = Tk()
player = VideoPlayer(root, video_source)
