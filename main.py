from tkinter import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x150')
        self.resizable(False, False)
        self.title('Sistema Especialista de Diagnóstico Médico')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        doencaum = tk.StringVar()
        doencadois = tk.StringVar()

        # heading
        heading = ttk.Label(self, text='Sintomas', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # doencaum
        doencaum_label = ttk.Label(self, text="doencaum:")
        doencaum_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        doencaum_entry = ttk.Entry(self, textvariable=doencaum, **entry_font)
        doencaum_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        
		# doencaum
        doencadois_label = ttk.Label(self, text="doencadois:")
        doencadois_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        doencadois_entry = ttk.Entry(self, textvariable=doencadois, **entry_font)
        doencadois_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))


if __name__ == "__main__":
    app = App()
    app.mainloop()