import tkinter as tk 

window = tk.Tk()
window.title("drow a line")

canva = tk.Canvas(window , width=1000,height=1000)
canva.pack()
canva.create_arc(50,50,300,150,start= 0, extent= 180,style=tk.ARC , fill= "blue" ,width = 2)

canva.create_oval(160 , 70, 180,90,width= 2)
canva.create_line(50 , 100, 300, 100,fill = "black",width= 2)
canva.create_line(50 , 100, 50, 200,fill = "black",width= 2)
canva.create_line(300 , 100, 300, 200,fill = "black",width= 2)
canva.create_line(50 , 200, 300, 200,fill = "black",width= 2)

window.mainloop()



import tkinter as tk

class Hut:
    # """A class to create and display a hut on a canvas using Tkinter."""
    
    def __init__(self):
        # """Initialize the hut window and draw the components."""
        # print("Initializing Hut...")  # Debugging message
        
        self.root = tk.Tk()  # Create the main application window
        self.root.title("Hut Drawing")

        # Create a canvas for drawing the hut
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Draw components of the hut
        # try:
        self.draw_walls()    # Correct method name
        #     print("Walls drawn")  # Debug message
        # except AttributeError as e:
        #     print(f"Error drawing walls: {e}")
        
        # try:
        self.draw_roof()     # Correct method name
        #     print("Roof drawn")  # Debug message
        # except AttributeError as e:
        #     print(f"Error drawing roof: {e}")
        
        # try:
        self.draw_door()     # Correct method name
        #     print("Door drawn")  # Debug message
        # except AttributeError as e:
        #     print(f"Error drawing door: {e}")
        
        # try:
        self.draw_windows()  # Correct method name
        #     print("Windows drawn")  # Debug message
        # except AttributeError as e:
        #     print(f"Error drawing windows: {e}")

    def draw_walls(self):
        # """Draw the rectangular walls of the hut."""
        # print("Drawing walls...")  # Debugging message
        self.canvas.create_rectangle(100, 200, 400, 400, fill="white", outline="black", width=2)

    def draw_roof(self):
        # """Draw the roof of the hut as a triangle."""
        # print("Drawing roof...")  # Debugging message
        self.canvas.create_polygon(100, 200, 250, 100, 400, 200, fill="pink", outline="black", width=2)

    def draw_door(self):
        # """Draw the door of the hut as a rectangle."""
        # print("Drawing door...")  # Debugging message
        self.canvas.create_rectangle(220, 300, 280, 400, fill="green", outline="black", width=2)

    def draw_windows(self):
        # """Draw two windows on the hut."""
        # print("Drawing windows...")  # Debugging message
        # Left window
        self.canvas.create_rectangle(130, 240, 180, 290, fill="lightblue", outline="black", width=2)
        # Right window
        self.canvas.create_rectangle(320, 240, 370, 290, fill="lightblue", outline="black", width=2)
    
    def run(self):
        # """Run the Tkinter main loop."""
        # print("Starting main loop...")  # Debugging message
        self.root.mainloop()

# Instantiate and run the Hut application
if __name__ == '__main__':
    hut_app = Hut()  # Ensure the correct class name is used here
    hut_app.run()
