from tkinter import *
from tkinter import ttk

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

    class LoginPage:
        def __init__(self,win):
            self.win = win
            self.win.geometry("1350x750+0+0")
            self.win.title("restaurent management system")

            self.title_lable = Label(self.win,text="Restaurent Management System",font=('Arial',35,'bold'),bg="lightgray",bd=8,relief=GROOVE)
            self.title_lable.pack(side=TOP,fill=X)

            self.main_frame =Frame(self.win,bg="lightgray",bd=6,relief=GROOVE)
            self.main_frame.place(x=250,y=150,width=800,height=450)

            self.login_lbl = Lable(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgray",font=('sans-serif',25,'bold'))
            self.login_lbl.pack(side=TOP,fill=X)

        



        if __name__ == "__main__":
            main()

