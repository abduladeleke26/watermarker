from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

fontNum = 0
def getImage():
        global fontNum
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.jpeg *.png")]
            )
            print(file_path)
            if file_path:
                img = Image.open(file_path)
                img.thumbnail((400, 400))
                photo = ImageTk.PhotoImage(img)
                canvas.itemconfig(waterPic,image=photo)
                fontNum = 0
                currentFont.config(text=fonts[fontNum])
                canvas.itemconfig(watermark,text="watermark",font=(fonts[fontNum],50))
                canvas.image = photo
        except:
            canvas.itemconfig(watermark,text="Try again(.PNG,,JPG,.JPEG,.GIF)")


def set():
    global fontNum
    if textt.get() == "":
        messagebox.showerror(title="empty box", message="You left text empty")
    try:
        canvas.itemconfig(watermark, text=textt.get(), font=(fonts[fontNum], int(num.get())))
    except:
        messagebox.showerror(title="empty box", message="You left the size empty")



def left():
    global fontNum
    if fontNum<0:
        fontNum = len(fonts)-1
    else:
        fontNum -= 1
    currentFont.config(text=fonts[fontNum])
    canvas.itemconfig(watermark, text=textt.get(), font=(fonts[fontNum], int(num.get())))

def right():
    global fontNum
    if fontNum > (len(fonts)-1):
        fontNum = 0
    else:
        fontNum += 1
    currentFont.config(text=fonts[fontNum])
    canvas.itemconfig(watermark, text=textt.get(), font=(fonts[fontNum], int(num.get())))

window = Tk()
window.title("WATERMARKER")
window.minsize(width=750,height=650)
fonts = list(font.families())

title = Label(text="WATERMARKER", font=("Courier",50))
title.place(x=130,y=0)

canvas = Canvas(width=500, height=490,   highlightthickness=0,borderwidth=0)
waterPic = canvas.create_image(250,250)
watermark = canvas.create_text(250,250,text="Upload you image(.PNG,,JPG,.JPEG,.GIF)")
canvas.place(x=50,y=50)









left = Button(text="<",command=left)
left.place(x=160,y=570)


currentFont = Label(text="Font")
currentFont.place(x=220,y=570)


right = Button(text=">",command=right)
right.place(x=360,y=570)

photo = Button(text="UPLOAD",command=getImage)
photo.place(x=250,y=540)

text = Label(text="Text:")
text.place(x=550,y=230)

textt = Entry(width=10)
textt.place(x=550,y=250)

size = Label(text="Size:")
size.place(x=550,y=290)

num = Entry(width=10)
num.place(x=550,y=310)

set = Button(text="SET", command=set)
set.place(x=550,y=340)






window.mainloop()
