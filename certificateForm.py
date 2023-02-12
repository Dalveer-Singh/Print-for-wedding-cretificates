import logging
import Tkinter as tk
import tkMessageBox as messagebox
import constants as CONST
import certificatePrint
from tkcalendar import DateEntry
import DB

formObject = {}
collectedFormadata={};
buttons ={}
logging.basicConfig(filename=CONST.STATIC_LOG_PATH, level=logging.INFO, format=CONST.LOG_FORMAT)


def drawCertificateForm():
    window = tk.Tk()
    # window.geometry(CONST.SCREEN_SIZE)
    window.state('zoomed')
    window.title("Dashboard | "+CONST.LoggedInUser)
    window.configure(bg=CONST.BG_COLOR)
    window.grid_columnconfigure((0,1), weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    window.bind('<Control-a>',CONST.select_all)
    
                      
    l_title = tk.Message(window, text="Details", relief="raised", width=2000, padx=600, pady=0,
                         fg=CONST.TITLE_FG_COLOR, bg=CONST.TITLE_BG_COLOR, justify="center", anchor="center")
    l_title.config(font=("Sans", "50", "bold"))
    l_title.grid(row=0, column=0, columnspan=2)

    # form data
    l1 = CONST.getLabel_grid(tk, window, "S.no."); 
    formObject['s_no']= CONST.getEntry_grid(tk,window)

    updateSNoValue(formObject['s_no'], DB.getLatestSNo()+1)
    l1.grid(row=1, column=0)
    formObject['s_no'].grid(row=1, column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Groom Name."); 
    formObject['groomName']= CONST.getEntry_grid(tk,window)
    l1.grid(row=2,column=0)
    formObject['groomName'].grid(row=2,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Groom's Father"); 
    formObject['groomFather']= CONST.getEntry_grid(tk,window)
    l1.grid(row=3,column=0)
    formObject['groomFather'].grid(row=3,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Groom's Address"); 
    formObject['groomAddress']= CONST.getEntry_grid(tk,window)
    l1.grid(row=4,column=0)
    formObject['groomAddress'].grid(row=4,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Groom's passport/ Adhar"); 
    formObject['groomId']= CONST.getEntry_grid(tk,window)
    l1.grid(row=5,column=0)
    formObject['groomId'].grid(row=5,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Bride Name"); 
    formObject['brideName']= CONST.getEntry_grid(tk,window)
    l1.grid(row=6,column=0)
    formObject['brideName'].grid(row=6,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Bride's Father"); 
    formObject['brideFather']= CONST.getEntry_grid(tk,window)
    l1.grid(row=7,column=0)
    formObject['brideFather'].grid(row=7,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Bride's passport/ Adhar"); 
    formObject['brideId']= CONST.getEntry_grid(tk,window)
    l1.grid(row=8,column=0)
    formObject['brideId'].grid(row=8,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Bride's Address"); 
    formObject['brideAddress']= CONST.getEntry_grid(tk,window)
    l1.grid(row=9,column=0)
    formObject['brideAddress'].grid(row=9,column=1, pady=4)

    l1 = CONST.getLabel_grid(tk, window, "Marriage Date"); 
    formObject['marriageDate']= DateEntry(window, font="Sans 16", date_pattern='yyyy-MM-dd', width= 38, background=CONST.TITLE_BG_COLOR, justify='right', headersbackground="white", showweeknumbers=False, weekendbackground="white", othermonthwebackground="gray93", showothermonthdays=False)
    l1.grid(row=10,column=0)
    formObject['marriageDate'].grid(row=10,column=1, pady=4)

    btn_submit = tk.Button(window, text="Submit", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
        command=lambda: submit(),        borderwidth=0,highlightthickness = 0)
    btn_submit.grid(row=11, column=1,  padx=(150, 0))
    buttons["btn_submit"]=btn_submit;       

    btn_back_to_dashboard = tk.Button(window, text="Back", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised",     bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR,
        command=lambda: CONST.openDashboard(window), borderwidth=0,highlightthickness = 0)
    btn_back_to_dashboard.grid(row=11, column=0, padx=(0, 100), pady=10)
    buttons["btn_back_to_dashboard"]=btn_back_to_dashboard;

    btn_preview = tk.Button(window, text="Preview", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised", bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
        command=lambda:  CONST.openPdfFile(collectedFormadata['marriageDate'], CONST.genrateFileName(collectedFormadata) ),        borderwidth=0,highlightthickness = 0)
    buttons["btn_preview"]=btn_preview;

    btn_open_folder = tk.Button(window, text="Open Save Folder", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised",     bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
        command=lambda: CONST.openSaveFolder(collectedFormadata['marriageDate']), borderwidth=0,highlightthickness = 0)
    buttons["btn_open_folder"]=btn_open_folder;

    btn_open_print_pdf = tk.Button(window, text="Print", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised",     bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
        command=lambda: CONST.openPdfFile(collectedFormadata['marriageDate'], "print_"+CONST.genrateFileName(collectedFormadata) ), borderwidth=0,highlightthickness = 0)
    buttons["btn_open_print_pdf"]=btn_open_print_pdf;

    btn_new_form = tk.Button(window, text="New", font=(CONST.LABEL_FONT, CONST.LABEL_SIZE), relief="raised",     bg=CONST.TITLE_BG_COLOR, fg=CONST.TITLE_FG_COLOR, 
        command=lambda: CONST.openCertificateForm(window), borderwidth=0,highlightthickness = 0)
    buttons["btn_new_form"]=btn_new_form;

    window.mainloop()

def hide_button(widget):
    widget.grid_forget()

def show_button(widget):
    widget.grid() # pack

def showResultButtons():
    buttons["btn_open_print_pdf"].grid(row=11, column=1, padx=(210, 0), pady=10)
    buttons["btn_open_folder"].grid(row=11, column=1, padx=(0, 210), pady=10, )
    buttons["btn_preview"].grid(row=12, column=1,  padx=(180, 0), pady=10)
    buttons["btn_new_form"].grid(row=13, column=1,  padx=(210, 0), pady=10)
    
def promptErro(errorMsg):
    return "Error: " + errorMsg + "\n"

def validateInformation(formdata):
    groomAddressLimit = 75
    brideAddressLimit_1 = 35
    brideAddressLimit_2 = 22
    idLimit=16
    groomNameLimit=26
    brideNameLimit = 22
    fatherNameLimit=20

    errorMsg = "";
    if(collectedFormadata['s_no'].strip()         == "" ): errorMsg=errorMsg+ promptErro("S.No")
    if(collectedFormadata['groomName'].strip()    == "" ): 
        errorMsg=errorMsg+ promptErro("Groom Name")
    elif( len(collectedFormadata['groomName']) > groomNameLimit):
        collectedFormadata['groomName'] = collectedFormadata['groomName'][0:groomNameLimit]

    if(collectedFormadata['groomFather'].strip()  == "" ): errorMsg=errorMsg+ promptErro("Groom Father")
    if(collectedFormadata['groomAddress'].strip() == "" ):
        errorMsg=errorMsg+ promptErro("Groom Address")
    elif (len(collectedFormadata['groomAddress'].strip()) > groomAddressLimit):
        collectedFormadata['groomAddress'] = collectedFormadata['groomAddress'][0:groomAddressLimit]

    if(collectedFormadata['groomId'].strip()      == "" ):
        errorMsg=errorMsg+ promptErro("Groom Id")
    elif(len(collectedFormadata['groomId']) > idLimit):
        errorMsg=errorMsg+ promptErro("Groom Id - Long Len. Max:" + str(idLimit))

    if(collectedFormadata['brideName'].strip()    == "" ): 
        errorMsg=errorMsg+ promptErro("Bride Name")
    elif( len(collectedFormadata['brideName']) > brideNameLimit):
        collectedFormadata['brideName'] = collectedFormadata['brideName'][0:brideNameLimit]

    if(collectedFormadata['brideFather'].strip()  == "" ): errorMsg=errorMsg+ promptErro("Bride Father")
    if(collectedFormadata['brideId'].strip()      == "" ): 
        errorMsg=errorMsg+ promptErro("Bride Id")
    elif(len(collectedFormadata['brideId']) > idLimit):
        errorMsg=errorMsg+ promptErro("Bride Id - Long Len. Max:"+ str(idLimit))

    if(collectedFormadata['brideAddress'].strip() == "" ): 
        errorMsg=errorMsg+ promptErro("Bride Address")
    elif (len(collectedFormadata['brideAddress'].strip()) > brideAddressLimit_1):
        collectedFormadata['brideAddress2'] = collectedFormadata['brideAddress'][brideAddressLimit_1:brideAddressLimit_1+brideAddressLimit_2]
        collectedFormadata['brideAddress'] = collectedFormadata['brideAddress'][0:brideAddressLimit_1]

    if(collectedFormadata['marriageDate'].strip() == "" ): errorMsg=errorMsg+ promptErro("Marriage Date")

    if len(errorMsg)!=0: #if length == 0, then no error
        messagebox.showerror("ERROR",errorMsg, icon= "error")
        return False # return false if error
    return True # ture, no error/ valid info

def updateSNoValue(obj, value):
    obj.config(state= "normal")
    if len(obj.get()) > 0 : obj.delete(0,obj.get())
    obj.insert(0, value)
    obj.config(state= "disabled")

def updateEntryValue(obj, value):
    if len(obj.get()) > 0 : obj.delete(0,obj.get())
    obj.insert(0, value)

def submit():
    #read Information
    collectedFormadata['s_no']          =   formObject['s_no']        .get().strip()
    collectedFormadata['groomName']     =   formObject['groomName']   .get().strip()
    collectedFormadata['groomFather']   =   formObject['groomFather'] .get().strip()
    collectedFormadata['groomAddress']  =   formObject['groomAddress'].get().strip()
    collectedFormadata['groomId']       =   formObject['groomId']     .get().strip()
    collectedFormadata['brideName']     =   formObject['brideName']   .get().strip()
    collectedFormadata['brideFather']   =   formObject['brideFather'] .get().strip()
    collectedFormadata['brideId']       =   formObject['brideId']     .get().strip()
    collectedFormadata['brideAddress']  =   formObject['brideAddress'].get().strip()
    collectedFormadata['brideAddress2']  =  ""
    collectedFormadata['marriageDate']  =   formObject['marriageDate'].get().strip()
    collectedFormadata['marriageDate_obj']= formObject['marriageDate']
    
    print("collectedFormadata: "+str(collectedFormadata))
    logging.info("collectedFormadata: "+str(collectedFormadata))

    if not validateInformation(formObject):
        print();
        return;

    formdata_str = "Are details correct?"


    isCreatePdf = messagebox.askyesno("Verify Details", formdata_str)
    if isCreatePdf:  #if pdf save success
        # Create and save PDF
        certificatePrint.printCertificate(collectedFormadata)
        DB.writeEntry(collectedFormadata)
        messagebox.showinfo("Success","Successfully Created", icon= "info")
        showResultButtons();
        hide_button(buttons["btn_submit"]);


def init():
    appStartLog = "\n**************************************\n******** "+CONST.TODAY_DATE+" "+CONST.APP_START_TIME+" *********\n**************************************"
    logging.info(appStartLog)
    drawCertificateForm()

if __name__ == "__main__":
    init()
