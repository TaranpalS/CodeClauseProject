import pyperclip 
import pyshorteners

from tkinter import *          

import urlshortener as urlshortener
root= Tk()

root.title("URL Shortener")

root.configure(bg="#49A")

url=StringVar()
url_address= StringVar()

def urlshortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)

def copyurl():
        url_short = url_address.get()
        pyperclip.copy(url_short)

Label(root , text= "My URL Shortener", font="poppins").pack(pady=11)
Entry(root,textvariable=url).pack(pady=6)
Button(root , text= "Generate Short URL", command=urlshortener).pack(pady=8)
Entry(root,textvariable=url_address).pack(pady=6)
Button(root , text= "Copy URL", command=copyurl).pack(pady=6)

root.mainloop()