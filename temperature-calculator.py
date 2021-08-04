# This program will convert temperature to
# either Farenheit or Celcius

import tkinter

class TempConvertGUI:
    def __init__(self):

        # The main window.
        self.main_window = tkinter.Tk()

        # Four frames for the GUI.
        self.fahrenheit_frame = tkinter.Frame()
        self.celcius_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Widgets for the Fahrenheit
        # and Celcius frames.
        self.prompt_label1 = tkinter.Label(self.fahrenheit_frame,
                    text='Enter a temperature in Fahrenheit:')
        self.temp_entry1 = tkinter.Entry(self.fahrenheit_frame,
                                        width=10)
        self.prompt_label2 = tkinter.Label(self.celcius_frame,
                    text='Enter a temperature in Celcius:')
        self.temp_entry2 = tkinter.Entry(self.celcius_frame,
                                        width=10)

        # Packs the the widgets for the Fahrenheit
        # and Celcius frames.
        self.prompt_label1.pack(side='left')
        self.temp_entry1.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.temp_entry2.pack(side='left')

        # Widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to F or C:')

        
        # StringVar object to associate with
        # an output label. 
        self.value = tkinter.StringVar()

        # Label associated with StringVar object it with the
        # StringVar object. 
        self.temp_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        # Pack the middle frame's widgets.
        self.descr_label.pack(side='left')
        self.temp_label.pack(side='left')

        # Button widgets for the bottom frame.
        self.celcius_button = tkinter.Button(self.bottom_frame,
                                          text='Celcius',
                                          command=self.convert1)
        self.fahrenheit_button = tkinter.Button(self.bottom_frame,
                                          text='Fahrenheit',
                                          command=self.convert2)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.celcius_button.pack(side='left')
        self.fahrenheit_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.fahrenheit_frame.pack()
        self.celcius_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # The tkinter main loop.
        tkinter.mainloop()

    # Callback method for the Calculate button.    
    def convert1(self):
        
        # Get the value entered for Celcius.
        temp = float(self.temp_entry1.get())    

        # Convert Celcius to Fahrenheit.
        fahrenheit = ((9/5) * temp) + 32  

        # Converts and formats for one decimal place.
        self.value.set(format(fahrenheit,',.1f'))

    def convert2(self):
        # Get the value entered for Fahrenheit.
        temp = float(self.temp_entry2.get())

        # Convert Fahrenheit to Celcius.
        celcius = (temp-32)/(9/5)

        # Converts and formats for one decimal place.
        self.value.set(format(celcius,',.1f'))

# Instance of the TempConvertGUI Class
temp_conv = TempConvertGUI()
