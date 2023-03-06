from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import Email
import re
root = Tk()
root.geometry("600x450")
root.title("Send Email")
root.config(bg = "yellow")
filename=""
def Mail(mailid):
    subject = sub.get()
    body = Body.get(1.0, "end-1c")
    valid = Email.EMailSend(mailid,filename,subject,body)
    if valid:
        messagebox.showinfo("message","Mail Sent Successfully")
    
def solve():
    mailid = emailentry.get()
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,mailid):
        Mail(mailid)
    else:
        messagebox.showinfo("message","Plz enter valid mail")
def Upload():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",
                                          filetypes = (("Text files","*.txt*"),("all files","*.*")))
    fn = filename.split("/")
    Label(text = fn[-1],font = ('Calibri',13),bg="yellow",fg="blue").place(x = 320,y=332)
def Clear(Day,Month,Year):
    Day.delete(0,END)
    Month.delete(0,END)
    Year.delete(0,END)

emailentry = StringVar()
sub = StringVar()
Label(root,text = "Email",font = ('Times New Roman',50,'bold'),anchor = CENTER,
      bg = "pink",fg = "blue",width = 20).pack()
Label(root,text = "Email:",font = ('Calibri',15),bg="yellow").place(x = 20,y=100)
email = Entry(textvariable = emailentry,font = ('Calibri',15),width = 40,relief = GROOVE).place(x = 100,y=100)
Label(root,text = "Subject:",font = ('Calibri',15),bg="yellow").place(x = 20,y=150)
subject = Entry(textvariable = sub,font = ('Comic Sans MS',15),width = 25,relief = GROOVE).place(x = 100,y=150)
Label(root,text = "Body:",font = ('Calibri',15),bg="yellow").place(x = 20,y=200)
Body = Text(root,height = 5, width = 40,font=('Century Schoolbook', 14, 'normal'))
Body.place(x=100,y=200)
Label(root,text = "Wanna Upload files?",font = ('Calibri',14),bg="yellow").place(x = 20,y=330)
B = Button(root, text ="Upload",font = ('Calibri',12,"bold"),activebackground="sky blue",cursor = "hand2",relief = GROOVE,
           bg = "light green",fg = "black",width=12,height = 1,command = Upload)
B.place(x = 200,y=330)
B = Button(root, text ="Reset",font = ('Calibri',15,"bold"),activebackground="sky blue",cursor = "hand2",relief = GROOVE,
           bg = "red",fg = "white",width=12,height = 1,command = lambda:Clear(email,subject,Body))
B.place(x = 40,y=370)
B = Button(root, text ="Send",font = ('Calibri',15,"bold"),activebackground="sky blue",cursor = "hand2",relief = GROOVE,
           bg = "blue",fg = "white",width=12,height = 1,command = solve)
B.place(x = 400,y=370)

root.mainloop()
