from tkinter import *
from tkinter import messagebox
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Tickets")

        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()


    def __add_heading_label(self):
        #create
        self.heading_label = Label ()
        self.heading_label.grid(row=0, column=0)

        #style
        self.heading_label.configure(font="Arial 24", text ="Entrance Ticket")

    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        #self.instruction_label = sticky=w

        #style
        self.instruction_label.configure(font="Arial 18", text="How many tickets are needed")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry ()
        self.tickets_entry.grid(row=2, column=0)

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)

        self.buy_button.configure(font="Arial 18", text="submit")

    #events
        self.buy_button.bind("<Button-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        tickets = int(self.tickets_entry.get())

        if tickets == 1:
            messagebox.showinfo("Purchased!", "You have Purchased "+ str(tickets) + " ticket!")
        else:
            messagebox.showinfo("Purchased!", "You have Purchased "+ str(tickets) + " tickets!")

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()



