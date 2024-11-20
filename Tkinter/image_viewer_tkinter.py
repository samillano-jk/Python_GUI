from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icon and Images GUI")
root.iconbitmap(r"C:\Users\samil\Downloads\bnb_crypto_icon_264371.ico")

# importing the images to be compatible to tkinter
img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\samil\Downloads\cat_pics\img1.jpg"))
img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\samil\Downloads\cat_pics\img2.jpg"))
img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\samil\Downloads\cat_pics\img3.jpg"))
img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\samil\Downloads\cat_pics\img4.jpg"))
img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\samil\Downloads\cat_pics\img5.jpg"))

imgs = [img1, img2, img3, img4, img5] # images list
index = 0

# Functions
def forward():
    global index, front_image
    front_image.grid_forget()
    index += 1
    front_image = Label(root, image=imgs[index], borderwidth=10)

    if index > 3: # list length - 2
        button_forward.config(state="disabled")

    # update the backward button to be enabled
    button_back.config(state="normal")

    # placements
    front_image.grid(row=0, column=0, columnspan=3)


def backward():
    global index, front_image
    button_forward.config(state="normal") # This enables the forward button after reaching the end
    if index <= 0:
        button_back.config(state="disabled")
        
    else:   
        index -= 1
        front_image.grid_forget()
        front_image = Label(root, image=imgs[index], borderwidth=10)
        front_image.grid(row=0, column=0, columnspan=3)

        if index <= 0:
            button_back.config(state="disabled")

    
# Image
front_image = Label(image=img1, borderwidth=10)
front_image.grid(row=0, column=0, columnspan=3)

# Buttons
button_back = Button(root, text="<", borderwidth=2, command=backward, state="disabled")
button_exit = Button(root, text="Exit", borderwidth=2, command=root.quit)
button_forward = Button(root, text=">", borderwidth=2, command=forward)

# Button Placements
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Loop
root.mainloop()