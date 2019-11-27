from tkinter import *
class Gui(Tk):

    def __init__(self):
        super().__init__()


        self.cactusleaves_image =PhotoImage(file="//pclures02/home/4greee92/Documents/PG/COM404/cactus1.gif")
        self.tenor_image = PhotoImage(file="//pclures02/home/4greee92/Documents/PG/COM404/tenor.gif")
        
        self.title("Gui")

        self.__add_heading_label()
        self.__add_cactusleaves_image()
        self.__add_flip_button()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        #style
        self.heading_label.configure(text="Cactus Leaves", font="Arial 38")

    def __add_cactusleaves_image(self):
        self.cactusleaves_label = Label()
        self.cactusleaves_label.grid(row=1, column=0)
        self.cactusleaves_label.configure(image=self.cactusleaves_image, height=360, width=360)

    def __add_tenor_image(self):
        self.tenor_label = Label()
        self.tenor_label.grid(row=1, column=0)
        self.tenor_label.configure(image=self.cactusleaves_image, height=360, width=360)

    def __add_flip_button(self):
        self.flip_button =Button()
        self.flip_button.grid(row=3, column=0)
        self.flip_button.configure(text="Flip")
        self.flip_button.bind("<Button-1>", self.__flip_button_clicked)
        self.flip_button.bind("<Button-3>", self.__flip_button_clickedright)

    def __flip_button_clicked(self, event):
        self.cactusleaves_label.configure(image = self.tenor_image)
    def __flip_button_clickedright(self, event):
        self.cactusleaves_label.configure(image = self.cactusleaves_image)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()




