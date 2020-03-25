from tkinter import *
from tkinter import messagebox
from PIL import Image

def delete():
    image_name = message.get()
    image_file = open(image_name, mode="rb")
    image = Image.open(image_file)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(image_name)
    messagebox.showinfo("Success!", message="Success!")
 
root = Tk()
root.title("Metadata Deleter Pro Max")
root.geometry("300x200")

label1 = Label(text="This is Metadata Deleter Pro Max XS", fg="#0000CD")
label1.pack()
label2 = Label(text="Enter Image name", fg="#0000CD")
label2.pack()

message = StringVar()
 
message_entry = Entry(textvariable=message)
message_entry.pack()
 
message_button = Button(text="Delete Metadata", command=delete)
message_button.pack()
 
root.mainloop()