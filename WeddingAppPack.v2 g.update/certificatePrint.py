import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import calendar
import constants as CONST


PRINTABLE_CANVAS_HEIGHT = 595;
PRINTABLE_CANVAS_WIDTH = 842;
TODAY_DATE=str(datetime.date.today());
BG_IMAGE_PATH = "resources/marriage certificate.png"
PRINT_FONT = 'Vera'
PRINT_FONT_SIZE = 15;
LINE_HEIGHTS = {
    1:390, 2:313, 3:280, 4:250, 5:212, 6:177
}
XnY ={
    'S_NO_X' : 113,
    'S_NO_Y' : LINE_HEIGHTS.get(1),
    'PRINT_DATE_X' : 675,
    'PRINT_DATE_Y' : LINE_HEIGHTS.get(1),
    'GROOM_X' : 370,
    'GROOM_Y' : LINE_HEIGHTS.get(2),
    'GROOM_FATHER_X' : 626,
    'GROOM_FATHER_Y' : LINE_HEIGHTS.get(2),
    'GROOM_ADDRESS_X' : 153,
    'GROOM_ADDRESS_Y' : LINE_HEIGHTS.get(3),
    'GROOM_ID_X' : 240,
    'GROOM_ID_Y' : LINE_HEIGHTS.get(4),
    'BRIDE_X' : 425,
    'BRIDE_Y' : LINE_HEIGHTS.get(4),
    'BRIDE_FATHER_X' : 626,
    'BRIDE_FATHER_Y' : LINE_HEIGHTS.get(4),
    'BRIDE_ID_X' : 240,
    'BRIDE_ID_Y' : LINE_HEIGHTS.get(5),
    'BRIDE_ADDRESS_X' : 483,
    'BRIDE_ADDRESS_Y' : LINE_HEIGHTS.get(5),
    'BRIDE_ADDRESS_2_X' : 55,
    'BRIDE_ADDRESS_2_Y' : LINE_HEIGHTS.get(6),
    'MARRIAGE_DATE_X' : 567,
    'MARRIAGE_DATE_Y' : LINE_HEIGHTS.get(6),
    'MARRIAGE_DAY_X' : 712,
    'MARRIAGE_DAY_Y' : LINE_HEIGHTS.get(6)
}

def getDayy(date):
    a = date.split("-")
    d = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    day = calendar.day_name[d.weekday()]
    return day

def getNormalisedDate(date):
    a = date.split("-")
    d = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    month = calendar.month_abbr[int(a[1])]
    year = a[0]
    datee = a[2]
    returnDate = datee +" "+ month +" "+ year
    # print(returnDate)
    return returnDate;

# Fill form Data
def drawStrings(canvas,formData):
    canvas.drawString(x=XnY.get('S_NO_X'), y=XnY.get('S_NO_Y'),                     text= formData["s_no"]) 
    canvas.drawString(x=XnY.get('PRINT_DATE_X'), y=XnY.get('PRINT_DATE_Y'),         text= getNormalisedDate(str(TODAY_DATE))) 
    canvas.drawString(x=XnY.get('GROOM_X'), y=XnY.get('GROOM_Y'),                   text= formData["groomName"]) 
    canvas.drawString(x=XnY.get('GROOM_FATHER_X'), y=XnY.get('GROOM_FATHER_Y'),     text= formData["groomFather"]) 
    canvas.drawString(x=XnY.get('GROOM_ADDRESS_X'), y=XnY.get('GROOM_ADDRESS_Y'),   text= formData["groomAddress"]) 
    canvas.drawString(x=XnY.get('GROOM_ID_X'), y=XnY.get('GROOM_ID_Y'),             text= formData["groomId"]) 
    canvas.drawString(x=XnY.get('BRIDE_X'), y=XnY.get('BRIDE_Y'),                   text= formData["brideName"]) 
    canvas.drawString(x=XnY.get('BRIDE_FATHER_X'), y=XnY.get('BRIDE_FATHER_Y'),     text= formData["brideFather"]) 
    canvas.drawString(x=XnY.get('BRIDE_ID_X'), y=XnY.get('BRIDE_ID_Y'),             text= formData["brideId"]) 
    canvas.drawString(x=XnY.get('BRIDE_ADDRESS_X'), y=XnY.get('BRIDE_ADDRESS_Y'),   text= formData["brideAddress"]) 
    canvas.drawString(x=XnY.get('BRIDE_ADDRESS_2_X'),y=XnY.get('BRIDE_ADDRESS_2_Y'),text= formData["brideAddress2"]) 
    canvas.drawString(x=XnY.get('MARRIAGE_DATE_X'), y=XnY.get('MARRIAGE_DATE_Y'),   text= getNormalisedDate(formData["marriageDate"])) 
    canvas.drawString(x=XnY.get('MARRIAGE_DAY_X'), y=XnY.get('MARRIAGE_DAY_Y'),     text= getDayy(formData["marriageDate"])) 

def createPDF(formData):
    fileName = CONST.genrateFileName(formData);
    # fileName = formData['brideName'].split(" ")[0] +"_"+ formData['groomName'].split(" ")[0] + ".pdf";
    savePath = CONST.getSavePath(marriageDate=formData['marriageDate']);
    print("save path: "+ savePath)

    canvas_with_BG = Canvas(savePath + fileName, pagesize=landscape(letter))
    canvas_printable = Canvas(savePath + "print_" + fileName, pagesize=landscape(letter))

    # set font and size
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    canvas_with_BG.setFont(PRINT_FONT, PRINT_FONT_SIZE)
    canvas_printable.setFont(PRINT_FONT, PRINT_FONT_SIZE)

    # set page size
    canvas_with_BG.setPageSize((PRINTABLE_CANVAS_WIDTH, PRINTABLE_CANVAS_HEIGHT))
    canvas_printable.setPageSize((PRINTABLE_CANVAS_WIDTH, PRINTABLE_CANVAS_HEIGHT))

    # set BG image
    canvas_with_BG.drawImage(BG_IMAGE_PATH, 0, -15, height=PRINTABLE_CANVAS_HEIGHT+10, width=PRINTABLE_CANVAS_WIDTH, preserveAspectRatio=False, mask=[0])
    
    drawStrings(canvas_with_BG, formData)
    drawStrings(canvas_printable, formData)

    canvas_with_BG.showPage()
    canvas_printable.showPage()

    canvas_with_BG.save()
    canvas_printable.save()


#########################
def printCertificate(data):
    formData = data;
    createPDF(formData=formData);    

if __name__ == "__main__":
    import certificateForm