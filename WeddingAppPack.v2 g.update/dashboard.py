import Tkinter as tk
import constants as CONST

def drawDashboardWindow():
    window = tk.Tk()
    #window.geometry(CONST.SCREEN_SIZE)
    window.title("Dashboard | "+CONST.LoggedInUser)
    window.configure(bg=CONST.BG_COLOR)
    window.iconbitmap(default='icon.ico')
    window.state('zoomed')
    # window.bind('<Escape>',CONST.quit)

    l_title = tk.Message(window, text="Wedding Certificates | Gurudwara Sector-7", relief="raised", width=2000, padx=600, pady=0,
                         fg=CONST.TITLE_FG_COLOR, bg=CONST.TITLE_BG_COLOR, justify="center", anchor="center")
    l_title.config(font=CONST.SUB_TITLE_FONT_CONFIG)
    l_title.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(0, CONST.PADY1))

    l_title = tk.Message(window, text="Dashboard", relief="raised", width=2000, padx=600, pady=0,
                         fg=CONST.TITLE_FG_COLOR, bg=CONST.TITLE_BG_COLOR, justify="center", anchor="center")
    l_title.config(font=CONST.TITLE_FONT_CONFIG)
    l_title.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(0, CONST.PADY1))

    fr1 = tk.Frame(window)
    fr1.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    btn_submit = tk.Button(window, text="Register New Users", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: check_log_in(loginwn, userName.get().strip(), password.get().strip()),borderwidth=0,highlightthickness = 0)
    # btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))
    
    btn_submit = tk.Button(window, text="Activity History", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: check_log_in(loginwn, userName.get().strip(), password.get().strip()),borderwidth=0,highlightthickness = 0)
    # btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    btn_submit = tk.Button(window, text="Create Certificate", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: CONST.openCertificateForm(window),borderwidth=0,highlightthickness = 0)
    btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    btn_submit = tk.Button(window, text="Find Certificate", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: CONST.openHistoryWindow(window), borderwidth=0,highlightthickness = 0)
    btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    btn_submit = tk.Button(window, text="Open Certificate Folder", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=lambda: CONST.openSaveFolder(), borderwidth=0,highlightthickness = 0)
    btn_submit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    btn_exit = tk.Button(window, text="Exit", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, command=window.destroy, borderwidth=0,highlightthickness = 0)
    btn_exit.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    window.mainloop()

def init():
    drawDashboardWindow()

if __name__ == "__main__":
    init()