import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.createQuitWidget()
        
##    def window(main):
##        main.title('Dice Roller')
##        main.update_idletasks()
##        width = main.winfo_width()
##        height = main.winfo_height()
##        x = (main.winfo_screenwidth() // 2) - (width // 2)
##        y = (main.winfo_screenheight() // 2) - (height // 2)
##        main.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def create_widgets(self):
        
        self.eyes = tk.Button(bottomFrame, text="Eyes")
        self.eyes.pack(side="left")
        self.talk = tk.Button(bottomFrame, text="Talk")
        self.talk.pack(side="top")
        bottomFrame.pack(side="bottom") 

    def createQuitWidget(self):
        topFrame = tk.Frame(root)
        self.quit = tk.Button(topFrame, text="QUIT", fg="black", command=root.destroy)
        self.quit.pack(side="left")
        topFrame.pack(side="top")   
 
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
##window(root)
root.geometry('500x500+700+300')

 
middleFrame = tk.Frame(root)
middleFrame.pack(side="right")
 

 
##topFrame_Label = tk.Label(topFrame, text="Welcome to Python GUI(Top Frame)")
##topFrame_Label.pack()
middleFrame_Label = tk.Label(middleFrame, text="Welcome to Python GUI(Middle Frame)")
middleFrame_Label.pack()
bottomFrame = tk.Frame(root, bg="green")
 
##bottomFrame_Label = tk.Label(bottomFrame, text="Welcome to Python GUI(Bottom Frame)")
##bottomFrame_Label.pack()
##theButton = tk.Button(bottomFrame, text="Button", fg="red", bg="black")
##theButton.pack()
#sets the window size to 300x300, 700 is the X coord and 300 is the Y coord
app = Application(master=root)
app.mainloop()
