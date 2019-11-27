from tkinter import *

class Gui(Tk):
 
    def __init__(self):
        super().__init__()

        self.ambulance_image = PhotoImage(file="//pclures02/home/4greee92/Documents/PG/COM404/AE2/ambulance.gif")

        self.bike_image = PhotoImage(file="//pclures02/home/4greee92/Documents/PG/COM404/AE2/bike.gif")

        self.plane_image = PhotoImage(file="//pclures02/home/4greee92/Documents/PG/COM404/AE2/plane.gif")

        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
        
    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=0, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image, height=50,width=50)
        

    def __add_bike_image_label(self):
         self.bike_image_label = Label()
         self.bike_image_label.grid(row=0, column=1)
         self.bike_image_label.configure(image=self.bike_image,height=50,width=50)

        
 
    def __add_plane_image_label(self):
         self.plane_image_label = Label()
         self.plane_image_label.grid(row=0, column=2)
         self.plane_image_label.configure(image=self.plane_image,height=50,width=50)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()


