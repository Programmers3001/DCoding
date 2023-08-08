from tkinter import *
from tkinter import ttk
import sv_ttk
from dcoding import decode, encode

root = Tk()
root.title("DCoding GUI")
root.geometry("500x400")

entry = ttk.Entry(root, font=("Arial",18))
entry.grid(row=0,column=0,padx=120,pady=20)
entry2 = ttk.Entry(root,font=("Arial",18))
entry2.grid(row=3,column=0,padx=120,pady=20)
def checkcombo(event):
    global v
    v = deoren.get()
def button():
    text = entry.get()
    print(v)
    if v=="Decode":
        response = decode(text)
        entry2.delete(0,END)
        entry2.insert(0,response)
        history = f"{text} -> {response} (Decode)"
    elif v=="Encode":
        response = encode(text)
        entry2.delete(0,END)
        entry2.insert(0,response)
        history = f"{text} -> {response} (Encode)"
    with open('history.txt', 'w', encoding="utf-8") as f:
        f.write(history + "\n")
        f.close()
button1 = ttk.Button(root,text="Encode/Decode",command=button)
button1.grid(row=2,column=0,padx=150,pady=20)
n = StringVar()
deoren = ttk.Combobox(root, width = 27, textvariable = n, state="readonly")
deoren['values'] = ("Encode", "Decode")
deoren.current()
deoren.grid(row=1,column=0,padx=120,pady=10)
deoren.bind("<<ComboboxSelected>>", checkcombo)
sv_ttk.set_theme("dark")
root.mainloop()