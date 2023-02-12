from Tkinter import *
# import Tkinter as tk
import constants as CONST
import ttk
import DB

def drawHistoryWindow():
    ws  = Tk()
    ws.title("HISTORY | "+CONST.LoggedInUser)
    # ws.geometry(CONST.SCREEN_SIZE)
    ws.state('zoomed')
    ws.configure(bg=CONST.BG_COLOR)
    # ws.bind('<Escape>',CONST.quit)

    

    l_title = Message(ws, text="History", relief="raised", width=2000, padx=600, pady=0,
                         fg=CONST.TITLE_FG_COLOR, bg=CONST.TITLE_BG_COLOR, justify="center", anchor="center")
    l_title.config(font=("Sans", "50", "bold"))
    l_title.pack(padx= (CONST.PADX0,CONST.PADX1 ),pady=(CONST.PADY0, CONST.PADY1))

    game_frame = Frame(ws)
    game_frame.pack()

    #scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)
    game_scroll = Scrollbar(game_frame,orient='horizontal')
    game_scroll.pack(side= BOTTOM,fill=X)
    # my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
    my_game = ttk.Treeview(game_frame, show='headings', height=24)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 8))
    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)
    my_game.pack()


    #define our column
    # my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
    # my_game['columns'] = ('s_no', 'groomName', 'groomFather', 'groomAddress', 'groomId', 'brideName', 'brideFather', 'brideId', 'brideAddress', 'marriageDate')
    my_game['columns'] = DB.fields

    # format our column
    my_game.column("#0", width=0,  stretch=YES)
    my_game.column("s_no",anchor=CENTER, width=40)
    my_game.column("groomName",anchor=CENTER,width=100)
    my_game.column("groomFather",anchor=CENTER,width=100)
    my_game.column("groomAddress",anchor=CENTER,width=100)
    my_game.column("groomId",anchor=CENTER,width=100)
    my_game.column("brideName",anchor=CENTER,width=100)
    my_game.column("brideFather",anchor=CENTER,width=100)
    my_game.column("brideId",anchor=CENTER,width=100)
    my_game.column("brideAddress",anchor=CENTER,width=100)
    my_game.column("marriageDate",anchor=CENTER,width=100)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("s_no",text="S no",anchor=CENTER)
    my_game.heading("groomName",text="Groom",anchor=CENTER)
    my_game.heading("groomFather",text="Groom's Father",anchor=CENTER)
    my_game.heading("groomAddress",text="Groom Address",anchor=CENTER)
    my_game.heading("groomId",text="Groom Id",anchor=CENTER)
    my_game.heading("brideName",text="Bride Name",anchor=CENTER)
    my_game.heading("brideFather",text="Bride Father",anchor=CENTER)
    my_game.heading("brideId",text="Bride Id",anchor=CENTER)
    my_game.heading("brideAddress",text="Bride Address",anchor=CENTER)
    my_game.heading("marriageDate",text="Marriage Date",anchor=CENTER)

    #add data 
    rows = DB.readEntries()
    iid = 0
    for x in range(len(rows), 0, -1):
        row = rows[x-1]
        my_game.insert(parent='',index='end',iid=iid,text='',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        iid = iid+1
    my_game.pack()

    btn_back_to_dashboard = Button(ws, text="Back", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised",
                            bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
                            command=lambda: CONST.openDashboard(ws), borderwidth=0,highlightthickness = 0, width=50)
    btn_back_to_dashboard.pack(pady=10)

    ws.mainloop()

def init():
    drawHistoryWindow()

if __name__ == "__main__":
    init()
    
