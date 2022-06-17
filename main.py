"""
Copyright (C) 2022, Jie Li

This file is part of ShapeEst3D

ShapeEst3D is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ShapeEst3D is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ShapeEst3D.  If not, see <https://www.gnu.org/licenses/>.
    
Author: Jie Li <lj201112@163.com>, Feb. 2021, modefied on July 2021, March 2022.
License: GPL v 3
"""
#  -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import random
import numpy as np
# from tkinter import filedialog
# from Modules import __init__

def vp_start_gui():
    root = tk.Tk()
    ShapeEstimation(root)
    root.iconbitmap('./Modules/logo.ico')
    # root.attributes("-topmost", True)
    root.update()
    root.lift()
    root.focus_force()
    root.mainloop()
    # root.destroy()


class ShapeEstimation:
    def __init__(self,top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        # _fgcolor = '#000000'  # X11 color: 'black'
        # _compcolor = '#d9d9d9' # X11 color: 'gray85'
        # _ana1color = '#d9d9d9' # X11 color: 'gray85'
        # _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.top = top
        top.geometry("653x405+356+354")
        top.minsize(116, 1)
        top.maxsize(1924, 1062)
        top.resizable(1,  1)
        top.title("ShapeEst3D")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # 左侧的frame notes
        self.notes = tk.Frame(top)
        self.notes.place(relx=0.008, rely=0.012, relheight=0.98, relwidth=0.49)
        self.notes.configure(relief='groove')
        self.notes.configure(borderwidth="2")
        self.notes.configure(relief="groove")
        self.notes.configure(background="#d9d9d9")
        self.notes.configure(highlightbackground="#d9d9d9")
        self.notes.configure(highlightcolor="black")

        # 左侧frame中的文本框
        self.notes_text = tk.Text(self.notes)
        self.notes_text.place(relx=0.0, rely=0.0, relheight=1.005, relwidth=0.997)
        self.notes_text.configure(background="white")
        self.notes_text.configure(font="-family {Arial} -size 10")
        self.notes_text.configure(foreground="black")
        self.notes_text.configure(highlightbackground="#d9d9d9")
        self.notes_text.configure(highlightcolor="black")
        self.notes_text.configure(insertbackground="black")
        self.notes_text.configure(selectbackground="blue")
        self.notes_text.configure(selectforeground="white")
        self.notes_text.configure(wrap="word")
        self.notes_text.insert(tk.END,'Welcome ...\n\nThis program is used to estimate 3D crystal shape from a set of 2D sections by statistical methods.\n=========================')
        self.notes_text.see(tk.END)
        # self.notes_text.configure(state='normal')       
        self.notes_text.insert(tk.END,'\n'+'Single shape estimation activated')
        self.notes_text.insert(tk.END,'\n'+'---------------------------\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')  
        
        # text.configure(state='normal')
        # text.insert('end', 'Some Text')
        # self.notes_text.configure(state='disabled')
        
        self.menu_frame = tk.Frame(top)
        self.menu_frame.place(relx=0.505, rely=0.012, relheight=0.099, relwidth=0.492)
        self.menu_frame.configure(relief='groove')
        self.menu_frame.configure(borderwidth="2")
        self.menu_frame.configure(relief="groove")
        self.menu_frame.configure(background="#d9d9d9")
        self.menu_frame.configure(highlightbackground="#d9d9d9")
        self.menu_frame.configure(highlightcolor="black")
        # self.menu_frame.place_forget()    
        # print(self.menu_frame.place_info())
        # self.menu_frame.pack()
        # self.menu_frame.destroy()

        self.single_shape_button = tk.Button(self.menu_frame,command=self.load_operation_single)
        self.single_shape_button.place(relx=0.016, rely=0.125, height=30, width=100)
        self.single_shape_button.configure(activebackground="#ececec")
        self.single_shape_button.configure(activeforeground="#000000")
        self.single_shape_button.configure(background="#d9d9d9")
        self.single_shape_button.configure(disabledforeground="#a3a3a3")
        self.single_shape_button.configure(font="-family {Arial} -size 10")
        self.single_shape_button.configure(foreground="#000000")
        self.single_shape_button.configure(highlightbackground="#d9d9d9")
        self.single_shape_button.configure(highlightcolor="black")
        self.single_shape_button.configure(pady="0")
        self.single_shape_button.configure(text='Single shape')

        self.multiple_shapes_button = tk.Button(self.menu_frame,command=self.load_opration_multi)
        self.multiple_shapes_button.place(relx=0.343, rely=0.125, height=30, width=100)
        self.multiple_shapes_button.configure(activebackground="#ececec")
        self.multiple_shapes_button.configure(activeforeground="#000000")
        self.multiple_shapes_button.configure(background="#d9d9d9")
        self.multiple_shapes_button.configure(disabledforeground="#a3a3a3")
        self.multiple_shapes_button.configure(font="-family {Arial} -size 10")
        self.multiple_shapes_button.configure(foreground="#000000")
        self.multiple_shapes_button.configure(highlightbackground="#d9d9d9")
        self.multiple_shapes_button.configure(highlightcolor="black")
        self.multiple_shapes_button.configure(pady="0")
        self.multiple_shapes_button.configure(text='Multiple Shapes')
        
        # add message // To do
        self.about_button = tk.Button(self.menu_frame,command=self.about)
        self.about_button.place(relx=0.826, rely=0.125, height=30, width=50)
        self.about_button.configure(activebackground="#ececec")
        self.about_button.configure(activeforeground="#000000")
        self.about_button.configure(background="#d9d9d9")
        self.about_button.configure(disabledforeground="#a3a3a3")
        self.about_button.configure(font="-family {Arial} -size 10 -weight bold")
        self.about_button.configure(foreground="#a50320")
        self.about_button.configure(highlightbackground="#d9d9d9")
        self.about_button.configure(highlightcolor="black")
        self.about_button.configure(pady="0")
        self.about_button.configure(text='About')

        # 右侧single frame
        self.operation_single = tk.Frame(top)
        self.operation_single.place(relx=0.505, rely=0.111, relheight=0.881, relwidth=0.49)
        self.operation_single.configure(relief='groove')
        self.operation_single.configure(borderwidth="2")
        self.operation_single.configure(relief="groove")
        self.operation_single.configure(background="#d9d9d9")
        self.operation_single.configure(highlightbackground="#d9d9d9")
        self.operation_single.configure(highlightcolor="black")

        
        # single_load_file
        self.load_file_button_single = tk.Button(self.operation_single,command=self.load_data_file_single)
        self.load_file_button_single.place(relx=0.031, rely=0.025, height=30, width=99)
        self.load_file_button_single.configure(activebackground="#ececec")
        self.load_file_button_single.configure(activeforeground="#000000")
        self.load_file_button_single.configure(background="#d9d9d9")
        self.load_file_button_single.configure(disabledforeground="#a3a3a3")
        self.load_file_button_single.configure(font="-family {Arial} -size 10")
        self.load_file_button_single.configure(foreground="#000000")
        self.load_file_button_single.configure(highlightbackground="#d9d9d9")
        self.load_file_button_single.configure(highlightcolor="black")
        self.load_file_button_single.configure(pady="0")
        self.load_file_button_single.configure(text='Load data file')

        self.shape_num_label_single = tk.Label(self.operation_single)
        self.shape_num_label_single.place(relx=0.469, rely=0.028, height=30, width=150)
        self.shape_num_label_single.configure(activebackground="#f9f9f9")
        self.shape_num_label_single.configure(activeforeground="black")
        self.shape_num_label_single.configure(background="#d9d9d9")
        self.shape_num_label_single.configure(disabledforeground="#a3a3a3")
        self.shape_num_label_single.configure(font="-family {Arial} -size 10")
        self.shape_num_label_single.configure(foreground="#000000")
        self.shape_num_label_single.configure(highlightbackground="#d9d9d9")
        self.shape_num_label_single.configure(highlightcolor="black")
        self.shape_num_label_single.configure(text='Number of shapes: 1')

        self.method_labelframe_single = tk.LabelFrame(self.operation_single)
        self.method_labelframe_single.place(relx=0.031, rely=0.109, relheight=0.185, relwidth=0.563)
        self.method_labelframe_single.configure(relief='groove')
        self.method_labelframe_single.configure(font="-family {Arial} -size 10")
        self.method_labelframe_single.configure(foreground="black")
        self.method_labelframe_single.configure(text='Method')
        self.method_labelframe_single.configure(background="#d9d9d9")
        self.method_labelframe_single.configure(highlightbackground="#d9d9d9")
        self.method_labelframe_single.configure(highlightcolor="black")
        
        # method radiobutton

        self.method_single_value = tk.StringVar(value='histogram')
        # self.method_single_value.set('histogram')
        self.histogram_select_button_single = tk.Radiobutton(self.method_labelframe_single, text='Histogram', value='histogram', variable=self.method_single_value,command=self.change_method_state_single)
        self.histogram_select_button_single.place(relx=0.017, rely=0.227, relheight=0.364, relwidth=0.494, bordermode='ignore')
        self.histogram_select_button_single.configure(activebackground="#ececec")
        self.histogram_select_button_single.configure(activeforeground="#000000")
        self.histogram_select_button_single.configure(background="#d9d9d9")
        self.histogram_select_button_single.configure(disabledforeground="#a3a3a3")
        self.histogram_select_button_single.configure(font="-family {Arial} -size 10")
        self.histogram_select_button_single.configure(foreground="#000000")
        self.histogram_select_button_single.configure(highlightbackground="#d9d9d9")
        self.histogram_select_button_single.configure(highlightcolor="black")
        self.histogram_select_button_single.configure(justify='left')
        # self.histogram_select_button_single.configure(state='disable')
        
        self.kde_select_button_single = tk.Radiobutton(self.method_labelframe_single, text='Kernel density estimation', value='gaussian_kde', variable=self.method_single_value,command=self.change_method_state_single)
        self.kde_select_button_single.place(relx=0.028, rely=0.545, relheight=0.348, relwidth=0.95, bordermode='ignore')
        self.kde_select_button_single.configure(activebackground="#ececec")
        self.kde_select_button_single.configure(activeforeground="#000000")
        self.kde_select_button_single.configure(background="#d9d9d9")
        self.kde_select_button_single.configure(disabledforeground="#a3a3a3")
        self.kde_select_button_single.configure(font="-family {Arial} -size 10")
        self.kde_select_button_single.configure(foreground="#000000")
        self.kde_select_button_single.configure(highlightbackground="#d9d9d9")
        self.kde_select_button_single.configure(highlightcolor="black")
        self.kde_select_button_single.configure(justify='left')
        # self.kde_select_button_single.configure(state='disable')
        
        # repeat times
        self.repeat_times_labelframe_single = tk.LabelFrame(self.operation_single)
        # self.repeat_times_labelframe_single.place(relx=0.609, rely=0.109, relheight=0.185, relwidth=0.375)
        self.repeat_times_labelframe_single.configure(relief='groove')
        self.repeat_times_labelframe_single.configure(font="-family {Arial} -size 10")
        self.repeat_times_labelframe_single.configure(foreground="black")
        self.repeat_times_labelframe_single.configure(text='Repeat times')
        self.repeat_times_labelframe_single.configure(background="#d9d9d9")
        self.repeat_times_labelframe_single.configure(highlightbackground="#d9d9d9")
        self.repeat_times_labelframe_single.configure(highlightcolor="black")
        
        self.repeat_times_single_value = tk.StringVar()
        self.repeat_times_single_value.set('0')
        self.repeat_times_combobox_single = ttk.Combobox(self.repeat_times_labelframe_single, textvariable=self.repeat_times_single_value, values=[0,20,50,100,200,300,500], state='readonly')
        # self.repeat_times_combobox_single.place(relx=0.267, rely=0.379, relheight=0.394, relwidth=0.467, bordermode='ignore')
        self.repeat_times_combobox_single.configure(background="white")
        # self.repeat_times_combobox_single.configure(disabledforeground="#a3a3a3")
        self.repeat_times_combobox_single.configure(font="-family {Arial} -size 10")
        # self.repeat_times_combobox_single.configure(foreground="#000000")
        # self.repeat_times_combobox_single.configure(highlightbackground="#d9d9d9")
        # self.repeat_times_combobox_single.configure(highlightcolor="black")
        # self.repeat_times_combobox_single.configure(selectbackground="blue")
        # self.repeat_times_combobox_single.configure(selectforeground="white")
        
        # self.repeat_times_combobox_single['values'] = [0,50,100,200,300,500]
        # self.repeat_times_combobox_single.current(0)  
        # self.repeat_times_combobox_single.bind("<<ComboboxSelected>>", self.repeat_time_state)
        # self.repeat_times_combobox_single.configure(state='disable')
        
        self.bin_num_label_single = tk.Label(self.operation_single)
        # self.bin_num_label_single.place(relx=0.031, rely=0.308, height=25, width=232)
        self.bin_num_label_single.configure(activebackground="#f9f9f9")
        self.bin_num_label_single.configure(activeforeground="black")
        self.bin_num_label_single.configure(background="#d9d9d9")
        self.bin_num_label_single.configure(disabledforeground="#a3a3a3")
        self.bin_num_label_single.configure(font="-family {Arial} -size 10")
        self.bin_num_label_single.configure(foreground="#000000")
        self.bin_num_label_single.configure(highlightbackground="#d9d9d9")
        self.bin_num_label_single.configure(highlightcolor="black")
        self.bin_num_label_single.configure(text='Number of bins for histogram method:')

        self.bin_num_single_value = tk.IntVar(value=30)
        # self.bin_num_single_value.set('30')
        self.bin_num_spin_single = tk.Spinbox(self.operation_single, from_=10, to=50, textvariable=self.bin_num_single_value, state='disable')
        # self.bin_num_spin_single.place(relx=0.766, rely=0.308, relheight=0.07, relwidth=0.156)
        self.bin_num_spin_single.configure(background="white")
        self.bin_num_spin_single.configure(font="-family {Arial} -size 10")
        self.bin_num_spin_single.configure(foreground="black")
        self.bin_num_spin_single.configure(highlightbackground="#d9d9d9")
        self.bin_num_spin_single.configure(highlightcolor="black")
        self.bin_num_spin_single.configure(insertbackground="black")
        self.bin_num_spin_single.configure(selectbackground="blue")
        self.bin_num_spin_single.configure(selectforeground="white")
        # self.bin_num_spin_single.configure(state='disable')

        self.best_match_spin_single_value = tk.IntVar(value=5)
        self.best_match_to_calc = int(self.best_match_spin_single_value.get())
        # self.best_match_spin_single_value.set('10')
        self.best_match_spin_single = tk.Spinbox(self.operation_single, from_=1, to=30, textvariable=self.best_match_spin_single_value, justify=tk.CENTER)#, from_=1.0, to=100.0)
        self.best_match_spin_single.place(relx=0.219, rely=0.406, relheight=0.059, relwidth=0.109)
        self.best_match_spin_single.configure(activebackground="#f9f9f9")
        self.best_match_spin_single.configure(background="white")
        self.best_match_spin_single.configure(buttonbackground="#d9d9d9")
        self.best_match_spin_single.configure(disabledforeground="#a3a3a3")
        self.best_match_spin_single.configure(font="-family {Arial} -size 10")
        self.best_match_spin_single.configure(foreground="black")
        self.best_match_spin_single.configure(highlightbackground="black")
        self.best_match_spin_single.configure(highlightcolor="black")
        self.best_match_spin_single.configure(insertbackground="black")
        self.best_match_spin_single.configure(selectbackground="blue")
        self.best_match_spin_single.configure(selectforeground="white")
        # self.best_match_spin_single.configure(state='readonly')      
        
        self.best_match_label0_single = tk.Label(self.operation_single)
        self.best_match_label0_single.place(relx=0.047, rely=0.398, height=24, width=47)
        self.best_match_label0_single.configure(activebackground="#f9f9f9")
        self.best_match_label0_single.configure(activeforeground="black")
        self.best_match_label0_single.configure(background="#d9d9d9")
        self.best_match_label0_single.configure(disabledforeground="#a3a3a3")
        self.best_match_label0_single.configure(font="-family {Arial} -size 10")
        self.best_match_label0_single.configure(foreground="#000000")
        self.best_match_label0_single.configure(highlightbackground="#d9d9d9")
        self.best_match_label0_single.configure(highlightcolor="black")
        self.best_match_label0_single.configure(text='Get the')

        self.best_match_label1_single = tk.Label(self.operation_single)
        self.best_match_label1_single.place(relx=0.344, rely=0.398, height=24, width=207)
        self.best_match_label1_single.configure(activebackground="#f9f9f9")
        self.best_match_label1_single.configure(activeforeground="black")
        self.best_match_label1_single.configure(background="#d9d9d9")
        self.best_match_label1_single.configure(disabledforeground="#a3a3a3")
        self.best_match_label1_single.configure(font="-family {Arial} -size 10")
        self.best_match_label1_single.configure(foreground="#000000")
        self.best_match_label1_single.configure(highlightbackground="#d9d9d9")
        self.best_match_label1_single.configure(highlightcolor="black")
        self.best_match_label1_single.configure(text='best-match results by RMSE')

        self.get_params_button_single = tk.Button(self.operation_single, command=self.get_parameters_single)
        self.get_params_button_single.place(relx=0.063, rely=0.493, height=30, width=120)
        self.get_params_button_single.configure(activebackground="#ececec")
        self.get_params_button_single.configure(activeforeground="#000000")
        self.get_params_button_single.configure(background="#d9d9d9")
        self.get_params_button_single.configure(disabledforeground="#a3a3a3")
        self.get_params_button_single.configure(font="-family {Arial} -size 10")
        self.get_params_button_single.configure(foreground="#0000ff")
        self.get_params_button_single.configure(highlightbackground="#d9d9d9")
        self.get_params_button_single.configure(highlightcolor="black")
        self.get_params_button_single.configure(pady="0")
        self.get_params_button_single.configure(text='Get parameters')
        # self.get_params_button_single.configure(state='disable')

        self.run_button_single = tk.Button(self.operation_single,command=self.run_single)
        self.run_button_single.place(relx=0.559, rely=0.493, height=30, width=120)
        self.run_button_single.configure(activebackground="#ececec")
        self.run_button_single.configure(activeforeground="#000000")
        self.run_button_single.configure(background="#d9d9d9")
        self.run_button_single.configure(disabledforeground="#a3a3a3")
        self.run_button_single.configure(font="-family {Arial} -size 10")
        self.run_button_single.configure(foreground="#008000")
        self.run_button_single.configure(highlightbackground="#d9d9d9")
        self.run_button_single.configure(highlightcolor="black")
        self.run_button_single.configure(pady="0")
        self.run_button_single.configure(text='Run')
        # self.run_button_single.configure(state='disable')

        self.view_results_button_single = tk.Button(self.operation_single,command=self.open_view_result_single)
        self.view_results_button_single.place(relx=0.063, rely=0.602, height=30, width=120)
        self.view_results_button_single.configure(activebackground="#ececec")
        self.view_results_button_single.configure(activeforeground="#000000")
        self.view_results_button_single.configure(background="#d9d9d9")
        self.view_results_button_single.configure(disabledforeground="#a3a3a3")
        self.view_results_button_single.configure(font="-family {Arial} -size 10")
        self.view_results_button_single.configure(foreground="#000000")
        self.view_results_button_single.configure(highlightbackground="#d9d9d9")
        self.view_results_button_single.configure(highlightcolor="black")
        self.view_results_button_single.configure(pady="0")
        self.view_results_button_single.configure(text='''View results''')
        # self.view_results_button_single.configure(state='disable')

        self.calculate_average_labelframe_single = tk.LabelFrame(self.operation_single)
        # self.calculate_average_labelframe_single.place_forget()
        self.calculate_average_labelframe_single.place(relx=0.063, rely=0.686, relheight=0.294, relwidth=0.906)
        self.calculate_average_labelframe_single.configure(relief='groove')
        self.calculate_average_labelframe_single.configure(font="-family {Arial} -size 10")
        self.calculate_average_labelframe_single.configure(foreground="black")
        self.calculate_average_labelframe_single.configure(text='''Calculate the average of the results''')
        self.calculate_average_labelframe_single.configure(background="#d9d9d9")
        self.calculate_average_labelframe_single.configure(highlightbackground="#d9d9d9")
        self.calculate_average_labelframe_single.configure(highlightcolor="black")

        self.average_calc_button_single = tk.Button(self.calculate_average_labelframe_single, command=self.average_calc_single)
        self.average_calc_button_single.place(relx=0.052, rely=0.524, height=26, width=66, bordermode='ignore')
        self.average_calc_button_single.configure(activebackground="#ececec")
        self.average_calc_button_single.configure(activeforeground="#000000")
        self.average_calc_button_single.configure(background="#d9d9d9")
        self.average_calc_button_single.configure(disabledforeground="#a3a3a3")
        self.average_calc_button_single.configure(font="-family {Arial} -size 10")
        self.average_calc_button_single.configure(foreground="#000000")
        self.average_calc_button_single.configure(highlightbackground="#d9d9d9")
        self.average_calc_button_single.configure(highlightcolor="black")
        self.average_calc_button_single.configure(pady="0")
        self.average_calc_button_single.configure(text='Calculate')

        self.match_range0_single = tk.Label(self.calculate_average_labelframe_single)
        self.match_range0_single.place(relx=0.017, rely=0.219, height=23, width=37, bordermode='ignore')
        self.match_range0_single.configure(activebackground="#f9f9f9")
        self.match_range0_single.configure(activeforeground="black")
        self.match_range0_single.configure(background="#d9d9d9")
        self.match_range0_single.configure(disabledforeground="#a3a3a3")
        self.match_range0_single.configure(font="-family {Arial} -size 10")
        self.match_range0_single.configure(foreground="#000000")
        self.match_range0_single.configure(highlightbackground="#d9d9d9")
        self.match_range0_single.configure(highlightcolor="black")
        self.match_range0_single.configure(text='from')

        self.match_range_entry0_single_value = tk.IntVar(value=1)
        self.match_range_entry0_single = tk.Entry(self.calculate_average_labelframe_single,exportselection=0, textvariable=self.match_range_entry0_single_value)
        self.match_range_entry0_single.place(relx=0.138, rely=0.219, relheight=0.2, relwidth=0.08, bordermode='ignore')
        # self.match_range_entry0_single.configure(activebackground="#f9f9f9")
        self.match_range_entry0_single.configure(background="white")
        # self.match_range_entry0_single.configure(buttonbackground="#d9d9d9")
        self.match_range_entry0_single.configure(disabledforeground="#a3a3a3")
        self.match_range_entry0_single.configure(font="-family {Arial} -size 10")
        self.match_range_entry0_single.configure(foreground="black")
        self.match_range_entry0_single.configure(highlightbackground="black")
        self.match_range_entry0_single.configure(highlightcolor="black")
        self.match_range_entry0_single.configure(insertbackground="black")
        self.match_range_entry0_single.configure(selectbackground="blue")
        self.match_range_entry0_single.configure(selectforeground="white")
        self.match_range_entry0_single.configure(justify=tk.CENTER)
        
        # self.match_range_spin0_single.configure(textvariable=ui_single_support.spinbox)
        # self.match_range_spin0_single.insert('1')
        # print()

        self.match_range1_single = tk.Label(self.calculate_average_labelframe_single)
        self.match_range1_single.place(relx=0.223, rely=0.219, height=23, width=17, bordermode='ignore')
        self.match_range1_single.configure(activebackground="#f9f9f9")
        self.match_range1_single.configure(activeforeground="black")
        self.match_range1_single.configure(background="#d9d9d9")
        self.match_range1_single.configure(disabledforeground="#a3a3a3")
        self.match_range1_single.configure(font="-family {Arial} -size 10")
        self.match_range1_single.configure(foreground="#000000")
        self.match_range1_single.configure(highlightbackground="#d9d9d9")
        self.match_range1_single.configure(highlightcolor="black")
        self.match_range1_single.configure(text='to')

        self.match_range_entry1_single_value = tk.IntVar(value=self.best_match_to_calc)
        self.match_range_entry1_single = tk.Entry(self.calculate_average_labelframe_single, exportselection=0, textvariable=self.match_range_entry1_single_value)
        self.match_range_entry1_single.place(relx=0.297, rely=0.219, relheight=0.2, relwidth=0.103, bordermode='ignore')
        # self.match_range_entry1_single.configure(activebackground="#f9f9f9")
        self.match_range_entry1_single.configure(background="white")
        # self.match_range_entry1_single.configure(buttonbackground="#d9d9d9")
        self.match_range_entry1_single.configure(disabledforeground="#a3a3a3")
        self.match_range_entry1_single.configure(font="TkDefaultFont")
        self.match_range_entry1_single.configure(foreground="black")
        self.match_range_entry1_single.configure(highlightbackground="black")
        self.match_range_entry1_single.configure(highlightcolor="black")
        self.match_range_entry1_single.configure(insertbackground="black")
        self.match_range_entry1_single.configure(selectbackground="blue")
        self.match_range_entry1_single.configure(selectforeground="white")
        self.match_range_entry1_single.configure(justify=tk.CENTER)
        # self.match_range_spin1_single.configure(textvariable=ui_single_support.spinbox)
        # print(int(self.match_range_spin1_single.get()))
        # self.match_range_spin0_single.configure(from_=1,to=int(self.match_range_spin1_single.get())-1)
        # self.match_range_spin1_single.configure(from_=int(self.match_range_spin0_single.get())+1, to=self.best_match_to_calc)
        
        self.short_label_single = tk.Label(self.calculate_average_labelframe_single)
        self.short_label_single.place(relx=0.466, rely=0.19, height=23, width=37, bordermode='ignore')
        self.short_label_single.configure(activebackground="#f9f9f9")
        self.short_label_single.configure(activeforeground="black")
        self.short_label_single.configure(background="#d9d9d9")
        self.short_label_single.configure(disabledforeground="#a3a3a3")
        self.short_label_single.configure(font="-family {Arial} -size 10")
        self.short_label_single.configure(foreground="#000000")
        self.short_label_single.configure(highlightbackground="#d9d9d9")
        self.short_label_single.configure(highlightcolor="black")
        self.short_label_single.configure(text='''S =''')

        self.intermediate_label_single = tk.Label(self.calculate_average_labelframe_single)
        self.intermediate_label_single.place(relx=0.466, rely=0.429, height=23, width=37, bordermode='ignore')
        self.intermediate_label_single.configure(activebackground="#f9f9f9")
        self.intermediate_label_single.configure(activeforeground="black")
        self.intermediate_label_single.configure(background="#d9d9d9")
        self.intermediate_label_single.configure(disabledforeground="#a3a3a3")
        self.intermediate_label_single.configure(font="-family {Arial} -size 10")
        self.intermediate_label_single.configure(foreground="#000000")
        self.intermediate_label_single.configure(highlightbackground="#d9d9d9")
        self.intermediate_label_single.configure(highlightcolor="black")
        self.intermediate_label_single.configure(text='''I =''')

        self.long_label_single = tk.Label(self.calculate_average_labelframe_single)
        self.long_label_single.place(relx=0.466, rely=0.667, height=23, width=37, bordermode='ignore')
        self.long_label_single.configure(activebackground="#f9f9f9")
        self.long_label_single.configure(activeforeground="black")
        self.long_label_single.configure(background="#d9d9d9")
        self.long_label_single.configure(disabledforeground="#a3a3a3")
        self.long_label_single.configure(font="-family {Arial} -size 10")
        self.long_label_single.configure(foreground="#000000")
        self.long_label_single.configure(highlightbackground="#d9d9d9")
        self.long_label_single.configure(highlightcolor="black")
        self.long_label_single.configure(text='''L =''')

        self.S_result_single = tk.Label(self.calculate_average_labelframe_single)
        self.S_result_single.place(relx=0.569, rely=0.19, height=23, width=115, bordermode='ignore') #,justify=tk.CENTER)
        self.S_result_single.configure(activebackground="#f9f9f9")
        self.S_result_single.configure(activeforeground="black")
        self.S_result_single.configure(background="#d9d9d9")
        self.S_result_single.configure(disabledforeground="#a3a3a3")
        self.S_result_single.configure(font="-family {Arial} -size 10")
        self.S_result_single.configure(foreground="#000000")
        self.S_result_single.configure(highlightbackground="#d9d9d9")
        self.S_result_single.configure(highlightcolor="black")
        # self.S_result_single.configure(text='''Label''')

        self.I_result_single = tk.Label(self.calculate_average_labelframe_single)
        self.I_result_single.place(relx=0.569, rely=0.429, height=23, width=115, bordermode='ignore') #,justify=tk.CENTER)
        self.I_result_single.configure(activebackground="#f9f9f9")
        self.I_result_single.configure(activeforeground="black")
        self.I_result_single.configure(background="#d9d9d9")
        self.I_result_single.configure(disabledforeground="#a3a3a3")
        self.I_result_single.configure(font="-family {Arial} -size 10")
        self.I_result_single.configure(foreground="#000000")
        self.I_result_single.configure(highlightbackground="#d9d9d9")
        self.I_result_single.configure(highlightcolor="black")
        # self.I_result_single.configure(text='''Label''')

        self.L_result_single = tk.Label(self.calculate_average_labelframe_single)
        self.L_result_single.place(relx=0.569, rely=0.667, height=23, width=115, bordermode='ignore') #,justify=tk.CENTER)
        self.L_result_single.configure(activebackground="#f9f9f9")
        self.L_result_single.configure(activeforeground="black")
        self.L_result_single.configure(background="#d9d9d9")
        self.L_result_single.configure(disabledforeground="#a3a3a3")
        self.L_result_single.configure(font="-family {Arial} -size 10")
        self.L_result_single.configure(foreground="#000000")
        self.L_result_single.configure(highlightbackground="#d9d9d9")
        self.L_result_single.configure(highlightcolor="black")
        # self.L_result_single.configure(text='''Label''')

        self.restart_button_single = tk.Button(self.operation_single,command=self.restart_single)
        self.restart_button_single.place(relx=0.672, rely=0.602, height=30, width=54)
        self.restart_button_single.configure(activebackground="#ececec")
        self.restart_button_single.configure(activeforeground="#000000")
        self.restart_button_single.configure(background="#d9d9d9")
        self.restart_button_single.configure(disabledforeground="#a3a3a3")
        self.restart_button_single.configure(font="-family {Arial} -size 10")
        self.restart_button_single.configure(foreground="#6a4d20")
        self.restart_button_single.configure(highlightbackground="#d9d9d9")
        self.restart_button_single.configure(highlightcolor="black")
        self.restart_button_single.configure(pady="0")
        self.restart_button_single.configure(text='Restart')
        # self.restart_button_single.configure(state='disable')
        
        # self.deactivate_operation_single()
        
        # // add test
        # self.operation_single.place_forget()
        
        
        
        # =================================
        self.operation_multi = tk.Frame(top)
        self.operation_multi.place(relx=0.505, rely=0.111, relheight=0.881, relwidth=0.49)
        self.operation_multi.configure(relief='groove')
        self.operation_multi.configure(borderwidth="2")
        self.operation_multi.configure(relief="groove")
        self.operation_multi.configure(background="#d9d9d9")
        self.operation_multi.configure(highlightbackground="#d9d9d9")
        self.operation_multi.configure(highlightcolor="black")

        self.load_file_button_multi = tk.Button(self.operation_multi,command=self.load_data_file_multi)
        self.load_file_button_multi.place(relx=0.031, rely=0.025, height=30, width=99)
        self.load_file_button_multi.configure(activebackground="#ececec")
        self.load_file_button_multi.configure(activeforeground="#000000")
        self.load_file_button_multi.configure(background="#d9d9d9")
        # self.load_file_button_multi.configure(command=lambda :ui_multi_support.print('Hello world'))
        self.load_file_button_multi.configure(disabledforeground="#a3a3a3")
        self.load_file_button_multi.configure(font="-family {Arial} -size 10")
        self.load_file_button_multi.configure(foreground="#000000")
        self.load_file_button_multi.configure(highlightbackground="#d9d9d9")
        self.load_file_button_multi.configure(highlightcolor="black")
        self.load_file_button_multi.configure(pady="0")
        self.load_file_button_multi.configure(text='Load data file')

        self.shape_num_label_multi = tk.Label(self.operation_multi)
        self.shape_num_label_multi.place(relx=0.438, rely=0.02, height=30, width=110)
        self.shape_num_label_multi.configure(activebackground="#f9f9f9")
        self.shape_num_label_multi.configure(activeforeground="black")
        self.shape_num_label_multi.configure(background="#d9d9d9")
        self.shape_num_label_multi.configure(disabledforeground="#a3a3a3")
        self.shape_num_label_multi.configure(font="-family {Arial} -size 10")
        self.shape_num_label_multi.configure(foreground="#000000")
        self.shape_num_label_multi.configure(highlightbackground="#d9d9d9")
        self.shape_num_label_multi.configure(highlightcolor="black")
        self.shape_num_label_multi.configure(text='Number of shapes')

        self.shape_num_spin_multi_value = tk.IntVar(value=2)
        self.shape_num_spin_multi = tk.Spinbox(self.operation_multi, from_=2.0, to=20.0, textvariable=self.shape_num_spin_multi_value, justify=tk.CENTER)
        self.shape_num_spin_multi.place(relx=0.797, rely=0.03, relheight=0.059, relwidth=0.094) # rely = 0.028
        self.shape_num_spin_multi.configure(activebackground="#f9f9f9")
        self.shape_num_spin_multi.configure(background="white")
        self.shape_num_spin_multi.configure(buttonbackground="#d9d9d9")
        self.shape_num_spin_multi.configure(disabledforeground="#a3a3a3")
        self.shape_num_spin_multi.configure(font="-family {Arial} -size 10")
        self.shape_num_spin_multi.configure(foreground="black")
        self.shape_num_spin_multi.configure(highlightbackground="black")
        self.shape_num_spin_multi.configure(highlightcolor="black")
        self.shape_num_spin_multi.configure(insertbackground="black")
        self.shape_num_spin_multi.configure(selectbackground="blue")
        self.shape_num_spin_multi.configure(selectforeground="white")

        self.method_labelframe_multi = tk.LabelFrame(self.operation_multi)
        self.method_labelframe_multi.place(relx=0.031, rely=0.109, relheight=0.185, relwidth=0.563)
        self.method_labelframe_multi.configure(relief='groove')
        self.method_labelframe_multi.configure(font="-family {Arial} -size 10")
        self.method_labelframe_multi.configure(foreground="black")
        self.method_labelframe_multi.configure(text='''Method''')
        self.method_labelframe_multi.configure(background="#d9d9d9")
        self.method_labelframe_multi.configure(highlightbackground="#d9d9d9")
        self.method_labelframe_multi.configure(highlightcolor="black")

        self.method_multi_value = tk.StringVar(value='histogram')
        self.histogram_select_button_multi = tk.Radiobutton(self.method_labelframe_multi, text='Histogram', value='histogram', variable=self.method_multi_value,command=self.change_method_state_multi)
        self.histogram_select_button_multi.place(relx=0.017, rely=0.227, relheight=0.364, relwidth=0.494, bordermode='ignore')
        self.histogram_select_button_multi.configure(activebackground="#ececec")
        self.histogram_select_button_multi.configure(activeforeground="#000000")
        self.histogram_select_button_multi.configure(background="#d9d9d9")
        self.histogram_select_button_multi.configure(disabledforeground="#a3a3a3")
        self.histogram_select_button_multi.configure(font="-family {Arial} -size 10")
        self.histogram_select_button_multi.configure(foreground="#000000")
        self.histogram_select_button_multi.configure(highlightbackground="#d9d9d9")
        self.histogram_select_button_multi.configure(highlightcolor="black")
        self.histogram_select_button_multi.configure(justify='left')

        self.kde_select_button_multi = tk.Radiobutton(self.method_labelframe_multi, text='Kernel density estimation', value='gaussian_kde', variable=self.method_multi_value,command=self.change_method_state_multi)
        self.kde_select_button_multi.place(relx=0.028, rely=0.545, relheight=0.348, relwidth=0.95, bordermode='ignore')
        self.kde_select_button_multi.configure(activebackground="#ececec")
        self.kde_select_button_multi.configure(activeforeground="#000000")
        self.kde_select_button_multi.configure(background="#d9d9d9")
        self.kde_select_button_multi.configure(disabledforeground="#a3a3a3")
        self.kde_select_button_multi.configure(font="-family {Arial} -size 10")
        self.kde_select_button_multi.configure(foreground="#000000")
        self.kde_select_button_multi.configure(highlightbackground="#d9d9d9")
        self.kde_select_button_multi.configure(highlightcolor="black")
        self.kde_select_button_multi.configure(justify='left')

        self.repeat_times_labelframe_multi = tk.LabelFrame(self.operation_multi)
        # self.repeat_times_labelframe_multi.place(relx=0.609, rely=0.109, relheight=0.185, relwidth=0.375)
        self.repeat_times_labelframe_multi.configure(relief='groove')
        self.repeat_times_labelframe_multi.configure(font="-family {Arial} -size 10")
        self.repeat_times_labelframe_multi.configure(foreground="black")
        self.repeat_times_labelframe_multi.configure(text='Repeat times')
        self.repeat_times_labelframe_multi.configure(background="#d9d9d9")
        self.repeat_times_labelframe_multi.configure(highlightbackground="#d9d9d9")
        self.repeat_times_labelframe_multi.configure(highlightcolor="black")

        self.repeat_times_multi_value = tk.StringVar(value='0')
        self.repeat_times_combobox_multi = ttk.Combobox(self.repeat_times_labelframe_multi, textvariable=self.repeat_times_multi_value, values=[0,20,50,100,200,300,500], state='readonly')
        # self.repeat_times_combobox_multi.place(relx=0.267, rely=0.379, relheight=0.394, relwidth=0.467, bordermode='ignore')
        self.repeat_times_combobox_multi.configure(background="white")
        # self.repeat_times_combobox_multi.configure(disabledforeground="#a3a3a3")
        self.repeat_times_combobox_multi.configure(font="-family {Arial} -size 10")

        self.bin_num_label_multi = tk.Label(self.operation_multi)
        # self.bin_num_label_multi.place(relx=0.088, rely=0.308, height=25, width=232)
        self.bin_num_label_multi.configure(activebackground="#f9f9f9")
        self.bin_num_label_multi.configure(activeforeground="black")
        self.bin_num_label_multi.configure(background="#d9d9d9")
        self.bin_num_label_multi.configure(disabledforeground="#a3a3a3")
        self.bin_num_label_multi.configure(font="-family {Arial} -size 10")
        self.bin_num_label_multi.configure(foreground="#000000")
        self.bin_num_label_multi.configure(highlightbackground="#d9d9d9")
        self.bin_num_label_multi.configure(highlightcolor="black")
        self.bin_num_label_multi.configure(text='Number of bins for histogram method:')

        self.bin_num_multi_value = tk.IntVar(value=30)
        self.bin_num_spin_multi = tk.Spinbox(self.operation_multi, from_=1.0, to=50,textvariable=self.bin_num_multi_value,justify=tk.CENTER)
        # self.bin_num_spin_multi.place(relx=0.828, rely=0.308, relheight=0.059, relwidth=0.125)
        self.bin_num_spin_multi.configure(activebackground="#f9f9f9")
        self.bin_num_spin_multi.configure(background="white")
        self.bin_num_spin_multi.configure(buttonbackground="#d9d9d9")
        self.bin_num_spin_multi.configure(disabledforeground="#a3a3a3")
        self.bin_num_spin_multi.configure(font="-family {Arial} -size 10")
        self.bin_num_spin_multi.configure(foreground="black")
        self.bin_num_spin_multi.configure(highlightbackground="black")
        self.bin_num_spin_multi.configure(highlightcolor="black")
        self.bin_num_spin_multi.configure(insertbackground="black")
        self.bin_num_spin_multi.configure(selectbackground="blue")
        self.bin_num_spin_multi.configure(selectforeground="white")
        self.bin_num_spin_multi.configure(state='disable')

        self.step_size_label_multi = tk.Label(self.operation_multi)
        self.step_size_label_multi.place_forget()
        self.step_size_label_multi.configure(background="#d9d9d9")
        self.step_size_label_multi.configure(disabledforeground="#a3a3a3")
        self.step_size_label_multi.configure(font="-family {Arial} -size 10")
        self.step_size_label_multi.configure(foreground="#000000")
        self.step_size_label_multi.configure(text='Step size on proportions:')
        self.step_size_spin_multi_value = tk.DoubleVar(value=0.1)
        self.step_size_spin_multi = tk.Spinbox(self.operation_multi, from_=0.01, to=0.5, increment=0.05, textvariable=self.step_size_spin_multi_value,justify=tk.CENTER)
        self.step_size_spin_multi.place_forget()
        
        self.best_match_spin_multi_value = tk.IntVar(value=5)
        self.best_match_to_calc = int(self.best_match_spin_multi_value.get())
        self.best_match_spin_multi = tk.Spinbox(self.operation_multi, from_=1, to=30, textvariable=self.best_match_spin_multi_value, justify=tk.CENTER)
        self.best_match_spin_multi.place(relx=0.208, rely=0.658-0.05, relheight=0.059, relwidth=0.109)
        self.best_match_spin_multi.configure(activebackground="#f9f9f9")
        self.best_match_spin_multi.configure(background="white")
        self.best_match_spin_multi.configure(buttonbackground="#d9d9d9")
        self.best_match_spin_multi.configure(disabledforeground="#a3a3a3")
        self.best_match_spin_multi.configure(font="-family {Arial} -size 10")
        self.best_match_spin_multi.configure(foreground="black")
        self.best_match_spin_multi.configure(highlightbackground="black")
        self.best_match_spin_multi.configure(highlightcolor="black")
        self.best_match_spin_multi.configure(insertbackground="black")
        self.best_match_spin_multi.configure(selectbackground="blue")
        self.best_match_spin_multi.configure(selectforeground="white")
        
        self.best_match_label0_multi = tk.Label(self.operation_multi)
        self.best_match_label0_multi.place(relx=0.047, rely=0.658-0.05, height=23, width=47)
        self.best_match_label0_multi.configure(activebackground="#f9f9f9")
        self.best_match_label0_multi.configure(activeforeground="black")
        self.best_match_label0_multi.configure(background="#d9d9d9")
        self.best_match_label0_multi.configure(disabledforeground="#a3a3a3")
        self.best_match_label0_multi.configure(font="-family {Arial} -size 10")
        self.best_match_label0_multi.configure(foreground="#000000")
        self.best_match_label0_multi.configure(highlightbackground="#d9d9d9")
        self.best_match_label0_multi.configure(highlightcolor="black")
        self.best_match_label0_multi.configure(text='Get the')

        self.best_match_label1_multi = tk.Label(self.operation_multi)
        self.best_match_label1_multi.place(relx=0.315, rely=0.658-0.05, height=23, width=207)
        self.best_match_label1_multi.configure(activebackground="#f9f9f9")
        self.best_match_label1_multi.configure(activeforeground="black")
        self.best_match_label1_multi.configure(background="#d9d9d9")
        self.best_match_label1_multi.configure(disabledforeground="#a3a3a3")
        self.best_match_label1_multi.configure(font="-family {Arial} -size 10")
        self.best_match_label1_multi.configure(foreground="#000000")
        self.best_match_label1_multi.configure(highlightbackground="#d9d9d9")
        self.best_match_label1_multi.configure(highlightcolor="black")
        self.best_match_label1_multi.configure(text='best-match results by RMSE')

        self.get_params_button_multi = tk.Button(self.operation_multi, command=self.get_parameters_multi)
        self.get_params_button_multi.place(relx=0.047, rely=0.756-0.025, height=30, width=120)
        self.get_params_button_multi.configure(activebackground="#ececec")
        self.get_params_button_multi.configure(activeforeground="#000000")
        self.get_params_button_multi.configure(background="#d9d9d9")
        self.get_params_button_multi.configure(disabledforeground="#a3a3a3")
        self.get_params_button_multi.configure(font="-family {Arial} -size 10")
        self.get_params_button_multi.configure(foreground="#0000ff")
        self.get_params_button_multi.configure(highlightbackground="#d9d9d9")
        self.get_params_button_multi.configure(highlightcolor="black")
        self.get_params_button_multi.configure(pady="0")
        self.get_params_button_multi.configure(text='Get parameters')

        self.run_button_multi = tk.Button(self.operation_multi, command=self.run_multi)
        self.run_button_multi.place(relx=0.594, rely=0.756-0.025, height=30, width=120)
        self.run_button_multi.configure(activebackground="#ececec")
        self.run_button_multi.configure(activeforeground="#000000")
        self.run_button_multi.configure(background="#d9d9d9")
        self.run_button_multi.configure(disabledforeground="#a3a3a3")
        self.run_button_multi.configure(font="-family {Arial} -size 10")
        self.run_button_multi.configure(foreground="#008000")
        self.run_button_multi.configure(highlightbackground="#d9d9d9")
        self.run_button_multi.configure(highlightcolor="black")
        self.run_button_multi.configure(pady="0")
        self.run_button_multi.configure(text='Run')

        self.view_results_button_multi = tk.Button(self.operation_multi,command=self.open_view_result_multi)
        self.view_results_button_multi.place(relx=0.047, rely=0.868-0.025, height=30, width=120)
        self.view_results_button_multi.configure(activebackground="#ececec")
        self.view_results_button_multi.configure(activeforeground="#000000")
        self.view_results_button_multi.configure(background="#d9d9d9")
        self.view_results_button_multi.configure(disabledforeground="#a3a3a3")
        self.view_results_button_multi.configure(font="-family {Arial} -size 10")
        self.view_results_button_multi.configure(foreground="#000000")
        self.view_results_button_multi.configure(highlightbackground="#d9d9d9")
        self.view_results_button_multi.configure(highlightcolor="black")
        self.view_results_button_multi.configure(pady="0")
        self.view_results_button_multi.configure(text='View results')

        self.restart_button_multi = tk.Button(self.operation_multi, command=self.restart_multi)
        self.restart_button_multi.place(relx=0.688, rely=0.868-0.025, height=30, width=54)
        self.restart_button_multi.configure(activebackground="#ececec")
        self.restart_button_multi.configure(activeforeground="#000000")
        self.restart_button_multi.configure(background="#d9d9d9")
        self.restart_button_multi.configure(disabledforeground="#a3a3a3")
        self.restart_button_multi.configure(font="-family {Arial} -size 10")
        self.restart_button_multi.configure(foreground="#6a4d20")
        self.restart_button_multi.configure(highlightbackground="#d9d9d9")
        self.restart_button_multi.configure(highlightcolor="black")
        self.restart_button_multi.configure(pady="0")
        self.restart_button_multi.configure(text='Restart')
        # self.restart_button_multi.configure(state='disable')

        self.multiple_processing_check_multi_value = tk.IntVar(value=0)
        self.multiple_processing_check_multi = tk.Checkbutton(self.operation_multi, variable=self.multiple_processing_check_multi_value, command=self.multiple_processing_check_func_multi)
        self.multiple_processing_check_multi.place(relx=0.02, rely=0.468-0.1, relheight=0.076, relwidth=0.75)
        self.multiple_processing_check_multi.configure(activebackground="#ececec")
        self.multiple_processing_check_multi.configure(activeforeground="#000000")
        self.multiple_processing_check_multi.configure(background="#d9d9d9")
        self.multiple_processing_check_multi.configure(disabledforeground="#a3a3a3")
        self.multiple_processing_check_multi.configure(font="-family {Arial} -size 10")
        self.multiple_processing_check_multi.configure(foreground="#000000")
        self.multiple_processing_check_multi.configure(highlightbackground="#d9d9d9")
        self.multiple_processing_check_multi.configure(highlightcolor="black")
        self.multiple_processing_check_multi.configure(justify='left')
        self.multiple_processing_check_multi.configure(text='Multiple processors for calcluation')
        # self.multiple_processing_check_multi.deselect()
                    
        self.multiple_processing_spin_multi_value = tk.IntVar(value=0)
        self.multiple_processing_spin_multi = tk.Spinbox(self.operation_multi, from_=0, to=64, textvariable=self.multiple_processing_spin_multi_value, justify=tk.CENTER)
        self.multiple_processing_spin_multi.place(relx=0.828, rely=0.476-0.1, relheight=0.059, relwidth=0.125)
        self.multiple_processing_spin_multi.configure(activebackground="#f9f9f9")
        self.multiple_processing_spin_multi.configure(background="white")
        self.multiple_processing_spin_multi.configure(buttonbackground="#d9d9d9")
        self.multiple_processing_spin_multi.configure(disabledforeground="#a3a3a3")
        self.multiple_processing_spin_multi.configure(font="-family {Arial} -size 10")
        self.multiple_processing_spin_multi.configure(foreground="black")
        self.multiple_processing_spin_multi.configure(highlightbackground="black")
        self.multiple_processing_spin_multi.configure(highlightcolor="black")
        self.multiple_processing_spin_multi.configure(insertbackground="black")
        self.multiple_processing_spin_multi.configure(selectbackground="blue")
        self.multiple_processing_spin_multi.configure(selectforeground="white")
        self.multiple_processing_spin_multi.configure(state='disable')
        
        self.data_chunks_multi = tk.Label(self.operation_multi)
        self.data_chunks_multi.place(relx=0.085, rely=0.549-0.075, relheight=0.076, relwidth=0.75)
        self.data_chunks_multi.configure(text='Split the data into chunks of size 1E6.')
        self.data_chunks_multi.configure(justify=tk.LEFT)

        self.data_chunks_multi.configure(font="-family {Arial} -size 10")
        self.data_chunks_multi.configure(foreground="#a3a3a3")
        self.data_chunks_multi.configure(background="#d9d9d9")
        
        
        
        
        self.data_chunks_check_multi_value = tk.IntVar(value=0)
        self.data_chunks_check_multi = tk.Checkbutton(self.operation_multi,variable=self.data_chunks_check_multi_value, command='')
        self.data_chunks_check_multi.place_forget()
        self.data_chunks_check_multi.configure(justify=tk.LEFT)
        

        self.data_chunks_combobox_multi_value = tk.IntVar(value=0)
        self.data_chunks_combobox_multi = ttk.Combobox(self.operation_multi, textvariable=self.data_chunks_combobox_multi_value, values=[0,200,500,1000,2000,3000,5000,7000,9000],justify=tk.CENTER)
        self.data_chunks_combobox_multi.place_forget()
        self.data_chunks_combobox_multi.configure(background="white")
        self.data_chunks_combobox_multi.configure(font="-family {Arial} -size 10")
        self.data_chunks_combobox_multi.configure(state='disable')
        
        self.deactivate_operation_single()
        self.deactivate_operation_multi()
        
        
        # // add test
        self.operation_multi.place_forget()


    def about(self):
        tk.messagebox.showinfo('About', 'Written by Jie Li <lj201112@163.com>\n in python with numpy, scipy, pandas, matplotlib and tkinter.')


    def load_operation_single(self):
        self.restart_single()
        self.restart_multi()
        self.deactivate_operation_single()
        self.deactivate_operation_multi()
        self.operation_multi.place_forget()
        self.operation_single.place(relx=0.505, rely=0.111, relheight=0.881, relwidth=0.49)
        
        self.notes_text.configure(state='normal')
        self.notes_text.see(tk.END)             
        self.notes_text.insert(tk.END,'Single shape estimation activated')
        self.notes_text.insert(tk.END,'\n'+'---------------------------\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')  
        
        
    # def show_widgets_after_loading_file(self):

    def load_opration_multi(self):
        self.restart_single()
        self.restart_multi()
        self.deactivate_operation_single()
        self.deactivate_operation_multi()
        self.operation_single.place_forget()
        self.operation_multi.place(relx=0.505, rely=0.111, relheight=0.881, relwidth=0.49)
        
        self.notes_text.configure(state='normal')
        self.notes_text.see(tk.END)             
        self.notes_text.insert(tk.END,'Multiple shapes estimation activated')
        self.notes_text.insert(tk.END,'\n'+'---------------------------\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')  
        
    def activate_operation_single(self): # set widgets states
        self.histogram_select_button_single.configure(state='normal')
        self.kde_select_button_single.configure(state='normal')
        # self.repeat_times_combobox_single.configure(state='normal')
        # self.bin_num_spin_single.configure(state='normal')
        self.best_match_spin_single.configure(state='normal')
        self.get_params_button_single.configure(state='normal')
        self.run_button_single.configure(state='disable')
        self.view_results_button_single.configure(state='disable')
        self.restart_button_single.configure(state='normal')
        self.average_calc_button_single.configure(state='disable')
        self.match_range_entry0_single.configure(state='disable')
        self.match_range_entry1_single.configure(state='disable')
        self.S_result_single.configure(text='')
        self.I_result_single.configure(text='')
        self.L_result_single.configure(text='')
        self.calculate_average_labelframe_single.place(relx=0.063, rely=0.686, relheight=0.294, relwidth=0.906)
        
    def deactivate_operation_single(self):
        self.histogram_select_button_single.configure(state='disable')
        self.kde_select_button_single.configure(state='disable')
        self.repeat_times_combobox_single.configure(state='disable')
        # self.bin_num_spin_single.configure(state='disable')
        self.best_match_spin_single.configure(state='disable')
        self.get_params_button_single.configure(state='disable')
        self.run_button_single.configure(state='disable')
        self.view_results_button_single.configure(state='disable')
        self.restart_button_single.configure(state='disable')
        self.average_calc_button_single.configure(state='disable')
        self.match_range_entry0_single.configure(state='disable')
        self.match_range_entry1_single.configure(state='disable')
        self.calculate_average_labelframe_single.place_forget()
        
    def activate_operation_multi(self):
        self.shape_num_spin_multi.configure(state='normal')
        self.histogram_select_button_multi.configure(state='normal')
        self.kde_select_button_multi.configure(state='normal')
        # self.repeat_times_combobox_multi.configure(state='normal')
        # self.bin_num_spin_multi.configure(state='normal')
        #self.step_size_spin_multi.configure(state='normal')
        self.best_match_spin_multi.configure(state='normal')
        self.multiple_processing_check_multi.configure(state='normal')
        # self.multiple_processing_spin_multi.configure(state='normal')
        #self.data_chunks_check_multi.configure(state='normal')
        # self.data_chunks_combobox_multi.configure(state='normal')
        self.get_params_button_multi.configure(state='normal')
        self.run_button_multi.configure(state='disable')
        self.view_results_button_multi.configure(state='disable')
        self.restart_button_multi.configure(state='normal')
    
    def deactivate_operation_multi(self):
        self.shape_num_spin_multi.configure(state='disable')
        self.histogram_select_button_multi.configure(state='disable')
        self.kde_select_button_multi.configure(state='disable')
        self.repeat_times_combobox_multi.configure(state='disable')
        # self.bin_num_spin_multi.configure(state='disable')
        self.step_size_spin_multi.configure(state='disable')
        self.best_match_spin_multi.configure(state='disable')
        self.multiple_processing_check_multi.configure(state='disable')
        self.multiple_processing_spin_multi.configure(state='disable')
        self.data_chunks_check_multi.configure(state='disable')
        self.data_chunks_combobox_multi.configure(state='disable')
        self.get_params_button_multi.configure(state='disable')
        self.run_button_multi.configure(state='disable')
        self.view_results_button_multi.configure(state='disable')
        self.restart_button_multi.configure(state='disable')
        self.data_chunks_multi.configure(foreground="#a3a3a3")
        
    def get_parameters_single(self):
        self.notes_text.configure(state='normal')
        
        self.data_to_calc = self.data_in_log
        self.method_to_calc = self.method_single_value.get()
        self.repeat_times_to_calc = int(self.repeat_times_combobox_single.get())
        
        try:
            self.hist_bin_num_to_calc = int(self.bin_num_spin_single.get())
        except:
            self.notes_text.insert(tk.END,'\n'+'Invalid bin number!')
            self.hist_bin_num_to_calc = 30
            
        try:
            self.best_match_to_calc = int(self.best_match_spin_single.get())
        except:
             self.notes_text.insert(tk.END,'\n'+'Invalid best-match data!')
             self.best_match_to_calc = 5
             
        try:
            self.view_result_TopLevel.destroy() ##### destroy view results window
        except:
            pass
             
        self.notes_text.see(tk.END)             
        self.notes_text.insert(tk.END,'\n\n'+'-----Parameters-----')
        self.notes_text.insert(tk.END,'\n'+'Method --> {0}'.format(self.method_to_calc))
        # self.notes_text.insert(tk.END,'\n'+'Repeat times --> {0}'.format(self.repeat_times_to_calc))
        if self.method_single_value.get() == 'histogram':
            self.notes_text.insert(tk.END,'\n'+'Bin numbers of the histogram --> {0}'.format(self.hist_bin_num_to_calc))
        self.notes_text.insert(tk.END,'\n'+'Top [{0}] best-match results will be selected'.format(self.best_match_to_calc))
        self.notes_text.insert(tk.END,'\n'+'---------------------------\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')  
        
        self.match_range_entry0_single.configure(state='disable')
        self.match_range_entry1_single.configure(state='disable')
        
        self.match_range_entry1_single.configure(state='normal')
        self.match_range_entry1_single.delete(0,last=len(self.match_range_entry1_single.get()))
        self.match_range_entry1_single.insert(0,self.best_match_to_calc)
        self.match_range_entry1_single.configure(state='disable')
        self.run_button_single.configure(state='normal')
        
    def restart_single(self): # empty the variables
        self.data_to_calc = None
        self.method_to_calc = ''
        self.repeat_times_to_calc = None
        self.hist_bin_num_to_calc = None
        self.best_match_to_calc = None
        self.result_single = None
        self.fig_single = []
        self.S_result_single.configure(text='')
        self.I_result_single.configure(text='')
        self.L_result_single.configure(text='')
        self.match_range_entry0_single_value.set(1)
        self.match_range_entry1_single_value.set(5)
        self.repeat_times_combobox_single.set('0')
        self.histogram_select_button_single.select()
        self.bin_num_single_value.set(30)
        self.best_match_spin_single_value.set(5)
        # self.bin_num_spin_single.place(relx=0.766, rely=0.308, relheight=0.07, relwidth=0.156)
        # self.bin_num_label_single.place(relx=0.031, rely=0.308, height=25, width=232)
        self.notes_text.configure(state='normal')
        self.notes_text.delete(1.0,tk.END)
        # self.notes_text.insert(tk.END,'++++++ Restart ++++++\n')
        self.notes_text.configure(state='disable')
        self.deactivate_operation_single()
        
        try:
            self.view_result_TopLevel.destroy() #####
        except:
            pass            

    def load_data_file_single(self): # 加载数据
        from Modules.data_process import data_process
        self.restart_single()
        self.restart_multi()
        
        self.notes_text.configure(state='normal')
        d = data_process()   
        open_fdialog_message,fpath = d.open_fdialog()
        self.notes_text.insert(tk.END,'\n'+open_fdialog_message)
        processing_data_message,self.data_in_log = d.processing_data()
        self.notes_text.insert(tk.END,'\n'+processing_data_message+'\n')
        # # self.notes_text.update()
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')
        if fpath:       
            self.activate_operation_single()
        else:
            self.deactivate_operation_single()
        
    def change_method_state_single(self):
        # self.method_state = self.method_single_value.get()
        if self.method_single_value.get() == 'gaussian_kde':
            self.bin_num_spin_single.place_forget()
            self.bin_num_label_single.place_forget()
        elif self.method_single_value.get() == 'histogram':
            pass
            # self.bin_num_spin_single.place(relx=0.766, rely=0.308, relheight=0.07, relwidth=0.156)
            # self.bin_num_label_single.place(relx=0.031, rely=0.308, height=25, width=232)
   
    def run_single(self):
        from Modules.shape_fit import ShapeFit
        self.notes_text.configure(state='normal')
        self.notes_text.insert(tk.END,'\n'+'**********************\n'+'Calculation in progress...')
        calc_message,self.result_single = ShapeFit(self.data_to_calc,1,method=self.method_to_calc,top_R=self.best_match_to_calc).main()

        self.notes_text.insert(tk.END,'\n'+calc_message)
        self.notes_text.insert(tk.END,'**********************')
        # # self.notes_text.update()
        
        self.notes_text.insert(tk.END,'\n+++++ Results +++++\n')
        for i in range(len(self.result_single)):
            self.notes_text.insert(tk.END,'{0}. R = {1:.4f},    '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = ')+'\n')           
        self.notes_text.insert(tk.END,'+++++++++++++++++\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')
        self.average_calc_button_single.configure(state='normal')
        self.match_range_entry0_single.configure(state='normal')
        self.match_range_entry1_single.configure(state='normal')
        self.view_results_button_single.configure(state='normal')
        
        self.get_database()

    def average_calc_single(self):
        import numpy as np
        shape_b,shape_c = [],[]

        self.notes_text.configure(state='normal') 
        try:
            r_range_temp = int(self.match_range_entry0_single.get()),int(self.match_range_entry1_single.get())
            if (r_range_temp[1] - r_range_temp[0] > 1) and (r_range_temp[1] <= self.best_match_to_calc) and (r_range_temp[0] >= 1):
                r_range = r_range_temp
            else:
                r_range = (1, self.best_match_to_calc)
                self.notes_text.insert(tk.END,'\n'+'The range should be from {0} to {1}\n'.format(1, self.best_match_to_calc))
        except:
            r_range = (1, self.best_match_to_calc)
            self.notes_text.insert(tk.END,'\n'+'Invalid data range! The range should be from {0} to {1}\n'.format(1, self.best_match_to_calc))
             
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')
        for result in self.result_single[r_range[0]:r_range[1]]:
            shape_b.append(float(eval(result[0].split(',')[1].split('=')[1])))
            shape_c.append(float(eval(result[0].split(',')[2].split('=')[1])))
        shape_b_mean = np.mean(np.array(shape_b))
        shape_c_mean = np.mean(np.array(shape_c))
        shape_b_sigma = np.std(np.array(shape_b),ddof=1)
        shape_c_sigma = np.std(np.array(shape_c),ddof=1)
        self.S_result_single.configure(text='1')
        self.I_result_single.configure(text='{0:.2f} '.format(shape_b_mean)+chr(0x00B1)+' {0:.2f}'.format(shape_b_sigma))
        self.L_result_single.configure(text='{0:.2f} '.format(shape_c_mean)+chr(0x00B1)+' {0:.2f}'.format(shape_c_sigma))

    # draw results single
    def get_database(self):
        import pickle
        import numpy as np
        with open('./Database/Database_LogAR_Hist.pickle','rb') as f:
            self.database_hist = pickle.load(f)
        with open('./Database/Database_LogAR_KDE.pickle','rb') as f:
            self.database_kde = pickle.load(f)
            
        self.index = np.array(list(self.database_hist.keys()))


    def open_view_result_single(self):
        self.view_result_TopLevel = tk.Toplevel(self.top)
        self.view_result_TopLevel.title("View results")
        self.view_result_TopLevel.geometry("580x747+601+130")
        self.view_result_TopLevel.minsize(580, 400)
        self.view_result_TopLevel.maxsize(580,800)
        self.view_result_TopLevel.resizable(1,  1)
        # self.view_result_TopLevel.attributes("-topmost", True)
        # view_result_TopLevel.title("New Toplevel")
        self.view_result_TopLevel.configure(background="#d9d9d9")
        
        # self.view_result_frame = tk.Frame(self.view_result_TopLevel)
        # self.view_result_frame.place(relx=0.017, rely=0.074, relheight=0.459, relwidth=0.933)
        # self.view_result_frame.configure(relief='groove')
        # self.view_result_frame.configure(borderwidth="1")
        # self.view_result_frame.configure(relief="groove")
        # self.view_result_frame.configure(background="#d9d9d9")

        self.view_result_frame = tk.Frame(self.view_result_TopLevel)
        self.view_result_frame.place(relx=0.008, rely=0.011, relheight=0.982, relwidth=0.983)
        self.view_result_frame.configure(relief='groove')
        self.view_result_frame.configure(borderwidth="1")
        self.view_result_frame.configure(relief="groove")
        self.view_result_frame.configure(background="#d9d9d9")

        self.view_result_canvas = tk.Canvas(self.view_result_frame)
        self.view_result_canvas.place(relx=0.008, rely=0.068, relheight=0.93, relwidth=0.985)
        self.view_result_canvas.configure(background="#d9d9d9")
        self.view_result_canvas.configure(insertbackground="black")
        self.view_result_canvas.configure(relief="ridge")
        self.view_result_canvas.configure(selectbackground="blue")
        self.view_result_canvas.configure(selectforeground="white")

        self.view_result_frame_in_canvas = tk.Frame(self.view_result_canvas)
        self.view_result_frame_in_canvas.place(relx=0.008, rely=0.007, relheight=0.989, relwidth=0.986)
        self.view_result_frame_in_canvas.configure(background="#d9d9d9")
        self.view_result_frame_in_canvas.configure(borderwidth="1")
        # self.view_result_frame_in_canvas.configure(insertbackground="black")
        self.view_result_frame_in_canvas.configure(relief="ridge")
        # self.view_result_frame_in_canvas.configure(selectbackground="blue")
        # self.view_result_frame_in_canvas.configure(selectforeground="white")
        
        self.view_result_canvas.create_window((0,0),window=self.view_result_frame_in_canvas,anchor='nw')
        
        self.view_result_scrollbar=tk.Scrollbar(self.view_result_frame,orient="vertical",command=self.view_result_canvas.yview)
        self.view_result_canvas.configure(yscrollcommand=self.view_result_scrollbar.set)
        self.view_result_scrollbar.pack(side="right",fill="y")

        # self.view_result_canvas.bind("<Configure>",self.view_result_canvas_scroll_action)
        # self.view_result_canvas.bind_all("<MouseWheel>",self.view_result_canvas_mouse_scroll)
        # self.view_result_draw_action_single()

        self.view_result_frame_in_canvas.bind("<Configure>",self.view_result_canvas_scroll_action)
        self.view_result_frame_in_canvas.bind_all("<MouseWheel>",self.view_result_canvas_mouse_scroll)
        self.view_result_draw_action_single()
    
        self.view_result_save_button_single = tk.Button(self.view_result_TopLevel,command=self.view_result_save_files_single)
        self.view_result_save_button_single.place(relx=0.7325, rely=0.0225, height=35, width=120)
        self.view_result_save_button_single.configure(activebackground="#ececec")
        self.view_result_save_button_single.configure(activeforeground="#000000")
        self.view_result_save_button_single.configure(background="#d9d9d9")
        self.view_result_save_button_single.configure(disabledforeground="#a3a3a3")
        self.view_result_save_button_single.configure(font="-family {Arial} -size 10")
        self.view_result_save_button_single.configure(foreground="#000000")
        self.view_result_save_button_single.configure(highlightbackground="#d9d9d9")
        self.view_result_save_button_single.configure(highlightcolor="black")
        self.view_result_save_button_single.configure(pady="0")
        self.view_result_save_button_single.configure(text='Save')
        
        self.view_result_TopLevel.protocol("WM_DELETE_WINDOW", self.view_result_TopLevel_close_action)

    def view_result_TopLevel_close_action(self):
        self.view_result_TopLevel.unbind_all("<MouseWheel>")
        self.view_result_TopLevel.destroy()

    def view_result_html_single(self): # save fig in html
        html_str = ''
        html_str += '<!DOCTYPE html>\n'
        html_str += '<html>\n'
        html_str += ' '*4+'<head>\n'
        html_str += ' '*8+'<title>Results</title>\n'
        html_str += ' '*8+'<h3>Results of 3D shape estimation</h3>\n'
        html_str += ' '*4+'</head>\n'
        html_str += ' '*4+'<body>\n'
        # html_str += ' '*4+'<br/>\n'
        for i in range(len(self.result_single)):
            html_str += ' '*8 +'<p>'+ ('-'*75)+'<br/>\n'
            html_str += ' '*12+('RMSE = %.4f, Simulated Shape: %s' % (self.result_single[i][1],self.result_single[i][0]))+'<br/>\n'
            html_str += ' '*12+ self.fig_to_html(self.fig_single[i])
            html_str += ' '*8+'</p>\n'
            html_str += ' '*8+ '<br/>\n'
        html_str += ' '*8+'<p>'+('='*75)+'</p>\n'
        html_str += ' '*4+'</body>\n'
        html_str += '</html>\n'
        return html_str  
        
    def view_result_save_fig_other_formats_single(self,fig_path,imgsize = (4,2.5),label_font_size=12,tick_font_size=10): # save in multiple formats except html and xls
        from scipy.stats import gaussian_kde
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib as mpl
        mpl.rcParams["font.family"] = 'Helvetica'
        mpl.rcParams['svg.fonttype'] = 'none'
        # import numpy as np

        files_list = []
        if self.method_to_calc == 'gaussian_kde':
            for i in range(len(self.result_single)):
                ax = plt.gca()
                x_ = np.linspace(0,3,150)
                y1 = gaussian_kde(self.data_to_calc[np.where(self.data_to_calc < 3)])(x_)
                y2 = self.database_kde[self.result_single[i][0]]
                ax.set_title('{0}. RMSE = {1:.4f}, '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '),fontsize=label_font_size)
                ax.plot(x_,y1,linestyle='--', lw=2.5,color=(256/256,127/256,14/256),label='Unknown',  alpha=1)
                ax.plot(x_,y2,linestyle='-' , lw=2.5,color=(31/256,119/256,181/256),label='Simulated',alpha=1)
                ax.set_xlim(x_.min(),x_.max())
                ax.set_xlabel('ln(AR)',fontsize=label_font_size)
                ax.set_ylabel('Probability density',fontsize=label_font_size)
                ax.spines[   'top'].set_linewidth(1.5)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines[  'left'].set_linewidth(1.5)
                ax.spines[ 'right'].set_linewidth(1.5)
                ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.legend(fontsize=11,loc=1,frameon=False)
                file_name = fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(i+1)+'.'+fig_path.split('.')[-1])
                # file_name = fig_path+'/'+fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(i+1)+'.'+fig_path.split('.')[-1])
                
                plt.savefig(file_name, transparent=True, dpi=300, pad_inches = 0.1, bbox_inches = 'tight')
                plt.clf()
                plt.close('all')
                files_list.append(file_name)
                
        if self.method_to_calc == 'histogram':
            for i in range(len(self.result_single)):
                ax = plt.gca()
                x_ = np.linspace(0,3,self.hist_bin_num_to_calc+1)
                n_src,bins_src,_ = ax.hist(self.data_to_calc, bins = x_, range = (x_.min(),x_.max()), density = True, lw=1.25,hatch='\\\\',   fill=False,edgecolor=(256/256,127/256,14/256), alpha=1)
                n_dst = self.database_hist[self.result_single[i][0]]
                bins_dst = bins_src
                mid_src = (bins_src[0:-1]+bins_src[1:])/2
                mid_dst = (bins_dst[0:-1]+bins_dst[1:])/2
                ax.plot(mid_src,n_src,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(256/256,127/256,14/256),markeredgecolor='k',markeredgewidth=1.25,label='Unknown'  )
                ax.plot(mid_dst,n_dst,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(31/256,119/256,181/256),markeredgecolor='k',markeredgewidth=1.25,label='Simulated')
                ax.set_xlim(x_.min(),x_.max())
                ax.set_xlabel('ln(AR)',fontsize=label_font_size)
                ax.set_ylabel('Probability density',fontsize=label_font_size)
                ax.spines[   'top'].set_linewidth(1.5)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines[  'left'].set_linewidth(1.5)
                ax.spines[ 'right'].set_linewidth(1.5)
                ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.set_title('{0}. RMSE = {1:.4f}, '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '),fontsize=label_font_size)
                ax.legend(fontsize=11,loc=1,frameon=False) 
                file_name = fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(i+1)+'.'+fig_path.split('.')[-1])
                plt.savefig(file_name, transparent=True, dpi=300, pad_inches = 0.1, bbox_inches = 'tight')
                plt.clf()
                plt.close('all')
                files_list.append(file_name)
                
        return files_list

    def view_result_save_xls_single(self,fig_path): # save in xls
        from scipy.stats import gaussian_kde
        import numpy as np
        import pandas as pd
        if self.method_to_calc == 'gaussian_kde':
            x_ = np.linspace(0,3,150)
            dict_ = {}
            dict_['x'] = x_
            dict_['sample'] = gaussian_kde(self.data_to_calc[np.where(self.data_to_calc < 3)])(x_)
            for i in range(len(self.result_single)):
                dict_['{0}. RMSE = {1:.4f}, '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = ')] = self.database_kde[self.result_single[i][0]]
            
            df = pd.DataFrame(dict_)
            df.index = range(1,len(df) + 1)
            df = df.T
            df.to_excel(fig_path)
        
        if self.method_to_calc == 'histogram':
            x_ = np.linspace(0,3,self.hist_bin_num_to_calc+1)
            dict_ = {}
            n_src,bins_src = np.histogram(self.data_to_calc, bins = x_, range = (x_.min(),x_.max()), density = True)
            mid_src = (bins_src[0:-1]+bins_src[1:])/2
            dict_['x'] = mid_src
            dict_['sample']  = n_src
            for i in range(len(self.result_single)):
                dict_['{0}. RMSE = {1:.4f}, '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = ')] = self.database_hist[self.result_single[i][0]]
            df = pd.DataFrame(dict_)
            df.index = range(1,len(df) + 1)
            df = df.T
            df.to_excel(fig_path)
    
    def view_result_save_files_single(self):
        import time
        import os
        from zipfile import ZipFile 
        def write_to_notes_in_save_files(name_temp):
            self.notes_text.configure(state='normal')
            self.notes_text.insert(tk.END,'\n'+name_temp.split('/')[-1]+' has been saved!')
            self.notes_text.see(tk.END)
            self.notes_text.configure(state='disable')       
        
        def bundle_into_one_file(fname,file_names):         
            
            zip_output = ZipFile(fname,'w')  #对大于4G的文件也可以操作
            for name in file_names:
                zip_output.write(name,name.split('/')[-1])
                os.remove(name)  
            zip_output.close()
            
            print()
            print('[{0}] saved.'.format(fname))
            print()
            
             
        fname_temp = tk.filedialog.asksaveasfilename(title='Save Results', defaultextension=".*" , filetypes = (("html files","*.html"),('excel','*.xlsx'),('png','*.png.zip'),('eps','*.eps.zip'),('pdf','*.pdf.zip'),('svg','*.svg.zip'),("all files","*.*")))
        self.view_result_TopLevel.lift()
        
        
        if str(fname_temp).endswith('.html'):
            fname = ".".join(fname_temp.split('.')[0:-1]) + '-' +str(int(time.time()))+'.html'
            with open(fname,'w') as f:
                f.write(self.view_result_html_single())
            write_to_notes_in_save_files(fname)    
            
        elif str(fname_temp).endswith('.xlsx'):
            fname = ".".join(fname_temp.split('.')[0:-1]) + '-' +str(int(time.time()))+'.xlsx'
            files = self.view_result_save_xls_single(fname)
            # print(files)
            write_to_notes_in_save_files(fname)
            # bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.png.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.png.zip'
            files = self.view_result_save_fig_other_formats_single(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.eps.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.eps.zip'
            files = self.view_result_save_fig_other_formats_single(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.pdf.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.pdf.zip'
            files = self.view_result_save_fig_other_formats_single(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.svg.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.svg.zip'
            files = self.view_result_save_fig_other_formats_single(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
             
    def fig_to_html(self,fig_data):
        from io import BytesIO
        import base64
        figfile = BytesIO()
        fig_data.savefig(figfile,format='png')
        figfile.seek(0)
        fig_data_png = base64.b64encode(figfile.getvalue()).decode('utf-8')
        img_str = '<img src="data:image/png;base64,'+fig_data_png+'">\n'
        return img_str      

    def view_result_canvas_scroll_action(self,event):
        self.view_result_canvas.configure(scrollregion=self.view_result_canvas.bbox("all"))#,width=500,height=500)

    def view_result_canvas_mouse_scroll(self,event):
        self.view_result_canvas.yview_scroll(-1*int(event.delta/80), "units")
        
    def view_result_draw_action_single(self):
        # import numpy as np
        fig_list = []
        if self.method_to_calc == 'gaussian_kde':
            for i in range(len(self.result_single)):
                t = tk.Label(self.view_result_frame_in_canvas,text='{0}. RMSE = {1:.4f},    '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '))
                t.grid(sticky=tk.W)
                t.configure(font="-family {Arial} -size 12")
                t.configure(background="#d9d9d9")
                fig = self.view_result_fit_kde_plot_func(self.result_single[i][0],self.database_kde[self.result_single[i][0]])                                                        
                fig_list.append(fig)
                f = tk.Frame(self.view_result_frame_in_canvas)
                f.grid(sticky=tk.N+tk.E)
                c = FigureCanvasTkAgg(fig, master=f)
                c.draw() 
                c.get_tk_widget().grid(ipadx=80,ipady=80,sticky=tk.S+tk.E)
                l = tk.Label(self.view_result_frame_in_canvas,text='==================================')
                l.configure(font="-family {Arial} -size 12")
                l.configure(background="#d9d9d9")
                l.grid(sticky=tk.W+tk.N)
        elif self.method_to_calc == 'histogram':
            for i in range(len(self.result_single)):
                t = tk.Label(self.view_result_frame_in_canvas,text='{0}. RMSE = {1:.4f},    '.format(i+1,self.result_single[i][1])+self.result_single[i][0].replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '))
                t.grid(sticky=tk.W)
                t.configure(font="-family {Arial} -size 12")
                t.configure(background="#d9d9d9")
                fig = self.view_result_fit_hist_plot_func(self.result_single[i][0],self.database_hist[self.result_single[i][0]])
                fig_list.append(fig)
                f = tk.Frame(self.view_result_frame_in_canvas)
                f.grid(sticky=tk.N+tk.E)
                c = FigureCanvasTkAgg(fig, master=f)
                c.draw()
                c.get_tk_widget().grid(ipadx=80,ipady=80,sticky=tk.S+tk.E)
                l = tk.Label(self.view_result_frame_in_canvas,text='==================================')
                l.configure(font="-family {Arial} -size 12")
                l.configure(background="#d9d9d9")
                l.grid(sticky=tk.W+tk.N)
        self.fig_single = fig_list

    def view_result_fit_kde_plot_func(self,shape_index,data,imgsize = (4,2.5),label_font_size=12,tick_font_size=10):
        from scipy.stats import gaussian_kde
        import numpy as np
        x_ = np.linspace(0,3,150)
        y1 = gaussian_kde(self.data_to_calc[np.where(self.data_to_calc < 3)])(x_)
        y2 = data
        fig = Figure(figsize=imgsize,dpi=96)
        ax = fig.add_subplot(111)
        ax.plot(x_,y1,linestyle='--', lw=2.5,color=(256/256,127/256,14/256),label='Unknown',  alpha=1)
        ax.plot(x_,y2,linestyle='-' , lw=2.5,color=(31/256,119/256,181/256),label='Simulated',alpha=1)
        ax.set_xlim(x_.min(),x_.max())
        ax.set_xlabel('ln(AR)',fontsize=label_font_size)
        ax.set_ylabel('Probability density',fontsize=label_font_size)
        ax.spines[   'top'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        ax.spines[  'left'].set_linewidth(1.5)
        ax.spines[ 'right'].set_linewidth(1.5)
        ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
        ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
        ax.set_title(shape_index.replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '),fontsize=label_font_size)
        ax.legend(fontsize=11,loc=1,frameon=False)
        # c = FigureCanvasTkAgg(fig, master=self.view_result_frame_in_canvas)
        return fig
        
    def view_result_fit_hist_plot_func(self,shape_index,data,imgsize = (4,2.5),label_font_size=12,tick_font_size=10):
        import numpy as np
        x_ = np.linspace(0,3,self.hist_bin_num_to_calc+1)
        fig = Figure(figsize=imgsize,dpi=96)
        ax = fig.add_subplot(111)
        n_src,bins_src,_ = ax.hist(self.data_to_calc, bins = x_, range = (x_.min(),x_.max()), density = True, lw=1.25,hatch='\\\\',   fill=False,edgecolor=(256/256,127/256,14/256), alpha=1)
        n_dst = data
        bins_dst = bins_src
        mid_src = (bins_src[0:-1]+bins_src[1:])/2
        mid_dst = (bins_dst[0:-1]+bins_dst[1:])/2

        ax.plot(mid_src,n_src,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(256/256,127/256,14/256),markeredgecolor='k',markeredgewidth=1.25,label='Unknown'  )
        ax.plot(mid_dst,n_dst,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(31/256,119/256,181/256),markeredgecolor='k',markeredgewidth=1.25,label='Simulated')
        ax.set_xlim(x_.min(),x_.max())
        ax.set_xlabel('ln(AR)',fontsize=label_font_size)
        ax.set_ylabel('Probability density',fontsize=label_font_size)
        ax.spines[   'top'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        ax.spines[  'left'].set_linewidth(1.5)
        ax.spines[ 'right'].set_linewidth(1.5)
        ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
        ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
        ax.set_title(str(shape_index).replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '),fontsize=label_font_size)
        ax.legend(fontsize=11,loc=1,frameon=False)
        # c = FigureCanvasTkAgg(fig, master=self.view_result_frame_in_canvas)
        return fig

    def change_method_state_multi(self):
        if self.method_multi_value.get() == 'gaussian_kde':
            self.bin_num_spin_multi.place_forget()
            self.bin_num_label_multi.place_forget()
        elif self.method_single_value.get() == 'histogram':
            pass
            # self.bin_num_spin_multi.place(relx=0.828, rely=0.308, relheight=0.059, relwidth=0.125)
            # self.bin_num_label_multi.place(relx=0.088, rely=0.308, height=25, width=232)
    
    def load_data_file_multi(self): # 加载数据
        from Modules.data_process import data_process
        self.restart_single()
        self.restart_multi()
        
        self.notes_text.configure(state='normal')
        d = data_process()   
        open_fdialog_message,fpath = d.open_fdialog()
        self.notes_text.insert(tk.END,'\n'+open_fdialog_message)
        processing_data_message,self.data_in_log = d.processing_data()
        self.notes_text.insert(tk.END,'\n'+processing_data_message+'\n')
        # # self.notes_text.update()
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')
        if fpath:
            self.activate_operation_multi()
        else:
            self.deactivate_operation_multi()
    
    '''
    def data_chunks_check_func_multi(self):
        if self.data_chunks_check_multi_value.get() == 0:
            self.data_chunks_combobox_multi_value.set(0)
            self.data_chunks_combobox_multi.configure(state='disable')
        elif self.data_chunks_check_multi_value.get() == 1:
            self.data_chunks_combobox_multi_value.set(500)
            self.data_chunks_combobox_multi.configure(state='normal')  
    '''
    
    def multiple_processing_check_func_multi(self):
        if self.multiple_processing_check_multi_value.get() == 0:
            self.multiple_processing_spin_multi_value.set(0)
            self.multiple_processing_spin_multi.configure(state='disable')
            self.data_chunks_multi.configure(foreground="#a3a3a3")
        elif self.multiple_processing_check_multi_value.get() == 1:
            self.multiple_processing_spin_multi_value.set(2)
            self.multiple_processing_spin_multi.configure(state='normal')
            self.data_chunks_multi.configure(foreground="#000000")
        
    def get_parameters_multi(self):
        self.notes_text.configure(state='normal')
        self.data_to_calc = self.data_in_log
        self.method_to_calc = self.method_multi_value.get()
        self.repeat_times_to_calc = int(self.repeat_times_multi_value.get())
        self.shape_num_to_calc = int(self.shape_num_spin_multi_value.get())
        self.step_size_to_calc = float(self.step_size_spin_multi_value.get())
        
        try:
            self.hist_bin_num_to_calc = int(self.bin_num_spin_multi.get())
        except:
            self.notes_text.insert(tk.END,'\n'+'Invalid bin number!')
            self.hist_bin_num_to_calc = 30
            
        try:
            self.best_match_to_calc = int(self.best_match_spin_multi.get())
        except:
             self.notes_text.insert(tk.END,'\n'+'Invalid best-match data!')
             self.best_match_to_calc = 5
             
        try:
            self.view_result_TopLevel.destroy() ##### destroy view results window
        except:
            pass
             
        self.notes_text.see(tk.END)
        
        if self.shape_num_to_calc > 3:
            self.notes_text.insert(tk.END,'\n'+'********* Warning *********')
            self.notes_text.insert(tk.END,'\n'+'Estimation of shapes more than 3 may take a long time.')
            self.notes_text.insert(tk.END,'\n'+'*****************************')   
        if self.shape_num_to_calc < 2:
            self.notes_text.insert(tk.END,'\n'+'***************************')
            self.notes_text.insert(tk.END,'\n'+'Shape num should be no less than 2. Or use single shape mode instead. The shape num is set to 2.')
            self.notes_text.insert(tk.END,'\n'+'***************************')
            self.shape_num_to_calc = 2
            #self.shape_num_spin_multi_value = 2
            
        self.notes_text.insert(tk.END,'\n\n'+'-----Parameters-----')
        self.notes_text.insert(tk.END,'\n'+'Method --> {0}'.format(self.method_to_calc))
        # self.notes_text.insert(tk.END,'\n'+'Repeat times --> {0}'.format(self.repeat_times_to_calc))
        if self.method_multi_value.get() == 'histogram':
            self.notes_text.insert(tk.END,'\n'+'Bin numbers of the histogram --> {0}'.format(self.hist_bin_num_to_calc))
        self.notes_text.insert(tk.END,'\n'+'Number of shapes --> {0}'.format(self.shape_num_to_calc))
        #self.notes_text.insert(tk.END,'\n'+'Step size --> {0}'.format(self.step_size_to_calc))
        self.notes_text.insert(tk.END,'\n'+'Top [{0}] best-match results will be selected'.format(self.best_match_to_calc))
        
        if self.multiple_processing_check_multi_value.get() == 1:
            self.multiple_processing_to_calc = int(self.multiple_processing_spin_multi_value.get())
            self.notes_text.insert(tk.END,'\n'+'Multiple processors for calculation --> {0}'.format(self.multiple_processing_to_calc))
        elif self.multiple_processing_check_multi_value.get() == 0:
            self.multiple_processing_to_calc = None
        
        if self.data_chunks_check_multi_value.get() == 1:
            self.data_chunk_to_calc = int(self.data_chunks_combobox_multi_value.get())
            self.memory_saving_state_multi = True
            self.notes_text.insert(tk.END,'\n'+'Number of data chunks --> {0}'.format(self.data_chunk_to_calc))
        elif self.data_chunks_check_multi_value.get() == 0:
            self.data_chunk_to_calc = 0
            self.memory_saving_state_multi = False
            
        self.notes_text.insert(tk.END,'\n'+'---------------------------\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')  
        self.run_button_multi.configure(state='normal')
   
    def run_multi(self):
        from Modules.shape_fit import ShapeFit
        # import pickle
        import configparser
        config = configparser.ConfigParser()
        try:
            config.read('./config.ini',encoding='utf-8')
        except:
            # pass
            config.read('./config.ini', encoding='utf-8-sig')
        #if config.get('config','portable') == '1':
        #     env = 'python'
        #     idp = ''
        #else:
        if config.get('config','python_env') != '':
            env = config.get('config','python_env')
        else:
            env = 'python'
            
        if config.get('config','python_loc') != '':
            idp = config.get('config','python_loc')
        else:
            idp = ''
        #if config.get('config','portable') == '1':
        #    print('portable: {0}'.format(True))
        print('python_env = {0}'.format(env))
        print('python_loc = {0}'.format(idp))
        self.notes_text.configure(state='normal')
        self.notes_text.insert(tk.END,'\n'+'**********************\n'+'Calculation in progress...\n')
        calc_message,self.result_multi = ShapeFit(self.data_to_calc,self.shape_num_to_calc,method=self.method_to_calc,top_R=self.best_match_to_calc).main(pool_num=self.multiple_processing_to_calc,python_env=env,idp_loc=idp)
        self.notes_text.insert(tk.END,'\n'+calc_message)
        self.notes_text.insert(tk.END,'**********************')
        self.notes_text.insert(tk.END,'\n+++++ Results +++++\n')
        
        # with open('data_result.pickle','rb') as f:
        #     self.result_multi = pickle.load(f)
        self.get_database()
        times = 0
        for result in self.result_multi:
            times += 1
            shape_output = ''
            for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                shape_output += (shape_str + ' + ')
            shape_output_1 = ''
            self.notes_text.insert(tk.END,'\n{0}. RMSE = {1:.4f}\n'.format(times,result[1]))
            self.notes_text.insert(tk.END,'{0}\n'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',':').replace('+ ','+\n'))
            self.notes_text.insert(tk.END,'{0}\n'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',':').replace('+ ','+\n'))              
        self.notes_text.insert(tk.END,'+++++++++++++++++++\n')
        self.notes_text.see(tk.END)
        self.notes_text.configure(state='disable')
        self.view_results_button_multi.configure(state='normal')
        # with open('data_result.pickle','wb') as f:
        #     pickle.dump(self.result_multi,f,pickle.HIGHEST_PROTOCOL)
        

        # print(self.result_multi)
    
    def open_view_result_multi(self):
        self.view_result_TopLevel = tk.Toplevel(self.top)
        self.view_result_TopLevel.title("View results")
        self.view_result_TopLevel.geometry("580x747+601+130")
        self.view_result_TopLevel.minsize(580, 400)
        self.view_result_TopLevel.maxsize(580,800)
        self.view_result_TopLevel.resizable(1,  1)
        # self.view_result_TopLevel.attributes("-topmost", True)
        # view_result_TopLevel.title("New Toplevel")
        self.view_result_TopLevel.configure(background="#d9d9d9")
        
        self.view_result_frame = tk.Frame(self.view_result_TopLevel)
        self.view_result_frame.place(relx=0.008, rely=0.011, relheight=0.982, relwidth=0.983)
        self.view_result_frame.configure(relief='groove')
        self.view_result_frame.configure(borderwidth="1")
        self.view_result_frame.configure(relief="groove")
        self.view_result_frame.configure(background="#d9d9d9")

        self.view_result_canvas = tk.Canvas(self.view_result_frame)
        self.view_result_canvas.place(relx=0.008, rely=0.068, relheight=0.93, relwidth=0.985)
        self.view_result_canvas.configure(background="#d9d9d9")
        self.view_result_canvas.configure(insertbackground="black")
        self.view_result_canvas.configure(relief="ridge")
        self.view_result_canvas.configure(selectbackground="blue")
        self.view_result_canvas.configure(selectforeground="white")

        self.view_result_frame_in_canvas = tk.Frame(self.view_result_canvas)
        self.view_result_frame_in_canvas.place(relx=0.008, rely=0.007, relheight=0.989, relwidth=0.986)
        self.view_result_frame_in_canvas.configure(background="#d9d9d9")
        self.view_result_frame_in_canvas.configure(borderwidth="1")
        # self.view_result_frame_in_canvas.configure(insertbackground="black")
        self.view_result_frame_in_canvas.configure(relief="ridge")
        # self.view_result_frame_in_canvas.configure(selectbackground="blue")
        # self.view_result_frame_in_canvas.configure(selectforeground="white")
        
        self.view_result_canvas.create_window((0,0),window=self.view_result_frame_in_canvas,anchor='nw')
        
        self.view_result_scrollbar=tk.Scrollbar(self.view_result_frame,orient="vertical",command=self.view_result_canvas.yview)
        self.view_result_canvas.configure(yscrollcommand=self.view_result_scrollbar.set)
        self.view_result_scrollbar.pack(side="right",fill="y")

        # self.view_result_canvas.bind("<Configure>",self.view_result_canvas_scroll_action)
        # self.view_result_canvas.bind_all("<MouseWheel>",self.view_result_canvas_mouse_scroll)
        # self.view_result_draw_action_single()

        self.view_result_frame_in_canvas.bind("<Configure>",self.view_result_canvas_scroll_action)
        self.view_result_frame_in_canvas.bind_all("<MouseWheel>",self.view_result_canvas_mouse_scroll)
        self.view_result_draw_action_multi()
    
        self.view_result_save_button_multi = tk.Button(self.view_result_TopLevel,command=self.view_result_save_files_multi)
        self.view_result_save_button_multi.place(relx=0.7325, rely=0.0225, height=35, width=120)
        self.view_result_save_button_multi.configure(activebackground="#ececec")
        self.view_result_save_button_multi.configure(activeforeground="#000000")
        self.view_result_save_button_multi.configure(background="#d9d9d9")
        self.view_result_save_button_multi.configure(disabledforeground="#a3a3a3")
        self.view_result_save_button_multi.configure(font="-family {Arial} -size 10")
        self.view_result_save_button_multi.configure(foreground="#000000")
        self.view_result_save_button_multi.configure(highlightbackground="#d9d9d9")
        self.view_result_save_button_multi.configure(highlightcolor="black")
        self.view_result_save_button_multi.configure(pady="0")
        self.view_result_save_button_multi.configure(text='Save')
        
        self.view_result_TopLevel.protocol("WM_DELETE_WINDOW", self.view_result_TopLevel_close_action)


    def view_result_draw_action_multi(self):
        # import numpy as np
        fig_list = []
        if self.method_to_calc == 'gaussian_kde':
            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = '' # in a format of the ratio with a slash
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    # print(shape_tuple[1])
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_kde[shape_tuple[1]]*shape_tuple[0])
                times += 1
                t0 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t0.configure(text='{0}. RMSE = {1:.4f}'.format(times,result[1]))
                t0.grid(sticky=tk.W)
                t1 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t1.configure(text='{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n'))
                t1.grid(sticky=tk.W)
                t2 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t2.configure(text='{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n'))
                t2.grid(sticky=tk.W)                

                fig = self.view_result_fit_kde_plot_func('',np.sum(shape_output_need_for_plot,axis=0))
                fig_list.append(fig)
                f = tk.Frame(self.view_result_frame_in_canvas)
                f.grid(sticky=tk.N+tk.E) 
                c = FigureCanvasTkAgg(fig, master=f)
                c.draw() 
                c.get_tk_widget().grid(ipadx=80,ipady=80,sticky=tk.S+tk.E)
                l = tk.Label(self.view_result_frame_in_canvas,text='==================================')
                l.configure(font="-family {Arial} -size 12")
                l.configure(background="#d9d9d9")
                l.grid(sticky=tk.W+tk.N)
                
        elif self.method_to_calc == 'histogram':
            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = ''
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_hist[shape_tuple[1]]*shape_tuple[0])
                times += 1
                t0 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t0.configure(text='{0}. RMSE = {1:.4f}'.format(times,result[1]))
                t0.grid(sticky=tk.W)
                t1 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t1.configure(text='{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n'))
                t1.grid(sticky=tk.W)
                t2 = tk.Label(self.view_result_frame_in_canvas,font="-family {Arial} -size 12",background="#d9d9d9",state='normal')
                t2.configure(text='{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n'))
                t2.grid(sticky=tk.W) 
                
                # t.insert(tk.END,)
                # t.insert(tk.END,'Simulated Shape:\n')
                # t.insert(tk.END,'    {0}'.format(shape_output[:-5]).replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '))
                # t.insert(tk.END,'    {0}'.format(shape_output_1[:-5]).replace('a','S').replace('b','I').replace('c','L').replace(',',',  ').replace('=',' = '))
                # t.grid(sticky=tk.W)
                # 
                # t.configure()   
                fig = self.view_result_fit_hist_plot_func('',np.sum(shape_output_need_for_plot,axis=0))
                fig_list.append(fig)
                f = tk.Frame(self.view_result_frame_in_canvas)
                f.grid(sticky=tk.N+tk.E)
                c = FigureCanvasTkAgg(fig, master=f)
                c.draw()
                c.get_tk_widget().grid(ipadx=80,ipady=80,sticky=tk.S+tk.E)
                l = tk.Label(self.view_result_frame_in_canvas,text='==================================')
                l.configure(font="-family {Arial} -size 14")
                l.configure(background="#d9d9d9")
                l.grid(sticky=tk.W+tk.N)
        self.fig_multi = fig_list

    
    def view_result_html_multi(self):
        html_str = ''
        html_str += '<!DOCTYPE html>\n'
        html_str += '<html>\n'
        html_str += ' '*4+'<head>\n'
        html_str += ' '*8+'<title>Results</title>\n'
        html_str += ' '*8+'<h3>Results of recognizing multiple populations</h3>\n'
        html_str += ' '*4+'</head>\n'
        html_str += ' '*4+'<body>\n'
        times=0
        for result in self.result_multi:
            html_str += ' '*8 +'<p>'+ ('-'*75)+'<br/>\n'
            times += 1
            shape_output = ''
            for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                shape_output += (shape_str + ' + ')
            shape_output_1 = ''
            # shape_output_need_for_plot = []
            # for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
            #     shape_output_1 += ('%i/%i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
            #     shape_output_need_for_plot.append(self.view_result_mean_rand_pick_func(shape_tuple[1],int(shape_tuple[0]*len(self.data_to_calc))))
            html_str += ' '*12+('\n{0}. RMSE = {1:.4f}\n'.format(times,result[1])+'<br/>\n')
            html_str += ' '*12+('{0}\n'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',':').replace('+ ','+\n')+'<br/>\n')
            html_str += ' '*12+('{0}\n'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',':').replace('+ ','+\n')+'<br/>\n')
            html_str += ' '*12+self.fig_to_html(self.fig_multi[times-1])
            html_str += ' '*8+'</p>\n'
            html_str += ' '*8+ '<br/>\n'
        html_str += ' '*8+'<p>'+('='*75)+'</p>\n'
        html_str += ' '*4+'</body>\n'
        html_str += '</html>\n'
        return html_str


    def view_result_save_fig_other_formats_multi(self,fig_path,imgsize = (4,2.5),label_font_size=10,tick_font_size=10): # save in multiple formats except html and xls
        from scipy.stats import gaussian_kde
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib as mpl
        mpl.rcParams["font.family"] = 'Helvetica'
        mpl.rcParams['svg.fonttype'] = 'none'
        # import numpy as np

        files_list = []
        if self.method_to_calc == 'gaussian_kde':
            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = ''
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    # print(shape_tuple[1])
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_kde[shape_tuple[1]]*shape_tuple[0])
                times += 1
                
                ax = plt.gca()
                x_ = np.linspace(0,3,150)
                y1 = gaussian_kde(self.data_to_calc[np.where(self.data_to_calc < 3)])(x_)
                y2 = np.sum(shape_output_need_for_plot,axis=0)

                title_text = \
                    '{0}. RMSE = {1:.4f}\n'.format(times,result[1]) + \
                    '{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n') + '\n\n' +\
                    '{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n')
                
                ax.set_title(title_text,fontsize=label_font_size)
  
                ax.plot(x_,y1,linestyle='--', lw=2.5,color=(256/256,127/256,14/256),label='Unknown',  alpha=1)
                ax.plot(x_,y2,linestyle='-' , lw=2.5,color=(31/256,119/256,181/256),label='Simulated',alpha=1)
                ax.set_xlim(x_.min(),x_.max())
                ax.set_xlabel('ln(AR)',fontsize=label_font_size)
                ax.set_ylabel('Probability density',fontsize=label_font_size)
                ax.spines[   'top'].set_linewidth(1.5)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines[  'left'].set_linewidth(1.5)
                ax.spines[ 'right'].set_linewidth(1.5)
                ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.legend(fontsize=11,loc=1,frameon=False)
                file_name = fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(times)+'.'+fig_path.split('.')[-1])
                # file_name = fig_path+'/'+fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(i+1)+'.'+fig_path.split('.')[-1])
                
                plt.savefig(file_name, transparent=True, dpi=300, pad_inches = 0.1, bbox_inches = 'tight')
                plt.clf()
                plt.close('all')
                files_list.append(file_name)
                
        if self.method_to_calc == 'histogram':
            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = ''
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    # print(shape_tuple[1])
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_hist[shape_tuple[1]]*shape_tuple[0])
                times += 1
                
                ax = plt.gca()
                x_ = np.linspace(0,3,self.hist_bin_num_to_calc+1)
                n_src,bins_src,_ = ax.hist(self.data_to_calc, bins = x_, range = (x_.min(),x_.max()), density = True, lw=1.25,hatch='\\\\',   fill=False,edgecolor=(256/256,127/256,14/256), alpha=1)
                n_dst = np.sum(shape_output_need_for_plot,axis=0)
                bins_dst = bins_src
                mid_src = (bins_src[0:-1]+bins_src[1:])/2
                mid_dst = (bins_dst[0:-1]+bins_dst[1:])/2
                
                title_text = \
                    '{0}. RMSE = {1:.4f}'.format(times,result[1]) + ' \n ' + \
                    '{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n') + '\n\n ' + \
                    '{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n')
                ax.set_title(title_text,fontsize=label_font_size)
                
                ax.plot(mid_src,n_src,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(256/256,127/256,14/256),markeredgecolor='k',markeredgewidth=1.25,label='Unknown'  )
                ax.plot(mid_dst,n_dst,lw=1.5,color='k', marker='s',markersize=7.5,markerfacecolor=(31/256,119/256,181/256),markeredgecolor='k',markeredgewidth=1.25,label='Simulated')
                ax.set_xlim(x_.min(),x_.max())
                ax.set_xlabel('ln(AR)',fontsize=label_font_size)
                ax.set_ylabel('Probability density',fontsize=label_font_size)
                ax.spines[   'top'].set_linewidth(1.5)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines[  'left'].set_linewidth(1.5)
                ax.spines[ 'right'].set_linewidth(1.5)
                ax.tick_params(axis = 'x', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.tick_params(axis = 'y', labelsize =tick_font_size ,direction = 'out',length=4, width=1.5)
                ax.legend(fontsize=11,loc=1,frameon=False) 
                file_name = fig_path.split('/')[-1].replace('.'+fig_path.split('.')[-1],'-'+str(times)+'.'+fig_path.split('.')[-1])
                plt.savefig(file_name, transparent=True, dpi=300, pad_inches = 0.1, bbox_inches = 'tight')
                plt.clf()
                plt.close('all')
                files_list.append(file_name)
                
        return files_list

    def view_result_save_xls_multi(self,fig_path): # save in xls
        from scipy.stats import gaussian_kde
        import numpy as np
        import pandas as pd
        if self.method_to_calc == 'gaussian_kde':
            x_ = np.linspace(0,3,150)
            dict_ = {}
            dict_['x'] = x_
            dict_['sample'] = gaussian_kde(self.data_to_calc[np.where(self.data_to_calc < 3)])(x_)
            
            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = ''
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    # print(shape_tuple[1])
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_kde[shape_tuple[1]]*shape_tuple[0])
                times += 1
                title_text = \
                    '{0}. RMSE = {1:.4f}'.format(times,result[1]) + '\n ' + \
                    '{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n') + '\n' + '\n'\
                    '{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n')
                dict_[title_text] = np.sum(shape_output_need_for_plot,axis=0)
                
            df = pd.DataFrame(dict_)
            df.index = range(1,len(df) + 1)
            df = df.T
            df.to_excel(fig_path)
        
        if self.method_to_calc == 'histogram':
            x_ = np.linspace(0,3,self.hist_bin_num_to_calc+1)
            dict_ = {}
            n_src,bins_src = np.histogram(self.data_to_calc, bins = x_, range = (x_.min(),x_.max()), density = True)
            mid_src = (bins_src[0:-1]+bins_src[1:])/2
            dict_['x'] = mid_src
            dict_['sample']  = n_src

            times = 0
            for result in self.result_multi:
                shape_output = ''
                for shape_str in ['%.f%% %s' % ((float(shape_x[0])*100),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    shape_output += (shape_str + ' + ')
                shape_output_1 = ''
                shape_output_need_for_plot = []
                for shape_tuple in [(float(shape_x[0]),shape_x[1]) for shape_x in [R_index.split('*') for R_index in result[0].split('+')]]:
                    # print(shape_tuple[1])
                    shape_output_1 += ('%i/ %i %s + ' % (round(shape_tuple[0]*len(self.data_to_calc)),int(len(self.data_to_calc)),shape_tuple[1]))
                    shape_output_need_for_plot.append(self.database_hist[shape_tuple[1]]*shape_tuple[0])
                times += 1
                title_text = \
                    '{0}. RMSE = {1:.4f}'.format(times,result[1]) + '\n' + \
                    '{0}'.format(shape_output[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n') + '\n' + '\n'\
                    '{0}'.format(shape_output_1[:-3]).replace('a=','').replace('b=','').replace('c=','').replace(',',': ').replace('+ ','+\n')
                dict_[title_text] = np.sum(shape_output_need_for_plot,axis=0)            
                
            df = pd.DataFrame(dict_)
            df.index = range(1,len(df) + 1)
            df = df.T
            df.to_excel(fig_path)
 
    
    def view_result_save_files_multi(self):
        import time
        import os
        from zipfile import ZipFile 
        def write_to_notes_in_save_files(name_temp):
            self.notes_text.configure(state='normal')
            self.notes_text.insert(tk.END,'\n'+name_temp.split('/')[-1]+' has been saved!')
            self.notes_text.see(tk.END)
            self.notes_text.configure(state='disable')       
        
        def bundle_into_one_file(fname,file_names):

            zip_output = ZipFile(fname,'w')  #对大于4G的文件也可以操作
            for name in file_names:
                zip_output.write(name,name.split('/')[-1])
                os.remove(name)
                
            zip_output.close()
            print()
            print('[{0}] saved.'.format(fname))
            print()
             
        fname_temp = tk.filedialog.asksaveasfilename(title='Save Results', defaultextension=".*" , filetypes = (("html files","*.html"),('excel','*.xlsx'),('png','*.png.zip'),('eps','*.eps.zip'),('pdf','*.pdf.zip'),('svg','*.svg.zip'),("all files","*.*")))
        self.view_result_TopLevel.lift()

        if str(fname_temp).endswith('.html'):
            fname = ".".join(fname_temp.split('.')[0:-1]) + '-' +str(int(time.time()))+'.html'
            with open(fname,'w') as f:
                f.write(self.view_result_html_multi())
            write_to_notes_in_save_files(fname)    
            
        elif str(fname_temp).endswith('.xlsx'):
            fname = ".".join(fname_temp.split('.')[0:-1]) + '-' +str(int(time.time()))+'.xlsx'
            files = self.view_result_save_xls_multi(fname)
            # print(files)
            write_to_notes_in_save_files(fname)
            # bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.png.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.png.zip'
            files = self.view_result_save_fig_other_formats_multi(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.eps.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.eps.zip'
            files = self.view_result_save_fig_other_formats_multi(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.pdf.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.pdf.zip'
            files = self.view_result_save_fig_other_formats_multi(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)
            
        elif str(fname_temp).endswith('.svg.zip'):
            fname = ".".join(fname_temp.split('.')[0:-2]) + '-' +str(int(time.time()))+'.svg.zip'
            files = self.view_result_save_fig_other_formats_multi(fname[0:-4])
            # print(files)
            write_to_notes_in_save_files(fname)
            bundle_into_one_file(fname.split('/')[-1],files)

    def restart_multi(self):
        self.data_to_calc = None
        self.method_to_calc = ''
        self.repeat_times_to_calc = None
        self.hist_bin_num_to_calc = None
        self.best_match_to_calc = None
        self.step_size_to_calc = None
        self.shape_num_to_calc = None
        self.result_multi = None
        self.data_chunk_to_calc = None
        self.multiple_processing_to_calc = None
        self.memory_saving_state_multi = False
        self.fig_multi = []

        self.repeat_times_combobox_multi.set('0')
        self.histogram_select_button_multi.select()
        self.bin_num_multi_value.set(30)
        self.best_match_spin_multi_value.set(5)
        self.multiple_processing_check_multi_value.set(0)
        self.data_chunks_check_multi_value.set(0)
        self.notes_text.configure(state='normal')
        self.notes_text.delete(1.0,tk.END)
        # self.notes_text.insert(tk.END,'++++++ Restart ++++++\n')
        self.notes_text.configure(state='disable')
        # self.bin_num_label_multi.place(relx=0.088, rely=0.308, height=25, width=232)
        # self.bin_num_spin_multi.place(relx=0.828, rely=0.308, relheight=0.059, relwidth=0.125)
        self.deactivate_operation_multi()
        try:
            self.view_result_TopLevel.destroy() #####
        except:
            pass            

        
if __name__ == '__main__':
    vp_start_gui()





