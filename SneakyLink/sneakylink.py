from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb


# function to open png, jpg or text files
def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetypes=(("PNG File", "*.png"),
                                                     ("JPG File", "*.jpg"),
                                                     ("JPEG File", "*.jpeg"),
                                                     ("All Files", "*.txt")))

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img


# function to hide text inside image
def hide_text():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


# function to extract hidden text from image
def show_text():
    clear_text = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_text)


# function to save image after hiding text inside it
def save_image():
    secret.save("sneakylink.png")



# BUILDING USER INTERFACE WITH TKINTER

# creating the main window frame
root = Tk()
root.title("SneakyLink - Hide a secret text message inside an image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#333333")

# adding icon
image_icon = PhotoImage(file="cologo.png")
root.iconphoto(False, image_icon)

# adding logo and text
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#333333").place(x=10, y=0)
Label(root, text="SNEAKY LINK - Steganography", bg="#333333", fg="white", font="Lato 25 bold").place(x=100, y=20)


# first frame where photo will be shown
f1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f1.place(x=10, y=80)

lbl = Label(f1, bg="black")
lbl.place(x=40, y=10)


# second frame where text will be displayed and input
f2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, bg="white", fg="black", font="Roboto 20", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# third frame for open and save image buttons
f3 = Frame(root, bd=3, bg="#878787", width=330, height=100, relief=GROOVE)
f3.place(x=10, y=370)

Button(f3, text="Open Image", width=10, height=2,font="arial 14 bold", command=show_image).place(x=20, y=30)
Button(f3, text="Save Image", width=10, height=2,font="arial 14 bold", command=save_image).place(x=180, y=30)
Label(f3, text="Picture, Image, Photo File", bg="#878787", fg="white").place(x=20, y=5)


# fourth frame for hide and show text buttons
f4 = Frame(root, bd=3, bg="#878787", width=330, height=100, relief=GROOVE)
f4.place(x=360, y=370)

Button(f4, text="Hide Text", width=10, height=2,font="arial 14 bold", command=hide_text).place(x=20, y=30)
Button(f4, text="Show Text", width=10, height=2,font="arial 14 bold", command=show_text).place(x=180, y=30)
Label(f4, text="Picture, Image, Photo File", bg="#878787", fg="white").place(x=20, y=5)

root.mainloop()
