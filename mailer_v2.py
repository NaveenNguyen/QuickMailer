from tkinter import *
import tkinter.messagebox
import smtplib

def domain(val):

 #google
    while 'gmail' in val:
        pro = 'smtp.gmail.com:587'
        return pro
 
 #outlook
    while 'outlook' in val:
        pro = 'smtp-mail.outlook.com:587'
        return pro
 #msn
    while 'msn' in val:
        pro = 'smtp.email.msn.com:587'
        return pro
 #hotmail
    while 'live' in val:
        pro = 'smtp.live.com:587'
        return pro
 #yahoo
    while 'ymail' or 'yahoo' in  val:
        pro = 'smtp.mail.yahoo.com:587'
        return pro
    
    
def send():
    print ("Sender : %s " % sen.get())
    print ("Receiver : %s " % rec.get())
    print ("Message : %s " % msg.get())
    pr = domain(sen.get())
        
    try:
        server = smtplib.SMTP(pr)
        server.ehlo()
        server.starttls()
        server.login(sen.get(),pas.get())

        server.sendmail(sen.get(),rec.get(),msg.get())
        messagebox.showinfo("Information","Mail Sent Successfully.")
        server.quit()
       

    except:
        messagebox.showerror("Message not sent", "Check your credentials")


def closebox():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        return root.destroy()


root = Tk()
root.title("Quick Mail")
intro = Label(root, text="This is a very simple GUI to send mail using any mail domains", fg="green")
intro.pack()

sen = StringVar()
pas = StringVar()
rec = StringVar()
msg = StringVar()

Label(root, text="From address").pack()
Entry(root,textvariable=sen).pack()

Label(root, text="Password").pack()
Entry(root,textvariable=pas).pack()

Label(root, text="To address").pack()
Entry(root,textvariable=rec).pack()

Label(root, text="Enter your message").pack()
Entry(root,textvariable=msg).pack()

    
Button(root,text="Send",fg='Green', command=send).pack(side = RIGHT)
Button(root,text="Cancel",fg='Red', command=closebox).pack(side = LEFT)
root.mainloop()
