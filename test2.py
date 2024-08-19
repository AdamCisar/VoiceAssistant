import tkinter as tk
import threading
from pubsub import pub
import time

popup_label = None
root = None

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = tk.Label(self, text="Jarvis")
        self.label.pack(side="top", fill="both", expand=True)

    def listener(self, plot_data):
        # Schedule GUI update on the main thread
        self.parent.after(0, self._update_label, plot_data)

    def _update_label(self, plot_data):
        self.label.configure(text=plot_data)

class WorkerThread(threading.Thread):
    def __init__(self):
        super(WorkerThread, self).__init__()
        self.daemon = True
        self._stop = False

    def updateText(self, text):
        pub.sendMessage('listener', plot_data=text)


def init():
    global popup_label
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 100
    x = screen_width - window_width - 30
    y = screen_height - window_height - 60
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg='#333333')

    popup_label = tk.Label(root, text='ssassa', bg='#333333', fg='#FFFFFF', font=('Arial', 14, 'bold'), wraplength=window_width-20)
    popup_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    root.tk_setPalette(background='#333333')
    root.after(3000, root.destroy)

    main = MainApplication(root)
    main.pack(side="top", fill="both", expand=True)

    pub.subscribe(main.listener, 'listener')
            
    wt = WorkerThread()
    wt.start()

    root.mainloop()
    return wt