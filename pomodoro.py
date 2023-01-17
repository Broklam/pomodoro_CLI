import tkinter as tk


class Pomodoro:
    def __init__(self):
        self.running = False
        self.minutes = 25
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.label = tk.Label(text="25:00", font=("Helvetica", 140))
        self.label.pack()
        self.start_button = tk.Button(text="Start", font=("Helvetica", 35), command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(text="Stop", command=self.stop, state='disabled', font=("Helvetica", 35))
        self.stop_button.pack()
        self.reset_button = tk.Button(text="Reset", command=self.reset, font=("Helvetica", 35))
        self.reset_button.pack()
        self.time_button = tk.Button(text="Change Time", command=self.change_time, font=("Helvetica", 35))
        self.time_button.pack()
        self.root.mainloop()

    def start(self):
        self.running = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.seconds = self.minutes * 60
        self.countdown()

    def stop(self):
        self.running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def reset(self):
        self.minutes = 25
        self.label.config(text="25:00")

    def change_time(self):
        self.minutes = int(input("Enter new time in minutes: "))
        self.label.config(text="{}:00".format(str(self.minutes).zfill(2)))

    def countdown(self):
        if self.running:
            m, s = divmod(self.seconds, 60)
            self.label.config(text="{}:{}".format(str(m).zfill(2), str(s).zfill(2)))
            self.seconds -= 1
            if self.seconds > 0:
                self.root.after(1000, self.countdown)
            else:
                self.running = False
                self.start_button.config(state='normal')
                self.stop_button.config(state='disabled')
                self.root.bell()


if __name__ == "__main__":
    Pomodoro()
