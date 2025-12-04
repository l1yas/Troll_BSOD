from tkinter import Tk, Label, messagebox
from PIL import Image, ImageTk
import time

def calculator():
    print("Calculator_App.py\n")
    number_1 = int(input("Enter your first number:  "))
    operator = input("Enter your operation (+, -, *, /):    ")
    number_2 = int(input("Enter your second number: "))
    
    print("\n\nCalculating....\n\n")
    time.sleep(3)
    print(f'{number_1} {operator} {number_2} = Hello World')
    time.sleep(1)
        
def show_bsod():
    root.deiconify()
    root.attributes('-fullscreen', True)
    img = Image.open(r"bsod.png")
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    photo = ImageTk.PhotoImage(img)
    label = Label(root, image=photo)
    label.photo = photo  
    label.pack()
    root.bind("<Escape>", lambda e: root.destroy())

calculator()

root = Tk()
root.withdraw()
messagebox.showwarning("Brace For Impact", "Deleting System 32")
with open('fakelogs.txt', 'r') as file:
    for line in file:
        print(line.strip())
        time.sleep(0.01)
time.sleep(2)
show_bsod()

root.mainloop()
