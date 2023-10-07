from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
window = Tk()
window.title("Video Player App")
def open_file():
    file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video Files", "*.mp4")])
    play_video(file_path)

def play_video(file_path):
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 2, 1024)
    pygame.display.init()

    movie = pygame.movie.Movie(file_path)
    screen = pygame.display.set_mode(movie.get_size())
    movie.set_display(screen)

    movie.play()

    while movie.get_busy(): 
        pygame.time.delay(100)

    pygame.quit()
open_button = Button(window, text="Open", command=open_file)
open_button.pack()

play_button = Button(window, text="Play", command=lambda: play_video(file_path))
play_button.pack()
window.mainloop()
