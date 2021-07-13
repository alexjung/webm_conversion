"""
Author: Konstantin (k0nze) Lübeck
License: BSD 3-Clause License
Copyright (c) 2020 Konstantin (k0nze) Lübeck
"""

try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk


from consts import *
from about_dialog import AboutDialog

import copy

class MainWindow(Tk.Frame):
    def __init__(self, model, root):

        self.model = model
        self.model.register_observer(self)

        self.root = root
        #self.root.minsize(200, 300)

        Tk.Frame.__init__(self, self.root)

        self.pack(fill="both", expand=True)

        self.menubar = Tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        
        # file menu
        file_menu = Tk.Menu(self.menubar)
        file_menu.add_command(label="About", command=self.on_about)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        self.menubar.add_cascade(label="File", menu=file_menu)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

        input_output_file_frame = Tk.Frame(self)
        input_output_file_frame.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=0, column=0, columnspan=3, padx=5, pady=5)

        input_output_file_frame.columnconfigure(1, weight=1)

        # input file label
        input_file_path_entry_label = Tk.Label(input_output_file_frame, text="Input File:")
        input_file_path_entry_label.grid(sticky=Tk.W, row=0, column=0, padx=10) 

        self.input_file_path = Tk.StringVar() 
        # TODO
        self.input_file_path.set("/test/test")
        input_file_path_entry = Tk.Entry(input_output_file_frame, textvariable=self.input_file_path, state='readonly', justify=Tk.LEFT).grid(sticky=Tk.E+Tk.W, row=0, column=1, padx=10)

        # input file selection button
        input_file_selection_button = Tk.Button(input_output_file_frame, text="Open Input File", command=self.on_select_input_file).grid(sticky=Tk.W, row=0, column=2, padx=10)


        # input file label
        output_file_path_entry_label = Tk.Label(input_output_file_frame, text="Output File:")
        output_file_path_entry_label.grid(sticky=Tk.W, row=1, column=0, padx=10) 

        self.output_file_path = Tk.StringVar() 
        # TODO
        self.output_file_path.set("/test/test")
        input_file_path_entry = Tk.Entry(input_output_file_frame, textvariable=self.output_file_path, state='readonly', justify=Tk.LEFT).grid(sticky=Tk.E+Tk.W, row=1, column=1, padx=10)

        # input file selection button
        input_file_selection_button = Tk.Button(input_output_file_frame, text="Select", command=self.on_select_input_file).grid(sticky=Tk.W, row=1, column=2, padx=10)





        # ffmpeg log
        ffmpeg_log_frame = Tk.LabelFrame(self, text="FFmpeg Log")
        ffmpeg_log_frame.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=1, column=0, columnspan=3, padx=5, pady=5)

        ffmpeg_log_frame.rowconfigure(0, weight=1)
        ffmpeg_log_frame.columnconfigure(0, weight=1)

        ffmpeg_log_text = Tk.Text(ffmpeg_log_frame)
        ffmpeg_log_text.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=0, column=0, padx=5, pady=5)

    def on_select_input_file(self):
        print("open input file")

    def on_select_output_file(self):
        print("open output file")

    def on_convert_output_file(self):
        print("open output file")

    def notify(self):
        pass

    def on_about(self):
        about_dialog = AboutDialog(self.root)

        # make window modal
        about_dialog.wait_visibility()
        about_dialog.focus_set()
        about_dialog.grab_set()
        about_dialog.transient(self.root)
