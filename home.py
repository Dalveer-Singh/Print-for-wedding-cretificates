import tkinter as tk
import certificatePrint
import dashboard
import constants as CONST

certificatePrint.drawCanvas()

def Create():
    print("in create");
    
def check_log_in(master, user, password):
    # if (verify_password_name(user, password) == 0):
    #     return
    master.destroy()
    dashboard.drawDashboardWindow(user)

def draw_login_window(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry(CONST.SCREEN_SIZE)
    loginwn.title("Log in")
    loginwn.configure(bg=CONST.BG_COLOR)

    l_title = tk.Message(loginwn, text="Login", relief="raised", width=2000, padx=600, pady=0,
                         fg=CONST.TITLE_FG_COLOR, bg=CONST.TITLE_BG_COLOR, justify="center", anchor="center")
    l_title.config(font=("Sans", "50", "bold"))
    l_title.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    
    l2 = tk.Label(loginwn, text="Username/ Mobile:", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised")
    l2.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    userName = tk.Entry(loginwn)
    userName.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    l3 = tk.Label(loginwn, text="Password:", font=(CONST.LABEL_FONT,CONST. LABEL_SIZE), relief="raised")
    l3.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    password = tk.Entry(loginwn, show="*")
    password.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    btn_submit = tk.Button(loginwn, text="Submit", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: check_log_in(loginwn, userName.get().strip(), password.get().strip()),borderwidth=0,highlightthickness = 0)
    btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    # b1 = tk.Button(text="HOME", font=(LABEL_FONT, LABEL_SIZE), relief="raised", bg=TITLE_BG_COLOR, fg=TITLE_FG_COLOR, command=lambda: home_return(loginwn))
    # b1.pack(padx= (PADX0,PADX1 ),pady=(PADY0, PADY1))

    loginwn.bind("<Return>", lambda x: check_log_in(loginwn,  userName.get().strip(), password.get().strip()))

def Main_Menu():
    rootwn = tk.Tk()
    # rootwn.geometry(CONST.SCREEN_SIZE)
    # rootwn.title("Banking System (project) 11")
    # rootwn.configure(background='CadetBlue')
    fr1 = tk.Frame(rootwn)
    fr1.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    draw_login_window(rootwn)
    rootwn.mainloop()

def init():
    Main_Menu()

init();