import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import ttkthemes


def message(message, width=300, height=150, margin_top=10, margin_bottom=10, margin_left=15, margin_right=15, font_size=12):
    root = tk.Tk()
    root.title("")
    fontstyle = Font(size=font_size)
    root.overrideredirect(True)
    root.wm_attributes('-topmost', 1)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_top = int((screen_width / 2) - (width / 2))
    window_left = int((screen_height / 2) - (height / 2))
    root.geometry(f'{width}x{height}+{window_top}+{window_left}')
    window = ttk.Frame(root)
    label = ttk.Label(window, text=message, font=fontstyle)
    button = ttk.Button(window, text="确定", command=lambda: root.destroy())
    style = ttkthemes.ThemedStyle(window)
    style.set_theme('arc')
    ttk.Frame(window, width=margin_left).pack(side=tk.LEFT)
    ttk.Frame(window, width=margin_right).pack(side=tk.RIGHT)
    ttk.Frame(window, height=margin_bottom).pack(side=tk.BOTTOM)
    ttk.Frame(window, height=margin_top).pack(side=tk.TOP)
    label.pack()
    button.pack(side=tk.BOTTOM)
    window.place(x=0, y=0, width=width, height=height)
    root.mainloop()
