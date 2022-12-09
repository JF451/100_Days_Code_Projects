import tkinter as tk
from tkinter import filedialog

import PIL.Image
from PIL import Image, ImageDraw, ImageFont, ImageTk
from PIL.ImageDraw2 import Draw
from django.conf.locale import ms
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D

render = None

filename = ""


def browseFiles():
    global filename
    filename = filedialog.askopenfilename()

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)

    image = PIL.Image.open(filename)
    img = PIL.ImageTk.PhotoImage(image)


    print(filename)
    imageLabel.configure(image=img)
    imageLabel.image = img

    #Create watermark
    width, height = img.width(), img.height()
    draw = ImageDraw.Draw(image)
    text = "sample watermark"

    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    image.show()

    # Save watermarked image
    # img = Draw.MolsToGridImage()
    # toSave = filedialog.asksaveasfile(mode='w', defaultextension='.jpg')
    # img.save(toSave)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=browseFiles)
slogan.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)


# Create a File Explorer label
label_file_explorer = tk.Label(root,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

button_explore = tk.Button(root,
                        text="Browse Files",
                        command=browseFiles)

button_exit = tk.Button(root,
                     text="Exit",
                     command=exit)

label_file_explorer.pack()

button_explore.pack()

button_exit.pack()



root.mainloop()