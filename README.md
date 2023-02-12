# Wedding-Certificate-Printing-GUI-Application
Use friendly GUI desigend for very specific certificate printitng requirement, where pre-printed (blank) certificates were available, and software to fill out the gaps was required. 

     Useful for small institutions looking for easy way to create fillable certificates.
        It uses tkinter GUI to gather information. 
        It uses csv file to store the data. 
        It uses reportlab to create output PDF

### Requirements:
- Python 2.7 - [download here](https://www.python.org/downloads/release/python-2718/)
- Windows 7 or above
- pip        19.2.3 - included with this Python version. (use `python -m pip` | ex. `python -m pip install reportlab`)
- reportlab  3.5.59
- Tkinter    1.0
- tkcalendar 1.6.1
- Microsoft Visual C++ 9.0  - [download here](https://web.archive.org/web/20200709160228if_/https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi)


After checking out the code, use .bat file or dashboard.py to inititate the application.

### RoadMap / Bugs list:
    login() - Login/ validation/ Entry Point / reset password.
    form() 
        - gather marriage info ✅
        - real-time Entry length limit (ex.address 75chars)
        - more info to gather? phone Numbers
        - Edit btn in form, with pre-information
    preview() - with bg image ✅
    print() - to PDF ✅
    logging enabled ✅
    Trim old Logs - to save space.
    store - CSV, maintain records ✅
    Report Bug/ feedback
    Dashboard() 
        - view history - activity(who printed/ created)
            - rePrint
        - users (new/block/delete/unblock) (ADMIN only)
        - create certificate ✅
    History() 
        view:
            - scrollbar ✅
            - search 
            - sort
        Actions:
            - reprint 
            - open folder/ file
    Notification()
        - user update
        - print update.
    Publish to GIT 
        - publish ✅
        - link git to code
        - make exe/ or downloadable lib 
    Report a Bug
    
## Wedding certificate printing
* @ 2023
* @ Author - Dalveer Singh
* sunnny433@gmail.com | [git](https://github.com/Dalveer-Singh) | [linkedin](https://www.linkedin.com/in/-dalveersingh/)
* Dont forget to mention us 🙂👍
