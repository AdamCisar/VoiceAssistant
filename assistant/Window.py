import tkinter as tk
import threading

popup_label = None
root = None
thread = None

def showPopup(message):
    global popup_label, root

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

    popup_label = tk.Label(root, text=message, bg='#333333', fg='#FFFFFF', font=('Arial', 14, 'bold'), wraplength=window_width-20)
    popup_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    root.tk_setPalette(background='#333333')
    root.update_idletasks()

    root.after(3000, root.destroy)
    root.mainloop()

def updatePopupMessage(new_message):
    global popup_label
    if popup_label:
        popup_label.after(0, lambda: popup_label.config(text=new_message))

def showPopupInBackground(command: str):
    global thread, popup_label

    if popup_label:
        updatePopupMessage(command)
        return

    thread = threading.Thread(target=showPopup, args=(command,))
    thread.start()
    return thread
