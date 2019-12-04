from tkinter import *
from tkinter import messagebox
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
        height =500,
        width=500, padx = 10, pady =10)

        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_subscribe_button()
        self.__add_email_entry()
        


    def __add_heading_label(self):
        #create
        self.heading_label = Label ()
        self.heading_label.grid(row=0, column=0)

        #style
        self.heading_label.configure(font="Arial 14", text ="Receive our newsletter", pady= 10)

    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        #self.instruction_label = sticky=w

        #style
        self.instruction_label.configure(font="Arial 12", text="Please enter your email below to receive our newsletter", padx = 10, pady= 10,
        justify=LEFT)

    def __add_email_label(self):
        self.email_label = Label ()
        self.email_label.grid(row=2, column=0)
        self.email_label.configure(font="arial 10", text="Email",
        padx=10)

    def __add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=4, column=0)

        self.subscribe_button.configure(font="Arial 12", text="SUBSCRIBE", bg="#fee")


    def __add_email_entry(self):
        self.email_entry = Label ()
        self.email_entry.grid(row=3, column=0)
        self.email_entry.configure(bd="2", fg="#f00", width=30)
      
    

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
