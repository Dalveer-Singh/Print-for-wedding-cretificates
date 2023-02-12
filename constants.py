import os
import logging
import datetime

# Style Constants
# height = window.winfo_screenheight()
# print(width,height)
# window.geometry(str(width)+"x"+str(height))


# SCREEN_HEIGHT=800
# SCREEN_WIDTH=800
# SCREEN_SIZE=""
TITLE_FG_COLOR="gainsboro"
TITLE_BG_COLOR="#414169"
BG_COLOR="#EEEED5"
TITLE_FONT="sans"
TITLE_SIZE=32
TITLE_FONT_CONFIG =("Sans", "50", "bold")
SUB_TITLE_FONT_CONFIG =("Sans", "20", "bold")

LABEL_FONT="Sans"
LABEL_SIZE=16
LABEL_FONT_COLOR=TITLE_BG_COLOR

# LEFT_MARGIN=SCREEN_WIDTH/2-25
PADX0=0
PADX1=0
PADY0=15
PADY1=0

# Constants
STATIC_SAVE_PATH = os.path.join(os.path.expanduser("~"), "Documents/Anand Karaj Certificates/")
STATIC_LOG_PATH = "logs/" + "log.log"
TODAY_DATE=str(datetime.date.today());
APP_START_TIME = datetime.datetime.now().strftime("%H:%M:%S")
LOG_FORMAT =  '%(filename)s.%(funcName)s#%(lineno)d\t%(levelname)s:\t%(message)s'
VERSION = 2.0

# variables
LoggedInUser = "Dalveer Singh"
sessionId = "null"


# common modules
# def screenSize(height,width):
#     x=(str(height)+'x'+str(width))
#     global SCREEN_SIZE 
#     SCREEN_SIZE = x
#     return (x)

def getLabel(tk, window, text):
    label = tk.Label(window, text=text, font=(LABEL_FONT, LABEL_SIZE), bg=BG_COLOR)
    label.pack(side=tk.LEFT, pady=(PADY0, PADY1))
    # label.pack(side=tk.LEFT, padx= (PADX0,PADX1 ),pady=(PADY0, PADY1))
    return label;   

def getLabel_grid(tk, window, text):
    label = tk.Label(window, text=text, font=(LABEL_FONT, LABEL_SIZE),fg=LABEL_FONT_COLOR, bg=BG_COLOR)
    return label;   

def getEntry(tk, window):
    entry = tk.Entry(window)
    entry.pack(side=tk.LEFT, padx= (PADX0,PADX1 ),pady=(PADY0, PADY1))
    # entry.pack(padx= (PADX0,PADX1 ),pady=(PADY0, PADY1))
    return entry;

def getEntry_grid(tk, window):
    entry = tk.Entry(window, width=40, font=(LABEL_FONT, LABEL_SIZE))
    return entry;

def getSavePath(marriageDate=""):
    logging.info("getSavePath params: "+marriageDate)
    print("getSavePath params: "+marriageDate)

    # Default return oputput(pdf) path
    path= STATIC_SAVE_PATH + marriageDate + "/"
    if not (os.path.exists(path)):
        os.makedirs(path);
    return path;

def genrateFileName(formData):
    return formData['brideName'].split(" ")[0] +"_"+ formData['groomName'].split(" ")[0] + ".pdf";

def openSaveFolder(marriageDate=""):
    path = str( getSavePath( marriageDate=marriageDate ) )
    os.startfile( path )

def openPdfFile(marriageDate, fileName):
    path = str( getSavePath( marriageDate=marriageDate )) + fileName;
    os.startfile( path )

def openDashboard(window):
    window.destroy()
    import dashboard;
    dashboard.drawDashboardWindow()

def openCertificateForm(window):
    window.destroy()
    import certificateForm
    certificateForm.init()

def openHistoryWindow(window):
    window.destroy()
    import history
    history.init()

def select_all(event):
        widget = event.widget;
        # select text
        widget.select_range(0, 'end')
        # move cursor to the end
        widget.icursor('end')

if __name__ == "__main__":
    import dashboard
    dashboard.init()
