import cv2
from tkinter import Tk, Label, Button, Canvas, filedialog
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root, video_source=None):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("800x600") 
        self.root.configure(bg='#F0F0F0')

        self.video_source = video_source
        self.cap = None

        self.title_label = Label(root, text="Video Player", font=("Helvetica", 24, "bold"), bg='#F0F0F0')
        self.title_label.pack(pady=10)

        self.canvas = Canvas(root, bg='black', width=640, height=480)
        self.canvas.pack()

        self.label = Label(root, text="Tekan 'Play' Untuk Memulai Video", font=("Helvetica", 12), bg='#F0F0F0')
        self.label.pack()

        self.play_button = Button(root, text="Play", command=self.play_video, font=("Helvetica", 12))
        self.play_button.pack(side="left", padx=10)

        self.pause_button = Button(root, text="Pause", state="disabled", command=self.pause_video, font=("Helvetica", 12))
        self.pause_button.pack(side="left", padx=10)

        self.choose_button = Button(root, text="Pilih Video", command=self.choose_video, font=("Helvetica", 12))
        self.choose_button.pack(side="left", padx=10)

        self.update()
        self.root.mainloop()

    def play_video(self):
        if self.video_source:
            self.cap = cv2.VideoCapture(self.video_source)
            self.play_button.config(state="disabled")
            self.pause_button.config(state="active")
            self.label.config(text="Playing...")

    def pause_video(self):
        if self.cap:
            self.cap.release()
            self.play_button.config(state="active")
            self.pause_button.config(state="disabled")
            self.label.config(text="tekan 'Play' untuk melanjutkan")

    def update(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
        self.root.after(10, self.update)

    def choose_video(self):
        file_path = filedialog.askopenfilename(title="Select Video", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_source = file_path
            self.play_video()

if __name__ == "__main__":
    root = Tk()
    player = VideoPlayer(root)
