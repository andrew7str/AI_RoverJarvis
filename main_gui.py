import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
from ai_engine import get_response
from voice_input import listen
from speech_output import speak

class DogAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dog Assistant")

        self.label = tk.Label(root)
        self.label.pack()

        self.load_animation("assets/dog_idle.gif")

        self.listen_button = tk.Button(root, text="Tanya AI", command=self.ask_ai)
        self.listen_button.pack(pady=10)

    def load_animation(self, path):
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(path))]
        self.anim_index = 0
        self.animate()

    def animate(self):
        self.label.configure(image=self.frames[self.anim_index])
        self.anim_index = (self.anim_index + 1) % len(self.frames)
        self.root.after(100, self.animate)

    def ask_ai(self):
        threading.Thread(target=self.handle_question).start()

    def handle_question(self):
        speak("Silakan bertanya...")
        question = listen()
        response = get_response(question)
        speak(response)

if __name__ == "__main__":
    root = tk.Tk()
    app = DogAssistantGUI(root)
    root.mainloop()
